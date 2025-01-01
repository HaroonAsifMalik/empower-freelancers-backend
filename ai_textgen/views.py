import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def interact_with_ollama(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON payload
            data = json.loads(request.body)
            user_prompt = data.get("prompt", "")
            if not user_prompt:
                return JsonResponse({"error": "Prompt is required"}, status=400)

            OLLAMA_API_URL = "http://localhost:11434/api/generate"
            headers = {"Content-Type": "application/json"}
            payload = {"model": "llama2:7b", "prompt": user_prompt, "max_token": 20}
            response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                # Handle multi-line JSON response
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
