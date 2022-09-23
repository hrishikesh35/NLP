from langdetect import detect
import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(input):
        engine.say(input)
        engine.runAndWait()

def run(val):
    var = detect(val)
    if 'en' in var:
        print("The input language is English")
        engine_talk("The input language is English")
    elif 'hi' in var:
        print("The input language is Hindi")
        engine_talk("The input language is Hindi")
    elif 'af' in var:
        print("The input language is Afrikaans")
        engine_talk("The input language is Afrikaans")
    elif 'ar' in var:
        print("The input language is Arabic")
        engine_talk("The input language is Arabic")
    elif 'bg' in var:
        print("The input language is Bulgarian")
        engine_talk("The input language is Bulgarian")
    elif 'bn' in var:
        print("The input language is Bengali")
        engine_talk("The input language is Bengali")
    elif 'ca' in var:
        print("The input language is Catalan")
        engine_talk("The input language is Catalan")
    elif 'cs' in var:
        print("The input language is Czech")
        engine_talk("The input language is Czech")
    elif 'cy' in var:
        print("The input language is Welsh")
        engine_talk("The input language is Welsh")
    elif 'da' in var:
        print("The input language is Danish")
        engine_talk("The input language is Danish")
    elif 'de' in var:
        print("The input language is German")
        engine_talk("The input language is German")
    elif 'el' in var:
        print("The input language is Greek")
        engine_talk("The input language is Greek")
    elif 'es' in var:
        print("The input language is Spanish")
        engine_talk("The input language is Spanish")
    elif 'et' in var:
        print("The input language is Estonian")
        engine_talk("The input language is Estonian")
    elif 'fa' in var:
        print("The input language is Persian")
        engine_talk("The input language is Persian")
    elif 'fi' in var:
        print("The input language is Finnish")
        engine_talk("The input language is Finnish")
    elif 'fr' in var:
        print("The input language is French")
        engine_talk("The input language is French")
    elif 'gu' in var:
        print("The input language is Gujarati")
        engine_talk("The input language is Gujarati")
    elif 'he' in var:
        print("The input language is Hebrew")
        engine_talk("The input language is Hebrew")
    elif 'hr' in var:
        print("The input language is Croatian")
        engine_talk("The input language is Croatian")
    elif 'hu' in var:
        print("The input language is Hungarian")
        engine_talk("The input language is Hungarian")
    elif 'id' in var:
        print("The input language is Indonesian")
        engine_talk("The input language is Indonesian")
    elif 'it' in var:
        print("The input language is Italian")
        engine_talk("The input language is Italian")
    elif 'ja' in var:
        print("The input language is Japanese")
        engine_talk("The input language is Japanese")
    elif 'kn' in var:
        print("The input language is Kannada")
        engine_talk("The input language is Kannada")
    elif 'ko' in var:
        print("The input language is Korean")
        engine_talk("The input language is Korean")
    elif 'lt' in var:
        print("The input language is Lithuanian")
        engine_talk("The input language is Lithuanian")
    elif 'lv' in var:
        print("The input language is Latvian")
        engine_talk("The input language is Latvian")
    elif 'mk' in var:
        print("The input language is Macedonian")
        engine_talk("The input language is Macedonian")
    elif 'ml' in var:
        print("The input language is Malayalam")
        engine_talk("The input language is Malayalam")
    elif 'mr' in var:
        print("The input language is Marathi")
        engine_talk("The input language is Marathi")
    elif 'ne' in var:
        print("The input language is Nepali")
        engine_talk("The input language is Nepali")
    elif 'nl' in var:
        print("The input language is Dutch")
        engine_talk("The input language is Dutch")
    elif 'no' in var:
        print("The input language is Norwegian")
        engine_talk("The input language is Norwegian")
    elif 'pa' in var:
        print("The input language is Punjabi")
        engine_talk("The input language is Punjabi")
    elif 'pl' in var:
        print("The input language is Polish")
        engine_talk("The input language is Polish")
    elif 'pt' in var:
        print("The input language is Portuguese")
        engine_talk("The input language is Portuguese")
    elif 'ro' in var:
        print("The input language is Romanian")
        engine_talk("The input language is Romanian")
    elif 'ru' in var:
        print("The input language is Russian")
        engine_talk("The input language is Russian")
    elif 'sk' in var:
        print("The input language is Slovak")
        engine_talk("The input language is Slovak")
    elif 'sl' in var:
        print("The input language is Slovenian")
        engine_talk("The input language is Slovenian")
    elif 'so' in var:
        print("The input language is Somali")
        engine_talk("The input language is Somali")
    elif 'sq' in var:
        print("The input language is Albanian")
        engine_talk("The input language is Albanian")
    elif 'sv' in var:
        print("The input language is Swedish")
        engine_talk("The input language is Swedish")
    elif 'sw' in var:
        print("The input language is Swahili")
        engine_talk("The input language is Swahili")
    elif 'ta' in var:
        print("The input language is Tamil")
        engine_talk("The input language is Tamil")
    elif 'te' in var:
        print("The input language is Telugu")
        engine_talk("The input language is Telugu")
    elif 'th' in var:
        print("The input language is Thai")
        engine_talk("The input language is Thai")
    elif 'tr' in var:
        print("The input language is Turkish")
        engine_talk("The input language is Turkish")
    elif 'uk' in var:
        print("The input language is Ukrainian")
        engine_talk("The input language is Ukrainian")
    elif 'ur' in var:
        print("The input language is Urdu")
        engine_talk("The input language is Urdu")
    elif 'vi' in var:
        print("The input language is Vietnamese")
        engine_talk("The input language is Vietnamese")
    elif 'zh' in var:
        print("The input language is Chinese")
        engine_talk("The input language is Chinese")

# Enter input language
val = input()

run(val)

