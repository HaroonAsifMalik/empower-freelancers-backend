import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ai_textgen.serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# @csrf_exempt
# def interact_with_ollama(request):
#     if request.method == "POST":
#         try:
            
#             user_prompt =  WebScrapingJob.objects.first().description
#             if not user_prompt:
#                 return JsonResponse({"error": "Prompt is required"}, status=400)

#             OLLAMA_API_URL = "http://localhost:11434/api/generate"
#             headers = {"Content-Type": "application/json"}
#             payload = {"model": "llama2:7b", "prompt": user_prompt, "max_token": 20}
#             response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)

#             if response.status_code == 200:
#                 results = []
#                 for line in response.text.strip().split("\n"):
#                     try:
#                         data = json.loads(line)
#                         results.append(data["response"])

#                     except json.JSONDecodeError as e:
#                         return JsonResponse(
#                             {"error": "Malformed response", "details": str(e)},
#                             status=500,
#                         )
#                 response_string = "".join(results)

#                 return JsonResponse({"results": response_string}, safe=False)
#             else:
#                 return JsonResponse(
#                     {
#                         "error": "Error communicating with Ollama",
#                         "details": response.text,
#                     },
#                     status=response.status_code,
#                 )

#         except Exception as e:
#             return JsonResponse(
#                 {"error": "An error occurred", "details": str(e)}, status=500
#             )
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)



class AIProposalResponseListView(APIView):
    def get(self, request):
        responses = AIProposalResponse.objects.all()
        serializer = AIProposalResponseSerializer(responses, many=True)
        return Response({"status": "success", "jobs": serializer.data}, status=200)


@csrf_exempt
def run_web_scrap(request):
    try:
        result = subprocess.run(
            ["python3", "web_scrap.py"], capture_output=True, text=True
        )

        if result.returncode == 0:
            try:
                jobs = json.loads(result.stdout)
                first_job = jobs[0]

                serializer = WebScrapingJobSerializer(data=first_job)
                if serializer.is_valid():
                    serializer.save()  # 
                
                return JsonResponse({"status": "success", "jobs": jobs})
            except json.JSONDecodeError:
                return JsonResponse({"status": "error", "message": "Invalid JSON format in script output"})
        else:
            return JsonResponse({"status": "error", "message": result.stderr})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
