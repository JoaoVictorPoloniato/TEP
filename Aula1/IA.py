import os
from groq import Groq
#  $env:GROQ_API_KEY="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"
# Acessa a API Key da variável de ambiente
api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Qual a capital do MT Brasil",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
