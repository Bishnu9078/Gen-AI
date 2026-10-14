
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(
    page_title="King AI - Mood Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Dark UI styling
st.markdown("""
<style>
.stApp {
    background: #0e1117;
    color: #f5f5f5;
}
.block-container {
    max-width: 850px;
    padding-top: 3rem;
}
h1 {
    font-size: 2.5rem !important;
}
div[role="radiogroup"] {
    gap: 22px;
}
div[data-testid="stChatMessage"] {
    background: #1c2029;
    border-radius: 12px;
    padding: 14px;
    border: 1px solid #30343d;
}
.stButton button {
    border-radius: 9px;
    min-height: 42px;
}
</style>
""", unsafe_allow_html=True)

# AI personalities
modes = {
    "😂 Funny": "You are a funny AI agent.",
    "🧠 Serious": "You are a serious AI agent. Be clear and professional.",
    "😏 Sarcastic": "You are a sarcastic AI agent. Use clever, playful sarcasm.",
    "🚀 Motivational": "You are a motivational AI agent. Be positive and encouraging."
}

@st.cache_resource
def get_model():
    return init_chat_model(
        "openai/gpt-oss-20b",
        model_provider="groq"
    )

model = get_model()

# Initialize session state
if "mode" not in st.session_state:
    st.session_state.mode = "😂 Funny"

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=modes[st.session_state.mode])
    ]

# Header
st.title("🤖 Mood Based AI Chatbot")
st.caption("Choose your AI personality and start chatting")

# Radio options
selected_mode = st.radio(
    "Choose your AI Mode:",
    options=list(modes.keys()),
    horizontal=True,
    key="mode"
)

# Reset conversation if personality changes
if st.session_state.messages[0].content != modes[selected_mode]:
    st.session_state.messages = [
        SystemMessage(content=modes[selected_mode])
    ]

st.divider()

# Reset chat button
if st.button("🔄 Reset Chat"):
    st.session_state.messages = [
        SystemMessage(content=modes[selected_mode])
    ]
    st.rerun()

# Display chat history
for message in st.session_state.messages[1:]:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# Chat input
prompt = st.chat_input("Say something...")

if prompt:
    if prompt.strip() == "0":
        st.session_state.messages = [
            SystemMessage(content=modes[selected_mode])
        ]
        st.rerun()

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.invoke(st.session_state.messages)
                st.markdown(response.content)
                st.session_state.messages.append(
                    AIMessage(content=response.content)
                )
            except Exception as error:
                st.error(f"Something went wrong: {error}")
