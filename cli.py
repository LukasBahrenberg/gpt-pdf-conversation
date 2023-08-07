import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = []

while True:
    cli_input = input(">>> ")
    prompt = {"role" : "user", "content" : cli_input}
    chat_history.append(prompt)
    output: str = ""
    for chunk in openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=chat_history,
        temperature=0.5, 
        stream=True
    ):
        content = chunk["choices"][0].get("delta", {}).get("content")
        if content is not None:
            print(content, end='')
            output += content
        
    print('\n')
    chat_history.append({"role" : "assistant", "content" : output})