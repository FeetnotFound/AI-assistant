# This file is to test which model is the best for you 
# and your computer. Run "tts --list_models" to see all
# the models available in your langauge. You can run 
# all of them and grade them of how well it sounds and how 
# fast they are.

# Import the tts model and the playback model
from TTS.api import TTS as textToSpeech
from pygame import mixer
import os
import time
mixer.init()

model = "tts_models/en/ljspeech/vits"

# Define the speech model
tts = textToSpeech(model_name=model, progress_bar=False)


def generate_tts(sentence, speech_file_path):
    tts.tts_to_file(text=sentence, file_path=speech_file_path,
                    split_sentences=False)
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


TextTS("There is a rabbit hopping across the field. Nominal. Sir Functional")