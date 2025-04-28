import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile
import os
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

class VoiceInterface:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
    
    def record_audio(self, duration=10, sample_rate=44100):
        """Record audio from microphone"""
        print("Recording.....")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()
        print("Recording Finished!")

        # Save to temporary file
        temp_file = tempfile.mktemp(suffix='.wav')
        sf.write(temp_file, audio_data, sample_rate)
        return temp_file
    
    def speech_to_text(self, audio_file_path):
        """Convert speech to text using offline recognizer"""
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)  
                return text
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            return None
    
    def text_to_speech(self, text):
        """Convert text to speech (simplified version - in production use a TTS service)"""
        print(f"AI: {text}")