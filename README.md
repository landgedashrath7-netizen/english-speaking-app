import streamlit as st
from gtts import gTTS

# 🌟 1. Page Configuration (Fun Title and Icon)
st.set_page_config(page_title="Machines & Health Adventure", page_icon="🧸")

# 🎈 2. App Title (Big and Clear for Kids)
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧸 Machines & Health Adventure</h1>", unsafe_allow_html=True)
st.write("---")

# 🛠️ Category 1: Machines (Cars, Robots, etc.)
st.markdown("<h2 style='color: #1F77B4;'>🚗 Let's Talk About Machines!</h2>", unsafe_allow_html=True)
st.write("Simple sentences for kids to learn about different machines.")

# List of simple sentences about machines
machine_sentences = [
    "I like cars.",
    "A car goes zoom zoom.",
    "The fan goes round and round.",
    "A train goes choo choo.",
    "I have a toy robot.",
    "The computer helps me play."
]

# Dropdown menu to select a sentence
machine_text = st.selectbox("Choose a machine sentence:", machine_sentences)

# Play button for machine sentences
if st.button("🔊 Hear Machine Sound"):
    tts = gTTS(text=machine_text, lang='en')
    tts.save("machine.mp3")
    st.audio("machine.mp3")

st.write("---")

# ❤️ Category 2: Health (Eating Healthy, Washing Hands, etc.)
st.markdown("<h2 style='color: #2CA02C;'>❤️ Let's Learn About Health!</h2>", unsafe_allow_html=True)
st.write("Simple sentences to help kids build healthy habits.")

# List of simple sentences about health
health_sentences = [
    "I wash my hands.",
    "I eat a red apple.",
    "I brush my teeth.",
    "Vegetables make me strong.",
    "I sleep every night.",
    "I drink water."
]

# Dropdown menu to select a sentence
health_text = st.selectbox("Choose a health sentence:", health_sentences)

# Play button for health sentences
if st.button("🔊 Hear Health Secret"):
    tts = gTTS(text=health_text, lang='en')
    tts.save("health.mp3")
    st.audio("health.mp3")

st.write("---")
st.success("Great job practicing! Listen and repeat!")
