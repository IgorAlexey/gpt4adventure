from rich import print
from rich.text import Text
from rich.errors import MarkupError
from dotenv import load_dotenv
import os
import sys
import openai
from art import *

load_dotenv()

def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

file = open("system.txt", "r")
system_prompt = file.read()
file.close()
file = open("welcome.txt", "r")
welcome_prompt = file.read()
file.close()

art = text2art("Adventure", font="small")

openai.api_key = os.getenv("OPENAI_API_KEY")

chat = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "assistant",
        "content": welcome_prompt,
    },
]

def append_to_chat(role, content):
    chat.append({"role": role, "content": content})

def get_chat_response():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat,
        temperature=1.05,
        max_tokens=850,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["message"]["content"]

def print_chat():
    for message in chat:
        if message["role"] != "system":
            message_content = ""
            try:
                message_content = Text.from_markup(message["content"])
            except MarkupError:
                message_content = message["content"]
            print("\n", message_content)

while True:
    clear_screen()
    print(art)
    print_chat()
    action = input("\n> ")
    if action.lower() == "undo":
        if len(chat) > 2:  # Check to ensure we don't pop beyond chat length
            chat.pop()  # Remove assistant's last response
            chat.pop()  # Remove user's last message
    else:
        append_to_chat("user", "> " + action)
        assistant_response = get_chat_response()
        append_to_chat("assistant", assistant_response)