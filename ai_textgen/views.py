import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def interact_with_ollama(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_prompt = data.get("prompt", "")
            if not user_prompt:
                return JsonResponse({"error": "Prompt is required"}, status=400)

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

                    except json.JSONDecodeError as e:
                        return JsonResponse(
                            {"error": "Malformed response", "details": str(e)},
                            status=500,
                        )
                response_string = "".join(results)

                return JsonResponse({"results": response_string}, safe=False)
            else:
                return JsonResponse(
                    {
                        "error": "Error communicating with Ollama",
                        "details": response.text,
                    },
                    status=response.status_code,
                )

        except Exception as e:
            return JsonResponse(
                {"error": "An error occurred", "details": str(e)}, status=500
            )
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def run_web_scrap(request):
    try:
        result = subprocess.run(
            ["python3", "web_scrap.py"], capture_output=True, text=True
        )

        if result.returncode == 0:
            return JsonResponse({"status": "success", "output": result.stdout})
        else:
            return JsonResponse({"status": "error", "message": result.stderr})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
