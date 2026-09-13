import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # walks up from cwd, picks up the shared .env at repo root

client = OpenAI(base_url=os.environ.get("AICREDITS_BASE_URL"), api_key=os.environ.get("AICREDITS_API_KEY"))

# Using Haiku (cheapest — best for practice)
response = client.chat.completions.create(
    model="anthropic/claude-haiku-4.5",
    messages=[
        {"role": "user", "content": "What is prompt caching in Claude? Explain in 2 lines."}
    ],
    max_tokens=200,
)

print(response.choices[0].message.content)