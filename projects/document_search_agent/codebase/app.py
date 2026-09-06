import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Add src to path so Python can find your assistant
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from src.assistant import DocumentAssistant

st.set_page_config(page_title="Document Assistant", page_icon="📄", layout="centered")

# Hide Streamlit branding for a cleaner look
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

st.title("📄 AI Document Assistant")
st.markdown("Ask questions, extract summaries, and calculate amounts from your documents!")

with st.sidebar:
    st.header("💡 Sample Questions")
    st.markdown("""
    Try copying and pasting these to test the different features:
    
    **🔍 Q&A**
    > *What is the status of the claim filed by John Doe?*
    
    **📝 Summarization**
    > *Can you summarize the Acme Corporation document?*
    
    **🧮 Calculation**
    > *What is the total sum of the invoice for Acme Corporation and the invoice for TechStart Inc?*
    
    **🕵️ NLP Search**
    > *Find documents with amounts over $50,000*
    """)

# Initialize the assistant in the session state so it doesn't restart every time you type
if "assistant" not in st.session_state:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("Please set OPENAI_API_KEY in your .env file or Streamlit Secrets")
        st.stop()
    
    st.session_state.assistant = DocumentAssistant(
        openai_api_key=api_key,
        model_name="gpt-4o",
        temperature=0.1
    )
    st.session_state.assistant.start_session("streamlit_user")
    
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 **Hello!** I am your AI Document Assistant. How can I help you analyze your documents today?"}
    ]

# Display all previous chat messages
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Capture the user's input
if prompt := st.chat_input("Ask about your documents (e.g. 'Summarize all contracts')..."):
    
    # Show what the user typed
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Process and display the assistant's response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            result = st.session_state.assistant.process_message(prompt)
            
            if result["success"]:
                response_text = result.get("response", "No response generated.")
                st.markdown(response_text)
                
                # Show the AI's internal thoughts in a dropdown!
                with st.expander("👀 See how the AI answered this"):
                    st.write("**Detected Intent:**", result.get("intent", {}).get("intent_type"))
                    st.write("**Source Documents:**", ", ".join(result.get("active_documents", [])))
                    st.write("**Tools Used:**", ", ".join(result.get("tools_used", [])))
                    
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            else:
                st.error(f"Error: {result.get('error', 'Unknown error')}")
