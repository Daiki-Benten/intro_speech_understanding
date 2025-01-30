import datetime, gtts, bs4, random, speech_recognition
from gtts import gTTS

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    try:
        tts = gTTS(text=f"The current time is {time_str}", lang=lang)
        tts.save(filename)
    except ValueError:
        print(f"Error: Language '{lang}' is not supported by gTTS.")
    

def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    lang (str) - language in which to speak
    audiofile (str) - filename in which to record the joke
    '''
    jokes = {
        "en": ["Why did the scarecrow win an award? Because he was outstanding in his field!",
                "Why don’t skeletons fight each other? They don’t have the guts."],
        "ja": ["なんでかっぱは川で泳ぐのが好きなの？それは水の中の方が快適だから！",
                "カレーが走ったら、どうなる？ スパイシー！"]
    }
    joke = random.choice(jokes.get(lang, ["Sorry, I don't have a joke in this language."]))
    try:
        tts = gTTS(text=joke, lang=lang)
        tts.save(audiofile)
    except ValueError:
        print(f"Error: Language '{lang}' is not supported by gTTS.")

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @Returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    today = datetime.date.today()
    date_str = today.strftime("Today is %A, %B %d, %Y")
    try:
        tts = gTTS(text=date_str, lang=lang)
        tts.save(audiofile)
    except ValueError:
        print(f"Error: Language '{lang}' is not supported by gTTS.")
    return f"https://www.timeanddate.com/calendar/?year={today.year}&month={today.month}"

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language in which to speak
    filename (str) - filename in which to store the result
    '''
    options = [what_time_is_it, tell_me_a_joke, what_day_is_it]
    choice = random.choice(options)
    if choice == what_day_is_it:
        url = choice(lang, filename)
        print(f"Check the calendar here: {url}")
    else:
        choice(lang, filename)


