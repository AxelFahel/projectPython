'''
Code projeto visto em vídeos na internet
Instalar:   pip install SpeechRecognition
            pip install pyttsx3


'''

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

def ouvir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {query}\n")

    except Exception as e:
        print("Repita, por favor...")
        return "None"

    return query

def falar(texto):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(texto)
    engine.runAndWait()
def executar():
    falar("Olá, eu sou a JARVIS do Homem de Ferro. Como posso ajudá-lo?")
    while True:
        query = ouvir().lower()

        if 'wikipedia' in query:
            falar('Pesquisando na Wikipedia...')
            query = query.replace("wikipedia", "")
            resultados = wikipedia.summary(query, sentences=2)
            falar("De acordo com a Wikipedia")
            print(resultados)
            falar(resultados)

        elif 'abrir youtube' in query:
            webbrowser.open("youtube.com")

        elif 'abrir google' in query:
            webbrowser.open("google.com")

        elif 'hora' in query:
            hora = datetime.datetime.now().strftime("%H:%M:%S")
            falar(f"A hora atual é {hora}")

        elif 'enviar email' in query:
            try:
                falar("O que você gostaria de dizer?")
                conteudo = ouvir()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('seuemail@gmail.com', 'sua-senha')
                server.sendmail('seuemail@gmail.com', 'destinatario@gmail.com', conteudo)
                server.close()
                falar("O email foi enviado com sucesso!")
            except Exception as e:
                print(e)
                falar("Não foi possível enviar o email.")

        elif 'tchau' in query:
            falar("Até logo!")
            break

if __name__ == "__main__":
    executar()
