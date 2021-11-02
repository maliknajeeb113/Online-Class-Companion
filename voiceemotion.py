from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("clearing background noises......")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("voice...")
    recordedaudio=recognizer.listen(source)
    print("done recordng......")
try:
    print("printing maessage....")
    text=recognizer.recognize_google(recordedaudio)
except Exception as ex:
    print(ex)


sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
for i in sentence:
    v=analyser.polarity_scores(i)
    print(v)
