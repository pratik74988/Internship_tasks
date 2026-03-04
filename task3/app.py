import streamlit as st
import speech_recognition as sr
import tempfile

st.title("Speech to Text Converter")
st.write("Upload an audio file and convert speech into text")

uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file is not None:
    
    # save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name

    recognizer = sr.Recognizer()

    with sr.AudioFile(temp_path) as source:
        st.info("Processing audio...")
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success("Transcription:")
        st.write(text)

    except sr.UnknownValueError:
        st.error("Could not understand audio")

    except sr.RequestError:
        st.error("API unavailable")