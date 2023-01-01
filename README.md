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
- Das [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) Modul (```pip install python-telegram-bot```)
- Das [Pytesseract](https://github.com/madmaze/pytesseract) Modul (```pip install pytesseract```)
- Das [Pillow](https://github.com/python-pillow/Pillow) Modul (```python3 -m pip install --upgrade Pillow```)
- Das [OpenAI](https://github.com/openai/openai-python) Modul (```pip install --upgrade openai```)

Alle Requirements findest du in der [```requirements.txt```](https://github.com/github-gabriel/openai-telegram-bot/blob/main/requirements.txt)

***Notiz: Es könnte sein, dass du noch weitere Sachen benötigst, wie einen API Key für OpenAI und den Telegram Bot. Lies dir dafür am besten die Documentations der einzelnen Module und deren Requirements durch!***

## Befehle

| Befehl     | Parameter              | Funktion                                                                                                                    |
|------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| /start     | Keine                  | Sendet eine Willkommensnachricht an den Benutzer                                                                            |
| /help      | Keine                  | Sendet eine Liste der verfügbaren Befehle an den Benutzer                                                                   |
| /image     | Eine Bildbeschreibung  | Generiert ein Bild mit Hilfe des DALL·E-Modells, das auf der von dem Benutzer angegebenen Beschreibung basiert              |
| /translate | Eine Sprache, ein Bild | Versucht, ein von dem Benutzer gesendetes Bild in eine bestimmte Sprache zu übersetzen, indem es das GPT-3-Modell verwendet |

***Einfache Nachrichten (keine Befehle) werden von GPT-3 beantwortet, sodass der Bot wie ein Chatbot verwendet werden kann***
