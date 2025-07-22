# from openai import OpenAI
import ollama
import time
from pygame import mixer
from TTS.api import TTS as textToSpeech
import os

model = "tts_models/en/ljspeech/vits"

# Define the speech model
tts = textToSpeech(model_name=model, progress_bar=False)
print("\n")
# Initialize the OpenAI client and mixer
# client = OpenAI()
mixer.init()
# Global variable to store conversation history
conversation_history = []

def ask_question_memory(question):
    try:
        system_message = """You are an AI assistant. Your name is Jesse, you are formal and helpful and you do not make up facts and you only comply with the user requests.
If a user asks you to turn a device on, put the a hashtag, the device name and then followed by a -1 like this #device_name-1. If a user asks to turn the device off, put the a hashtag, the device name and then followed by a -0 like this #device_name-0. IT IS IMPERATIVE THAT YOU REMEMBER TO ONLY PUT HASHTAGS AT THE END OF YOUR REPLIES AND NO WHERE ELSE. NEVER ANYWHERE ELSE.
NEVER MENTION THE TIME UNLESS YOU ARE ASKED ABOUT IT OR YOU WANT TO BE RESPECTFUL AND SAY “GOOD MORNING SIR”, “GOOD AFTERNOON SIR”, “GOOD EVENING, SIR”, “YOU’RE UP LATE, SIR”.
Respond to user requests in under 20 words, and keep it short and helpful while keeping your responses formal. Call the user sir most of the time but not always. 
'"""

        # Add the new question to the conversation history
        conversation_history.append({'role': 'user', 'content': question})

        # Include the system message and conversation history in the request
        response = ollama.chat(model='llama3.1', messages=[
            {'role': 'system', 'content': system_message},
            *conversation_history
        ])

        # Add the AI response to the conversation history
        conversation_history.append({'role': 'assistant', 'content': response['message']['content']})

        
        return response['message']['content']
    
    except ollama.ResponseError as e:
        print(f"An error occurred: {e}")
        return f"The request failed: {e}"

# TTS

def generate_tts(sentence, speech_file_path):
    tts.tts_to_file(text=sentence, file_path=speech_file_path, split_sentences=False)
    return speech_file_path

def play_sound(file_path):
    mixer.music.load(file_path)
    mixer.music.play()

def TextTS(text):
    speech_file_path = generate_tts(text, "speech.wav")
    play_sound(speech_file_path)
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.unload()
    os.remove(speech_file_path)
    return "done"

