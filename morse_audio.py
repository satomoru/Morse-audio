import os, sys
os.system("pip install pydub && pip install ffmpeg")

from pydub import AudioSegment
from pydub.generators import Sine

	
morse_code_mapping = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def text_to_morse(text):
    morse_code = '-....'
    for char in text.upper():
        if char in morse_code_mapping:
            morse_code += morse_code_mapping[char] + ' '
    return morse_code.strip()


def generate_audio(morse_code):
    dot_duration = 100  
    dash_duration = 3 * dot_duration

    audio = AudioSegment.silent(duration=dot_duration)  

    for symbol in morse_code:
        if symbol == '.':
            audio += Sine(1000).to_audio_segment(duration=dot_duration)
        elif symbol == '-':
            audio += Sine(1000).to_audio_segment(duration=dash_duration)
        elif symbol == ' ':
            audio += AudioSegment.silent(duration=dot_duration)  
        elif symbol == '/':
            audio += AudioSegment.silent(duration=7 * dot_duration)  

    return audio
os.system("clear")

text = input("here paste your text: ")
morse_code = text_to_morse(text)

audio = generate_audio(morse_code)
print("developed by darknet_off1cial")
audio_name = input("file name and file format (.mp3, .wav, .ogg) : ")
audio.export(audio_name, format="wav")

print("succesed ✓ ")
