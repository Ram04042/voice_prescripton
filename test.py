import speech_recognition as sr

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something")
    audio=r3.listen(source)
    print("Time Over")

if 'symptoms' in r2.recognize_google(audio):
    r2=sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Symptoms")
        audio=r2.listen(source)
        print("Time Over")

    try:
        print("Symptoms: "+r2.recognize_google(audio))
    except:
        print("Didn't get you bro")

elif 'prescription' in r1.recognize_google(audio):

    with sr.Microphone() as source:
        print("Say Prescription")
        audio=r2.listen(source)
        print("Time Over")

    try:
        print("Prescription: "+r2.recognize_google(audio))
    except:
        print("Didn't get you bro")


