from libraries import wikipedia as wiki
import sys
import time

wiki.set_lang("it")

def control(query):
    try:
        return wiki.summary(query)
    except Exception:
        return "Perdonami, non so nulla riguardo a: "+query
    

while(True):
    sentence = input("Ciao, su cosa vuoi fare ricerche? (stop per terminare)\n")
    if((sentence == "stop") | (sentence == "STOP")):
        print("Arrivederci!!!")
        time.sleep(3)
        sys.exit(0)
    else:
        print(control(sentence))
        argument = wiki.page(sentence)
        print("\nLink utili: ")
        print(argument.url)
