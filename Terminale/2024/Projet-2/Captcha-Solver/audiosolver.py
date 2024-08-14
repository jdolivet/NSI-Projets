import whisper
from openai import OpenAI
from time import perf_counter


model = whisper.load_model("large")

client = OpenAI(
    api_key=""
)

while True:
    result = model.transcribe(input("Entrez le chemin du captcha\n> "))

    completion = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        temperature=0,
        messages=[
            {"role": "system", "content": "Você agora é um assistente de compreensão de texto. Ira ser soletrado um código, e você devera retornar apenas este código."},
            {
            "role": "user",
            "content": result["text"]
            }
        ]
    )

    print(f"Le code est: {completion.choices[0].message.content}")
