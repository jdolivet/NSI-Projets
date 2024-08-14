from openai import OpenAI
import base64

client = OpenAI(
    api_key=""
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

while True:
    base64_image = encode_image(input("Entrez le chemin du captcha\n> "))

    completion = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    temperature=0,
    messages=[
        {"role": "system", "content": "You are an assistant for a program helping the blind. You must specify what the contents of the image are. The images usually contain noise, in the form of dots and lines. You must reply with only the contents of the image and no descriptions."},
        {
        "role": "user",
        "content": [
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            }
            }
        ]
        }
    ]
    )

    print(f"Le code est: {completion.choices[0].message.content.replace(" ", "")}")