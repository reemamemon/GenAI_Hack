import streamlit as st
import whisper
import speech_recognition as sr

# Load the Whisper model
model = whisper.load_model("base")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to record audio
def record_audio():
    with sr.Microphone() as source:
        st.write("Recording... Please speak into the microphone.")
        audio = recognizer.listen(source)
        st.write("Recording finished.")
    return audio

# Function to transcribe audio to text
def transcribe_audio(audio):
    # Convert speech to text using Whisper model
    text = recognizer.recognize_google(audio)
    return text

# Function to generate feedback (This can be a simple function for now)
def generate_feedback(text):
    # Placeholder for feedback generation
    feedback = "Your grammar was good, but you made some mistakes in vocabulary and pronunciation."
    return feedback

# Main app
def main():
    st.title("English Speaking Practice Bot")
    
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = False
    
    if not st.session_state.conversation_started:
        st.session_state.conversation_started = True
        st.write("Welcome to the English Speaking Practice Bot!")
    
    user_input = st.text_input("Type here to start the conversation: ", "")
    
    if user_input:
        if "conversation practice" in user_input.lower():
            st.write("Great! Let's start with a conversation practice session.")
            st.write("You can talk about any topic you want, and then I'll guide you through it, giving feedback along the way.")
            if st.button("Start Recording"):
                audio = record_audio()
                text = transcribe_audio(audio)
                st.write(f"You said: {text}")
                feedback = generate_feedback(text)
                st.write(f"Feedback: {feedback}")
        
if _name_ == "_main_":
    main()
