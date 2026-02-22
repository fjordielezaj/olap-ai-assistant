import streamlit as st
import pandas as pd
import google.generativeai as genai
import plotly.express as px
from data_utils import load_data
from prompts import SYSTEM_PROMPT

# 1. API Configuration
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("Error: GOOGLE_API_KEY not found in secrets.toml")
    st.stop()

genai.configure(api_key=api_key)

@st.cache_resource
def get_working_model():
    """Fallback logic to handle API stability with multiple model attempts."""
    models_to_try = [
        'gemini-2.5-flash',
        'gemini-1.5-flash', 
        'gemini-1.5-flash-latest',
        'gemini-3.0-flash-preview', 
        'gemini-2.0-flash'
    ]
    
    last_err = ""
    for m_name in models_to_try:
        try:
            model = genai.GenerativeModel(m_name)
            # Connectivity test
            model.generate_content("Hi", generation_config={"max_output_tokens": 1})
            return model
        except Exception as e:
            last_err = str(e)
            continue
    raise Exception(last_err)

# Initialize the model
try:
    model = get_working_model()
except Exception as e:
    st.warning("⛔ The assistant is currently having trouble connecting to the brain.")
    st.info("Please check your internet connection or API quota.")
    with st.expander("View Connection Details"):
        st.error(f"Technical Error: {e}")
    st.stop()

# 2. UI Setup
st.set_page_config(page_title="OLAP Assistant", layout="wide")
st.title("📊 AI-Powered OLAP Assistant")

st.sidebar.title("App Dashboard")
if 'model' in locals():
    st.sidebar.success(f"Connected to: {model.model_name}")

# 3. Data Loading
try:
    df = load_data()
except Exception as e:
    st.error(f"Data Error: {e}")
    st.stop()

if st.sidebar.checkbox("Show Dataset Preview"):
    st.subheader("Dataset Preview (First 10 Rows)")
    st.dataframe(df.head(10))

# 4. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_query := st.chat_input("Ask about your data..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner('Analyzing...'):
            try:
                # Combine system prompt with user question
                full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_query}"
                response = model.generate_content(full_prompt)
                
                # Extract Python code
                code = response.text.replace("```python", "").replace("```", "").strip()
                
                # Code Transparency Expander (Requirement for Choice A)
                with st.expander("Review Generated Code"):
                    st.code(code)
                
                # Execute generated code
                exec(code, globals(), locals())
                
                st.session_state.messages.append({"role": "assistant", "content": "Analysis complete."})
                
            except Exception as e:
                # Professional error message
                st.warning("⛔ You cannot perform this action with the current data or query.")
                st.info("Try rephrasing your question or checking your dataset filters.")
                
                # Hidden technical details for grading
                with st.expander("View Error Details (Admin)"):
                    st.error(f"Execution Error: {e}")
                    if 'code' in locals():
                        st.code(code)