from flask import jsonify
import speech_recognition

import pyaudio
import wave
import keyboard


class VoiceProcessing:
    @staticmethod
    def record_voice():
        recognizer = speech_recognition.Recognizer()
        frames = []
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        try:
            while True:
                data = stream.read(1024)
                frames.append(data)
                if keyboard.is_pressed('q'):
                    break
        except KeyboardInterrupt:
            pass
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Enregistrer l'audio
        with wave.open('./myrecording.wav', 'wb') as sfile:
            sfile.setnchannels(1)
            sfile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            sfile.setframerate(44100)
            sfile.writeframes(b''.join(frames))

        # Reconnaissance vocale
        try:
            with speech_recognition.AudioFile('./myrecording.wav') as source:
                audio_data = recognizer.listen(source)
                text = recognizer.recognize_google(audio_data)
        except Exception as e:
            text = f"Exception: {str(e)}"
        return jsonify({'data': text})
