### Eh week 1
in dit labo heb ik de slides doorgenomen en de verschillende python files aangemaakt. 
Als extratje in netcat heb ik logging toegevoegd aan het -c argument. Ook heb ik een keyboardlogger toegevoegd die teruggeeft wat de gebruiker intypt als die op enter drukt.
## werking
start netcat.py op met -l zet de default waarden in argerparse naar je eigen ip dan hoef je die niet elke keer mee te geven, anders -t erbij doen met je ip. standaard staat het op poort 5555 -p gebruiken om dit aan te passen.
```
python netcat.py -t <jouw ip> -p 7777 -l
```
geef het -kb om de keyboardlogger te gebruiken. 
```
python netcat.py  -l -kb
```