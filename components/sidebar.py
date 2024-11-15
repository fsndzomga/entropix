import streamlit as st
from components.faq import faq
from dotenv import load_dotenv

load_dotenv()


def sidebar():
    with st.sidebar:
        st.header("🔎 Entropix")
        st.subheader("AI-Powered Search Engine")
        st.markdown("LLMs can make mistakes. Check important info.")

        faq()
