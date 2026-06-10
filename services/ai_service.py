from openai import OpenAI
from config import Config

client = OpenAI(
    api_key=Config.OPENAI_API_KEY
)

def generate_response(message):

    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[
            {
                "role": "system",
                "content":
                """
                You are an advanced AI assistant.
                Provide accurate responses.
                """
            },
            {
                "role": "user",
                "content": message
            }
        ],

        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content
