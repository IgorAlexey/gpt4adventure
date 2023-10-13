from rich import print
from rich.text import Text
import os
import openai

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
        "content": "Welcome to [bold cyan]Adventure[/]. The genesis of your story awaits your input.\n\n[bold]Be warned[/]: [u]The pen is mightier than the sword[/]. Every word you inscribe may brand your path with [bold red]irreversible marks[/].\n\nMay the wisdom of the ancients guide your choices.\n\nIn your words, proffer the beginning you wish for your fable",
    },
]


def print_messages():
    for message in chat:
        if message["role"] != "system":
            print(Text.from_markup(message["content"]))


while True:
    os.system("clear")
    print_messages()
    action = "> " + input("> ")
    chat.append({"role": "user", "content": action})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat,
        temperature=1.1,
        max_tokens=853,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    chat.append(
        {"role": "assistant", "content": response["choices"][0]["message"]["content"]}
    )
