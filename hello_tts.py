import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', 'gmw/en')
engine.save_to_file("Hello.", "hello.wav")
engine.runAndWait()
# feeling = input(">")
# engine.say("Yes. I am feeling " + feeling + " as well.")
# engine.runAndWait()
