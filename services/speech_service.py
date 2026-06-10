import speech_recognition as sr

def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)

    except:
        return ""
