from RealtimeSTT import AudioToTextRecorder
import assist_local
import time
import torch
torch.cuda.empty_cache()
# import tools



if __name__ == '__main__':
    recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en", post_speech_silence_duration=1, silero_sensitivity=0.4)
    hot_words = ["buddy"]
    skip_hot_word_check = False
    print("\n Say something...")
    while True:
        current_text = recorder.text()
        print(current_text)
        if any(hot_word in current_text.lower() for hot_word in hot_words) or skip_hot_word_check:
                    #make sure there is text
                    if current_text:
                        print("User: " + current_text)
                        recorder.stop()
                        #get time
                        current_text = current_text + " Time:" + time.strftime("%Y-m-%d %H-%M-%S")
                        
                        response = assist_local.ask_question_memory(current_text)
                        
                        speech = response.split('#')[0]
                        speech = speech.replace(",", "", 1)
                        print(speech)
                        print("Hellos")
                        assist_local.TextTS(speech)
                        skip_hot_word_check = True if "?" in response else False
                        if len(response.split('#')) > 1:
                            command = response.split('#')[1]
                            # tools.parse_command(command)
                            print("Command: ", command)
                        
                        recorder.start()
