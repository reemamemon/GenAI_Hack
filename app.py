import streamlit as st
import whisper
import speech_recognition as sr
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play

# Load the Whisper model
model = whisper.load_model("base")

# Function to handle audio input (alternative method)
def record_audio():
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    if audio_file is not None:
        audio = AudioSegment.from_file(audio_file)
        play(audio)  # Optional: play the uploaded audio
        st.write("Audio file uploaded and played successfully.")
        return audio
    else:
        st.write("Please upload an audio file.")
    return None

# Function to transcribe audio to text
def transcribe_audio(audio):
    temp_wav_path = "/tmp/temp_audio.wav"
    audio.export(temp_wav_path, format="wav")
    result = model.transcribe(temp_wav_path)
    st.write("Transcription completed successfully.")
    return result["text"]

# Function to generate feedback
def generate_feedback(text):
    feedback = "Your grammar was good, but you made some mistakes in vocabulary and pronunciation."
    st.write("Feedback generated successfully.")
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
    st.write(f"User input received: {user_input}")  # Debug statement
    
    if user_input:
        if "conversation practice" in user_input.lower():
            st.write("Great! Let's start with a conversation practice session.")
            st.write("You can talk about any topic you want, and then I'll guide you through it, giving feedback along the way.")
            audio = record_audio()
            if audio is not None:
                text = transcribe_audio(audio)
                st.write(f"You said: {text}")
                feedback = generate_feedback(text)
                st.write(f"Feedback: {feedback}")
            else:
                st.write("No audio file was uploaded.")
        else:
            st.write("Please type 'conversation practice' to start.")

# Directly calling the main function
main()
