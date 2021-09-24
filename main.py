#our main file

import speech_recognition as sr

# cria um reconhecedor
r = sr.Recognizer()

# abrir o microfone para captura
with sr.Microphone() as source:
   while True:
      audio= r.listen(source) # define microfonee como fonte de audio
   

   print(r.recognize_google(audio, language='pt'))

