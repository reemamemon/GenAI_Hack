import gradio as gr
from gtts import gTTS
import whisper
from groq import Groq
import numpy as np
import librosa
import nltk
from nltk.corpus import wordnet
from deep_translator import GoogleTranslator

# Ensure wordnet data is downloaded
nltk.download('wordnet')

# Set up Groq API client
client = Groq(api_key="enter you groq api key heres")

# Load Whisper model
model = whisper.load_model("base")

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en')
        audio_file_path = "output.mp3"
        tts.save(audio_file_path)
        return audio_file_path
    except Exception as e:
        return f"Error in TTS: {str(e)}"

def chatbot(audio):
    try:
        if audio is None:
            return "Error: No audio input provided."

        audio_data, sample_rate = librosa.load(audio, sr=16000)

        if not np.issubdtype(audio_data.dtype, np.floating):
            audio_data = audio_data.astype(np.float32)

        transcription = model.transcribe(audio_data)
        user_input = transcription["text"]

        messages = [
            {"role": "system", "content": "You are an English tutor. Your job is to provide detailed feedback on grammar and vocabulary."},
            {"role": "user", "content": f"Please review the following text and provide feedback on grammar and vocabulary: {user_input}"}
        ]

        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-groq-70b-8192-tool-use-preview",
        )
        response_text = chat_completion.choices[0].message.content

        return response_text
    except Exception as e:
        return f"Error in chatbot: {str(e)}"

def get_synonyms(word):
    try:
        synonyms = wordnet.synsets(word)
        english_synonyms = set()
        translator = GoogleTranslator(source='en', target='ur')

        for syn in synonyms:
            for lemma in syn.lemmas():
                english_synonyms.add(lemma.name())

        urdu_synonyms = [translator.translate(word) for word in english_synonyms]

        return f"English Synonyms: {', '.join(english_synonyms)}", f"Urdu Synonyms: {', '.join(urdu_synonyms)}"
    except Exception as e:
        return f"Error in synonym finder: {str(e)}", ""

def build_interface():
    with gr.Blocks() as demo:
        gr.Markdown(
            """
            <h1 style="text-align: center; color: #4CAF50;">AI Based English Speaking Practice Bot</h1>
            <h3 style="text-align: center;">Welcome To the SpeakBuddy! Choose Your English Practice Model Below And Start Learning.</h3>
            """
        )

        with gr.Tabs():
            with gr.TabItem("Pronounciation"):
                gr.Markdown(
                    """
                    <h2 style="text-align: center; color: #4CAF50;">Pronounciation Helper</h2>
                    """
                )
                text_input = gr.Textbox(label="Enter your text here", lines=3, placeholder="Type your text here...")
                convert_button = gr.Button("Check Pronounciation")
                audio_output = gr.Audio(label="Audio Output")

                convert_button.click(text_to_speech, inputs=text_input, outputs=audio_output)

            with gr.TabItem("Coversation Practice"):
                gr.Markdown(
                    """
                    <h2 style="text-align: center; color: #4CAF50;">Conversation Helper</h2>
                    """
                )
                audio_input = gr.Audio(type="filepath", label="Record Your Voice")
                chatbot_output_text = gr.Textbox(label="Feedback", lines=5)

                audio_input.change(chatbot, inputs=audio_input, outputs=chatbot_output_text)

            with gr.TabItem("Synonym Finder"):
                gr.Markdown(
                    """
                    <h2 style="text-align: center; color: #4CAF50;">Synonym Finder</h2>
                    """
                )
                word_input = gr.Textbox(label="Enter a word", lines=1, placeholder="Type a word here...")
                synonym_output_english = gr.Textbox(label="English Synonyms", lines=2)
                synonym_output_urdu = gr.Textbox(label="Meaning In Urdu", lines=2)

                word_input.change(get_synonyms, inputs=word_input, outputs=[synonym_output_english, synonym_output_urdu])

    return demo

if __name__ == "__main__":
    interface = build_interface()
    interface.launch()
