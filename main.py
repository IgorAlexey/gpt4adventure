from rich import print
from rich.text import Text
from dotenv import load_dotenv
import os
import openai

load_dotenv()

system_txt = open("system.txt", "r")
system_prompt = system_txt.read()
system_txt.close()

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


def print_messages():
    for message in chat:
        try:
            message_content = Text.from_markup(message["content"])
        except MarkupError:
            message_content = message["content"]

        if message["role"] != "system":
            print("\n" + message_content)


while True:
    os.system("clear")
    print_messages()
    action = "> " + input("\n> ")
    chat.append({"role": "user", "content": action})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat,
        temperature=1.05,
        max_tokens=853,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    chat.append(
        {"role": "assistant", "content": response["choices"][0]["message"]["content"]}
    )
