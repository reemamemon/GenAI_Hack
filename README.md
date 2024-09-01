# AI-Based English Speaking Practice Bot

The AI-Based English Speaking Practice Bot is designed to assist non-native English speakers in improving their language skills. The bot provides a user-friendly platform for practicing conversations, learning pronunciation, and expanding vocabulary, all with real-time feedback and support in Urdu.

## Live Demo

Check out the live demo of Project [here](https://huggingface.co/spaces/alidotdev/Speak_buddy).

## Key Features

**1. Conversation Practice:** 
 - Engage in voice-based conversations with the bot. 
 - Receive instant feedback on fluency, grammar, and pronunciation.

**2. Pronunciation Assistance:**
 - Input any word or sentence.
 - The bot accurately pronounces the input, helping users refine their speaking skills.

**3. Vocabulary Enhancement:**
 - Provide a word to the bot.
 - The bot returns synonyms and their meanings in Urdu, aiding vocabulary growth.

## Technologies Used

The following technologies are used in the code:

1. **Gradio**: For building the user interface with tabs for different functionalities like pronunciation help, conversation practice, and synonym finder.
   
2. **Groq**: For using the Groq API to interact with the language model.
   
3. **NumPy**: For numerical operations, particularly to handle audio data.
   
4. **OpenAI Whisper**: For speech-to-text conversion, helping transcribe audio input into text.
   
5. **gTTS (Google Text-to-Speech)**: For converting text input into speech and generating audio output.
   
6. **Librosa**: For loading and processing audio files, particularly for extracting audio data for analysis.
   
7. **NLTK (Natural Language Toolkit)**: For working with the WordNet lexical database to find synonyms.
   
8. **Deep-Translator**: For translating English synonyms into Urdu.

These libraries and tools enable the functionalities of speech-to-text, text-to-speech, chatbot interaction, and translation within the bot.

## Future Work

**1. RAG-Based Vocabulary:** Integrating reputable dictionaries like Oxford and  Cambridge into a Retrieval-Augmented 
 Generation (RAG) system will enhance vocabulary definitions, providing more accurate and comprehensive meanings.

**2. Multilingual Support:** Expanding vocabulary features to support meanings in multiple languages beyond Urdu will make SpeakBuddy more accessible to a diverse user base.

**3. Interactive Learning Modules:** Introducing interactive modules such as quizzes, challenges, and interactive scenarios will make learning more engaging and effective, promoting active participation.

**4. Mobile Integration:** Developing a mobile app version will enhance accessibility, allowing learners to access SpeakBuddy anytime and anywhere, fostering continuous learning.

## Installation

To install , follow these steps:

1. Clone the repository:

```
git clone [https://github.com/reemamemon/SpeakBuddy.git](https://github.com/reemamemon/SpeakBuddy)
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

## Usage
Once the application is running, you can access the bot via your web browser. Use the interface to start conversations, practice pronunciation, and enhance your vocabulary with the provided features.

## Contributors


## License
This project is licensed under the MIT License. See the LICENSE file for details.



