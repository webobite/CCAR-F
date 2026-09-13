import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.aicredits.in/v1",
    api_key=os.environ.get("AICREDITS_API_KEY"),
)

# Using Haiku (cheapest — best for practice)
response = client.chat.completions.create(
    model="anthropic/claude-haiku-4.5",
    messages=[
        {"role": "user", "content": "What is prompt caching in Claude? Explain in 2 lines."}
    ],
    max_tokens=200,
)

print(response.choices[0].message.content)