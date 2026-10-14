
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

from langchain_core.messages import AIMessage, SystemMessage , HumanMessage

model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)

print("Choose your AI mode")
print("press 1 for funny mode")
print("press 2 for serious mode")
print("press 3 for sarcastic mode")
print("press 4 for motivational mode")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    mode = "You are a funny AI agent"
elif choice == '2':
    mode = "You are a serious AI agent"
elif choice == '3':
    mode = "You are a sarcastic AI agent"
elif choice == '4':
    mode = "You are a motivational AI agent"

messages = [ 
SystemMessage(content=mode)
]

print("-------------- welcome type 0 to exit --------------")

while True:
    prompt = input("You : ")

    messages.append(HumanMessage(content=prompt))

    if prompt == '0':
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot :", response.content)

print(messages)    
