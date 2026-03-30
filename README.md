# english-speaking-app

import streamlit as st
from gtts import gTTS
import speech_recognition as sr
import os

# १. पेज सेटअप
st.set_page_config(page_title="English Coach", layout="wide")

st.title("🗣️ English Speaking Practice")

# २. मुख्य भाग
col1, col2 = st.columns(2)

with col1:
    st.header("🎧 Listen")
    text_to_hear = st.text_input("Type a sentence:", "Hello, how are you?")
    if st.button("Play Audio"):
        tts = gTTS(text=text_to_hear, lang='en')
        tts.save("t.mp3")
        st.audio("t.mp3")

with col2:
    st.header("🎤 Speak")
    if st.button("Start Mic"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = r.listen(source)
        try:
            out = r.recognize_google(audio)
            st.success(f"You said: {out}")
        except:
            st.error("Mic error or voice not clear.")
