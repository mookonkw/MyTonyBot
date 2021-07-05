import pyttsx3
import speech_recognition as sr


def listen():
    mic = sr.Microphone()
    rec = sr.Recognizer()
    with mic as source:
        print('listening...')
        audio = rec.listen(source)
        try:
            word = rec.recognize_google(audio)
            #talk(f'did you say {word}')
            return word
        except sr.UnknownValueError:
            talk('i did not hear that')
            return listen()


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
