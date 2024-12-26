from main import kolored
import os
STARTMESSAGE = True
if os.name == 'nt':
    if STARTMESSAGE:
        print("You are using Windows, ANSI codes may not work properly unless you use Windows Terminal or etc.")
else:
    if STARTMESSAGE:
        print(kolored("Klor working", color="white", background="green", bold=True))
