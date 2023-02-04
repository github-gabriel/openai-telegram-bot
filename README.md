# OpenAI Telegram Bot
Dieses Projekt ist ein Telegram-Bot, der mithilfe von OpenAI-Modellen verschiedene Funktionen bereitstellt.

Die Funktionen des Bots sind über spezielle Befehle verfügbar und umfassen:

- das Senden von Bildern, die mit einer Beschreibung generiert wurden
- das Übersetzen von Bildern in eine bestimmte Sprache
- einfache Nachrichtenbeantwortung mithilfe des ChatGPT-Modells

Der Code enthält auch Funktionen zum Behandeln von Fehlern und zum Herunterladen von Bildern. Die verschiedenen Funktionen werden von Handlern aufgerufen, wenn Benutzereingaben empfangen werden.

## ChatGPT

Beim Programmieren hat mir [ChatGPT](https://chat.openai.com/chat) regelmäßig geholfen. Es ist ein schnelles und einfaches Tool um z.B. Codebeispiele zu bekommen ohne sich durch einen Haufen Dokumentation zu wühlen. Daher bin ich einfach begeistert von ChatGPT. Ich bin sogar so begeistert, dass die obige Beschreibung des Projektes komplett von ChatGPT geschrieben wurde.

## Requirements

- Python 3.10 oder höher
- Das [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) Modul
- Das [Pytesseract](https://github.com/madmaze/pytesseract) Modul
- Das [Pillow](https://github.com/python-pillow/Pillow) Modul 
- Das [OpenAI](https://github.com/openai/openai-python) Modul

Alle Requirements findest du in der [```requirements.txt```](https://github.com/github-gabriel/openai-telegram-bot/blob/main/requirements.txt)

Installiere alle Requirements mit ```pip install -r requirements.txt```

***Notiz: Es könnte sein, dass du noch weitere Sachen benötigst, wie einen API Key für OpenAI und den Telegram Bot. Lies dir dafür am besten die Documentations der einzelnen Module und deren Requirements durch!***

## Befehle

### AI Befehle

| Befehl     | Parameter              | Funktion                                                                                                                    |
|------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| /start     | Keine                  | Sendet eine Willkommensnachricht an den Benutzer                                                                            |
| /help      | Keine                  | Sendet eine Liste der verfügbaren Befehle an den Benutzer                                                                   |
| /image     | Eine Bildbeschreibung  | Generiert ein Bild mit Hilfe des DALL·E-Modells, das auf der von dem Benutzer angegebenen Beschreibung basiert              |
| /translate | Eine Sprache, ein Bild | Versucht, ein von dem Benutzer gesendetes Bild in eine bestimmte Sprache zu übersetzen, indem es das GPT-3-Modell verwendet |

***Einfache Nachrichten (keine Befehle) werden von GPT-3 beantwortet, sodass der Bot wie ein Chatbot verwendet werden kann***

### Cache Befehle (💤)

| Befehl                 | Parameter           | Funktion                                                                        |
|------------------------|---------------------|---------------------------------------------------------------------------------|
| /cache_time            | Zeit in Min.        | Setzt die Zeit nach der der Cache gelöscht wird                                 |
| /cache_size            | Anzahl der Elemente | Setzt die maximale Größe des Caches fest                                        |
| /cache_delete_elements | Anzahl der Elemente | Anzahl der Elemente die nach überschreiten der max. Cache Größe gelöscht werden |
| /clear_cache           | Keine               | Löscht den gesamten Cache                                                       |

## Updates

- ### Selbstlöschender Cache
  Der Cache löscht alte Elemente jetzt automatisch. So fängt er jetzt keine Gespräche über Sachen an, die schon mehrere     Stunden her sind. Hier ein Beispiel wie der 
  selbstläschende Cache in Aktion aussieht:
  
  <img src="https://user-images.githubusercontent.com/92476790/210180081-1a721d56-003b-4171-9ca1-28241d6dff0e.jpg" width="420" height="400" />
  
  ***Zu Testzwecken war die Zeit zum Löschen nur auf 60sek eingestellt***
  
 - ### Cache Einstellungen
   Die Einstellungen des Caches lassen sich jetzt auch über Befehle einstellen 
   
   <img src="https://user-images.githubusercontent.com/92476790/211151774-13c2048b-72f4-4199-b15a-564b7c3567db.jpg" width="280" height="450" />
   
   <img src="https://user-images.githubusercontent.com/92476790/211151794-3874f754-725f-4699-a7df-d35f652953ab.jpeg" width="280" height="450" />
  
   
## Einsatz

Um den Telegram Bot zu nutzen muss das Script einfach nur gestartet werden. Ich nutze dafür z.B. meinen Raspberry Pi 4 4GB. Als OS läuft Ubuntu Server 22.04 dort und um ihn auch sonst noch nutzen zu können nutze ich [Linux Screen](https://linuxize.com/post/how-to-use-linux-screen/), auf dem ich das Script dann ausgeführt habe.

Hier sind einige Videos zur Demonstration der einzelnen Befehle:

### Start, Help und Chatting

https://user-images.githubusercontent.com/92476790/210168963-77095455-36fc-4f70-bef1-678dd3ac201c.mp4

### Image

https://user-images.githubusercontent.com/92476790/210168980-e06e9336-6559-4c2d-bb3c-923aa7cd4fd9.mp4

### Translate

https://user-images.githubusercontent.com/92476790/210168989-417e0ff5-7761-4817-9108-5b15c0fa9bb1.mp4





