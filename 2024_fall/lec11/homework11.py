import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)  
        text = recognizer.recognize_google(audio, language=language)
        return text
    
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio."
    
    except sr.RequestError:
        return "Could not request results from Speech Recognition service."

    except FileNotFoundError:
        return "File not found. Please check the filename."
