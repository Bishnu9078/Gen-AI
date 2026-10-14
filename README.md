# Generative AI

This repository contains beginner-friendly Generative AI experiments built with
LangChain. It includes chat model examples, Hugging Face examples, embeddings,
a command-line mood chatbot, and a Streamlit mood-based AI chatbot.

## What Has Been Done So Far

- Set up a Python project for Generative AI practice.
- Added environment variable support with `python-dotenv`.
- Added `.env.example` so required API keys are documented safely.
- Added `.gitignore` so real secrets in `.env` and virtual environments are not pushed.
- Built simple LangChain chat examples using Groq-hosted models.
- Built a command-line mood chatbot in `chatmodels/chatbot.py`.
- Built a Streamlit web chatbot in `chatmodels/app.py`.
- Added four chatbot personalities:
  - Funny
  - Serious
  - Sarcastic
  - Motivational
- Added Hugging Face remote model and local pipeline examples.
- Added a Hugging Face embeddings example using `sentence-transformers/all-MiniLM-L6-v2`.
- Configured the GitHub remote as:

```bash
https://github.com/Bishnu9078/Gen-AI.git
```

## Project Structure

```text
.
├── chatmodels/
│   ├── app.py              # Streamlit mood-based chatbot
│   ├── chatbot.py          # Command-line mood chatbot
│   ├── chat.py             # Simple LangChain chat example
│   ├── huggingface.py      # Hugging Face endpoint example
│   └── localmodel.py       # Local Hugging Face pipeline example
├── embeddingmodels/
│   ├── embeddings.py       # Hugging Face embeddings example
│   └── higgingface_embedding.py
├── .env.example            # Example API key configuration
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## Requirements

- Python 3.13 or newer
- Groq API key for the main chat examples
- Hugging Face token for Hugging Face endpoint examples
- Optional OpenAI and Google API keys for future model experiments

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Bishnu9078/Gen-AI.git
cd Gen-AI
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:

```bash
copy .env.example .env
```

5. Add your API keys inside `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
HF_TOKEN=your_huggingface_token_here
```

## How To Run

Run the Streamlit chatbot:

```bash
streamlit run chatmodels/app.py
```

Run the command-line mood chatbot:

```bash
python chatmodels/chatbot.py
```

Run the simple chat model example:

```bash
python chatmodels/chat.py
```

Run the Hugging Face embedding example:

```bash
python embeddingmodels/embeddings.py
```

## GitHub Push Commands

Use these commands to add, commit, and push the latest work:

```bash
git add .
git commit -m "Add mood chatbot and project README"
git push origin main
```

## Notes

- Do not commit the real `.env` file because it contains private API keys.
- Use `.env.example` to show other users which keys they need.
- Some Hugging Face local model examples may need extra packages such as
  `transformers`, `sentence-transformers`, or `torch`.
