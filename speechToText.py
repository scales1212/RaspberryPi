import speech_recognition as sr

class speechToText():

    def listen(self):
        rec = sr.Recognizer()
        rec.pause_threshold = 0.5
        rec.energy_threshold = 800
        with sr.Microphone() as source:
            print("Speak anything : ")
            audio = rec.listen(source)
            print("finish")
            try:
                text = rec.recognize_google(audio)
                return text
            except:
                return

    def check_command(self, text):
        commands = ["rock", "NPR", "npr", "stop", "Best", "best", "off"]
        print(text)
        if text is None:
            return
        for str in commands:
            if str in text:
                print(str)
                return str
        return

# t = speechToText()
# txt = t.listen()
# print(t.check_command(txt))