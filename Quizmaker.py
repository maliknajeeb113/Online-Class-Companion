import speech_recognition as sr
def listToString(s):
    str1 = ""
    for ele in s:
        str1 +=" "+ ele
    return str1
# Initialize the recognizer
r = sr.Recognizer()
while(1):
    with sr.Microphone() as source:
    # read the audio data from the default microphone
        r.adjust_for_ambient_noise(source,duration=1)
        audio_data = r.listen(source)
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
        break

lst=text.split()
print(lst)
original_ans=lst[-1]
#print(original_ans)
print("Question is:",listToString(lst[:-1]),len(original_ans)*"_ ")
answer=input("Enter your answer: ")
if (original_ans==answer):
    print("This is the correct answer")
else:
    print("Try again")
