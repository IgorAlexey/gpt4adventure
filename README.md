# gpt4adventure

Ressurecting text-adventure games with GPT4 and coloring the output.

## Instructions

1. Clone & install the requirements...
```shell
git clone https://github.com/Sororfortuna/gpt4adventure.git
cd gpt4adventure && pip install -r requirements.txt
```

2. Create a file named `.env` with your API key
```ini
OPENAI_API_KEY=sk-...
```

1. launch with `python main.py` in a reliable terminal.

### Ideas...

This is a very simple implementation of a text-adventure game. The app can be extended to use other tools like [stable-diffusion](https://stability.ai/stable-diffusion) in order to generate image of the scenarios for example, in which case, it could be better to have a custom terminal interface rather than converting the images to colored ASCII characters...

If you want to contribute, feel free to create PRs, Issues.
