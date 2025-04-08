import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        try:
            # Increase timeout and phrase_time_limit for better capture
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=20)
            print("Audio captured.")
            command = recognizer.recognize_google(audio)
            print(f"Recognized command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return "Sorry, I didn’t catch that."
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "Speech service is unavailable."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "An error occurred while processing your request."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
