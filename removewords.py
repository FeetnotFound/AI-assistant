sentence="I'm functioning within normal parameters, Sir. Ready to assist with any task or inquiry. #lights"

speech = sentence.split('#')[0]
speech = speech.replace(",", "", 1)


print(speech)
