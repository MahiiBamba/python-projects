import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time
import os

class VoiceAssistant:
    def __init__(self, name="Assistant"):
        self.name = name
        
        # Initialize the speech recognition
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        # Set speaking rate
        self.engine.setProperty('rate', 180)
        # Set volume
        self.engine.setProperty('volume', 1.0)
        
        print(f"{self.name} is starting up...")
        self.speak(f"Hello, I am {self.name}, your voice assistant. How can I help you today?")
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice input and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                print("Processing...")
                
                # Use Google's speech recognition
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
                
            except sr.WaitTimeoutError:
                return "timeout"
            except sr.UnknownValueError:
                return "error"
            except sr.RequestError:
                return "network_error"
            except Exception as e:
                print(f"Error: {e}")
                return "error"
    
    def process_command(self, command):
        """Process the voice command"""
        # Handle errors or no input
        if command == "error":
            self.speak("I didn't catch that. Could you please repeat?")
            return
        elif command == "timeout":
            self.speak("I didn't hear anything. Please try again.")
            return
        elif command == "network_error":
            self.speak("I'm having trouble connecting to the internet. Please check your connection.")
            return
        
        # Process commands
        if "hello" in command or "hi" in command:
            self.speak(f"Hello! How can I help you?")
            
        elif "your name" in command:
            self.speak(f"My name is {self.name}.")
            
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}")
            
        elif "search" in command or "google" in command:
            search_terms = command.replace("search", "").replace("google", "").strip()
            if search_terms:
                self.speak(f"Searching Google for {search_terms}")
                webbrowser.open(f"https://www.google.com/search?q={search_terms}")
            else:
                self.speak("What would you like to search for?")
                
        elif "weather" in command:
            self.speak("To get weather information, I need to be connected to a weather API. This feature will be available in the next version.")
            
        elif "joke" in command:
            self.speak("Why don't scientists trust atoms? Because they make up everything!")
            
        elif "exit" in command or "quit" in command or "goodbye" in command or "bye" in command:
            self.speak("Goodbye! Have a great day!")
            return False
            
        else:
            self.speak("I'm not sure how to help with that yet. I'm still learning!")
        
        return True

def main():
    # Create the voice assistant
    assistant = VoiceAssistant("Jarvis")
    
    running = True
    while running:
        command = assistant.listen()
        running = assistant.process_command(command)
        time.sleep(0.5)  # Slight pause between commands
    
    print("Voice assistant has been shut down.")

if __name__ == "__main__":
    main()