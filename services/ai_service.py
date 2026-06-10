from openai import OpenAI

from config import Config

client = OpenAI(
    api_key=
    Config.OPENAI_API_KEY
)

SYSTEM_PROMPT = """

You are a highly intelligent AI Assistant.

Capabilities:

- Coding
- Mathematics
- Science
- Writing
- Reasoning
- Research

Always provide
well structured answers.

"""

def ask_ai(messages):

    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[
            {
                "role":"system",
                "content":
                SYSTEM_PROMPT
            }
        ] + messages,

        temperature=0.7,

        max_tokens=1500
    )

    return response.choices[0].message.content
