import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	print ("hello")
	print(ch)
	print ("hii")
audio = r.listen(source)
ch = r.recognize_google(audio)