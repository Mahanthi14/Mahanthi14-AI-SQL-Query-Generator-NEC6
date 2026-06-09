import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

def generate_sql(question):

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
                "content": f"""
Convert the following question into SQLite SQL.

Table Name: employees

Columns:
id
name
department
salary

Question:
{question}

Return only SQL query.
"""
            }
        ],
        "max_tokens": 100
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    result = response.json()

    sql = result["choices"][0]["message"]["content"]

    return sql.strip()