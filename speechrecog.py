import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()
while(1):
    with sr.Microphone() as source:
    # read the audio data from the default microphone
        r.adjust_for_ambient_noise(source,duration=1)
        audio_data = r.listen(source)
        # convert speech to text
        text = r.recognize_google(audio_data)
        try:
            print(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
