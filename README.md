# hackseries-algo_assistant

A Django-based AI-powered assistant for algorithmic and FAQ support, leveraging Hugging Face models and local knowledge bases.

## Overview

**hackseries-algo_assistant** is a web application built using Django that provides an interactive assistant for answering algorithmic and general FAQ-style questions. It uses a hybrid approach of:
- Looking up answers from a local FAQ database.
- Generating responses using Hugging Face language models when answers are not found locally.
- Supporting fine-tuning and inference with custom Hugging Face models.

This project is suitable for educational, hackathon, or research use cases where a blend of static and dynamic question answering is desired.

## Features

- **AI-Powered Q&A:** Uses Hugging Face models (e.g., Zephyr-7b-beta) for intelligent, context-aware answers.
- **Local FAQ Lookup:** Answers common questions instantly from an FAQ database.
- **Fine-Tuning Support:** Provides API endpoints to fine-tune models with custom prompts.
- **REST API:** Simple POST endpoints for both Q&A and fine-tuning operations.
- **Django Admin:** Manage FAQ entries via Django’s admin interface.
- **Environment-based Configuration:** Securely manage keys and model identifiers via environment variables.

## Directory Structure

```
assistant/
  ├── algobot/
  │   ├── admin.py
  │   ├── apps.py
  │   ├── migrations/
  │   ├── models.py
  │   ├── tests.py
  │   ├── urls.py
  │   ├── views.py
  │   └── (faq.json)
  ├── assistant/
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── manage.py
```

## API Endpoints

- **POST `/ask/`**
  - Request: `{ "query": "Your question here" }`
  - Response: `{ "response": "AI or FAQ answer" }`
- **POST `/fine_tune/`**
  - Request: `{ "query": "Prompt or fine-tuning instruction" }`
  - Response: `{ "response": "Fine-tuned model output" }`

## Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/Ravi8043/hackseries-algo_assistant.git
   cd hackseries-algo_assistant/assistant
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Requirements**
   ```bash
   pip install django python-dotenv huggingface_hub
   ```

4. **Set Environment Variables**
   Create a `.env` file in the `assistant/algobot` directory:
   ```
   HUGGINGFACE_API_KEY=your_hf_api_key
   HUGGINGFACE_API_KEY_1=your_hf_api_key_alt
   HUGGINGFACE_USER=your_hf_username
   HUGGINGFACE_MODEL_ID=your_model_id
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **(Optional) Add FAQ Entries**
   Access the Django admin to populate FAQ entries or add a `faq.json` file.

## Example Usage

```bash
curl -X POST http://localhost:8000/ask/ -H "Content-Type: application/json" -d '{"query": "What is Algorand?"}'
```

## Testing

Run the automated tests:
```bash
python manage.py test algobot
```

## License

MIT License

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Hugging Face](https://huggingface.co/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

*Project maintained by [Ravi8043](https://github.com/Ravi8043)*
