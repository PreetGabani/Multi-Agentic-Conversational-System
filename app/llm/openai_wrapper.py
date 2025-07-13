import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_llm_response(prompt, context=""):
    messages = [{"role": "system", "content": "You are a helpful assistant with access to internal company knowledge."}]
    if context:
        messages.append({"role": "system", "content": f"Relevant info: {context}"})
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response['choices'][0]['message']['content']
