from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient, HfApi
import traceback

load_dotenv()  # Load environment variables

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HUGGINGFACE_API_KEY_1 = os.getenv("HUGGINGFACE_API_KEY_1")
HUGGINGFACE_USER = os.getenv("HUGGINGFACE_USER")  # Hugging Face username
HUGGINGFACE_MODEL_ID = os.getenv("HUGGINGFACE_MODEL_ID")  # Name of your model on Hugging Face Hub

@csrf_exempt
def ask_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query', '').strip()

            if not query:
                return JsonResponse({'error': 'Query is empty'}, status=400)

            # Step 1: Check in local FAQ
            faq_path = os.path.join(os.path.dirname(__file__), 'faq.json')
            if os.path.exists(faq_path):
                with open(faq_path) as f:
                    faqs = json.load(f)

                if query.lower() in faqs:
                    return JsonResponse({'response': faqs[query.lower()]})

            # Step 2: If not in FAQ, send to Hugging Face Inference API
            client = InferenceClient(api_key=HUGGINGFACE_API_KEY)

            completion = client.chat.completions.create(
                model="HuggingFaceH4/zephyr-7b-beta",
                messages=[
                    {
                        "role": "user",
                        "content": query
                    }
                ],
                max_tokens=512,
            )

            generated = completion.choices[0].message.get('content', 'No response generated.')
            return JsonResponse({'response': f" {generated}"})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)


# New View for Fine-Tuning the Model


@csrf_exempt
def fine_tune_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query', '').strip()

            if not query:
                return JsonResponse({'error': 'Query is empty'}, status=400)

            # Log which model you *intend* to use
            full_model_path = f"{HUGGINGFACE_USER}/{HUGGINGFACE_MODEL_ID}"
            print(f"🔥 Using model from env: {full_model_path}")

            # Optional: fetch actual model metadata from Hugging Face
            api = HfApi()
            model_info = api.model_info(full_model_path)
            print(f"📦 Actual model base: {model_info.modelId}")
            print(f"🧠 Model config: {model_info.config}")
            print(f"📄 Model tags: {model_info.tags}")

            # Use the InferenceClient
            client = InferenceClient(
                model=full_model_path,
                token=HUGGINGFACE_API_KEY_1
            )

            response = client.text_generation(
                prompt=query,
                max_new_tokens=512,
                temperature=0.7,
                top_p=0.95,
                do_sample=True
            )

            return JsonResponse({'response': response.strip()})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)
        except Exception as e:
            print("💥 Exception occurred:")
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)