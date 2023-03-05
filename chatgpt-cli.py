import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_SECRET_KEY"]

messages=[{"role": "system", "content": "You are a helpful assistant."}]
def chat(messages):
  res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  return res


while True:
    prompt = input("Enter a prompt: ")
    messages.append({"role": "user", "content": prompt})

    completions = chat(messages)

    response = completions['choices'][0]['message']['content']
    print(response)
    messages.append({"role": "assistant", "content": response})