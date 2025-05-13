# app.py
import streamlit as st
from transformers import pipeline

# Load summarization pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# UI
st.title("📝 Bullet Point Summarizer")
st.write("Paste any long text below, and get 3–5 bullet points summarizing the key ideas.")

text_input = st.text_area("Enter your text here:", height=300)

if st.button("Summarize"):
    if len(text_input.strip()) == 0:
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(text_input, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
            # Convert summary into bullet points (basic splitting)
            bullet_points = summary.split(". ")
            st.subheader("🔍 Summary:")
            for point in bullet_points:
                point = point.strip()
                if point:
                    st.write(f"- {point.strip('.')}")
