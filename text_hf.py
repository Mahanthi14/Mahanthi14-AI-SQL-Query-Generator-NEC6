import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

url = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "model": "openai/gpt-oss-20b",
    "messages": [
        {
            "role": "user",
            "content": "Convert to SQL: Show all employees. Table: employees(id, name, department, salary). Return only SQL."
        }
    ],
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)