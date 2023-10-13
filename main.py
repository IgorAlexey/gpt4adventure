from rich import print
from rich.text import Text
from rich.errors import MarkupError
from dotenv import load_dotenv
import os
import sys
import openai

load_dotenv()


def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


file = open("system.txt", "r")
system_prompt = file.read()
file.close()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "assistant",
        "content": "Welcome to [bold cyan]Adventure[/] - The genesis of your story awaits...\n\n[bold]Disclaimer[/]: The pen is mightier than the sword, every word you inscribe may brand your path with [b red]irreversible marks[/]. May the wisdom of the ancients guide your choices.\n\nIn your words, proffer the beginning you wish for your fable",
    },
]


def append_to_chat(role, content):
    chat.append({"role": role, "content": content})


def get_chat_response():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat,
        temperature=1.05,
        max_tokens=853,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["message"]["content"]


def print_chat():
    for message in chat:
        if message["role"] != "system":
            try:
                message_content = Text.from_markup(message["content"])
            except MarkupError:
                message_content = message["content"]

            print("\n", message_content)


while True:
    clear_screen()
    print_chat()
    action = input("\n> ")
    append_to_chat("user", "> " + action)
    assistant_response = get_chat_response()
    append_to_chat("assistant", assistant_response)
