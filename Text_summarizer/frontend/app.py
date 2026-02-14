import streamlit as st
import requests


st.title("AI article Summarizer")
article = st.text_area("Paste Your article here", height = 300)

if st.button ("generate Summary "):
    if article:
        response = requests.post(
            "http://127.0.0.1:8000/summarize",
            json={"text": article}
        )
        summary = response.json()["summary"]
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text.")