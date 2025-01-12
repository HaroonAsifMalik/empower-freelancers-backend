from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
from .models import *


@receiver(post_save, sender=WebScrapingJob)
def generate_ai_proposal(sender, instance, created, **kwargs):
    if created:
        try:
            user_prompt = instance.description
            if not user_prompt:
                return

            OLLAMA_API_URL = "http://localhost:11434/api/generate"
            headers = {"Content-Type": "application/json"}
            payload = {"model": "llama2:7b", "prompt": user_prompt, "max_token": 20}

            response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                results = []
                for line in response.text.strip().split("\n"):
                    try:
                        data = json.loads(line)
                        results.append(data["response"])
                    except json.JSONDecodeError:
                        continue
                
                response_string = "".join(results)
                
                AIProposalResponse.objects.create(job=instance, description=response_string)
            else:
                print(f"Error communicating with Ollama: {response.text}")

        except Exception as e:
            print(f"An error occurred while generating AI proposal: {e}")
