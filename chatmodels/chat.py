
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)

response = model.invoke("give me a paragraph of machine learning")

print(response.content)
