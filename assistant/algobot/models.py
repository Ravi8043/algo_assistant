from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

@csrf_exempt
def ask_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query', '').lower()

        # Load the FAQ JSON file
        with open(os.path.join(os.path.dirname(__file__), 'faq.json')) as f:
            faqs = json.load(f)
        
        # Step 1: Check in FAQs
        if query in faqs:
            return JsonResponse({'response': faqs[query]})

        # Step 2: Placeholder for DeepSeek
        return JsonResponse({'response': f"🔍 [DeepSeek] Answer for: {query}"})
    
    return JsonResponse({'error': 'Only POST allowed'}, status=405)


# Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question