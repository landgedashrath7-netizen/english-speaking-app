import streamlit as st
import sqlite3
from gtts import gTTS

# ---------- Page Config ----------
st.set_page_config(page_title="English Learning App", page_icon="📘")

# ---------- UI Style ----------
st.markdown("""
<style>
.stApp {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)

# ---------- Database ----------
conn = sqlite3.connect("app.db", check_same_thread=False)
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS progress (username TEXT, day TEXT)")
conn.commit()

# ---------- Data ----------
days_data = {
    "Day 1": {
        "sentences": ["I wake up early.", "I study English daily.", "I practice speaking."],
        "words": {"Wake": "उठणे", "Study": "अभ्यास", "Practice": "सराव"}
    },
    "Day 2": {
        "sentences": ["I go to work.", "I learn new things.", "I improve daily."],
        "words": {"Work": "काम", "Learn": "शिकणे", "Improve": "सुधारणा"}
    }
}

# ---------- Functions ----------
def speak(text):
    tts = gTTS(text)
    tts.save("voice.mp3")
    audio_file = open("voice.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

def register_user(username, password):
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def save_progress(username, day):
    c.execute("INSERT INTO progress VALUES (?, ?)", (username, day))
    conn.commit()

def get_progress(username):
    c.execute("SELECT * FROM progress WHERE username=?", (username,))
    return c.fetchall()

# ---------- Sidebar ----------
menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

# ---------- Register ----------
if menu == "Register":
    st.title("📝 Register")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Register"):
        register_user(user, pwd)
        st.success("Account Created ✅")

# ---------- Login ----------
elif menu == "Login":
    st.title("🔐 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        result = login_user(user, pwd)

        if result:
            st.success(f"Welcome {user} 🎉")

            page = st.sidebar.radio("Go to", ["Home", "Practice", "Progress"])

            if page == "Home":
                st.title("📘 English Learning App")
                st.write("Improve your English daily 🚀")

            if page == "Practice":
                day = st.selectbox("Select Day", list(days_data.keys()))

                st.subheader("📌 Sentences")
                for s in days_data[day]["sentences"]:
                    st.write("👉", s)

                    if st.button(f"🔊 Play {s}"):
                        speak(s)

                st.subheader("📖 Word Meaning")
                for w, m in days_data[day]["words"].items():
                    st.write(f"{w} = {m}")

                if st.button("Mark Complete"):
                    save_progress(user, day)
                    st.success("Saved ✅")

            if page == "Progress":
                data = get_progress(user)
                st.subheader("📊 Progress")
                st.write(f"Completed {len(data)} days ✅")

        else:
            st.error("Invalid Login ❌")