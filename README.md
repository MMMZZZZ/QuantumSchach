# QuantumSchach
Spielereien rund um https://github.com/pippinbarr/chesses

Python3 Skript, interaktive Konsole
## Benötigte Pakete
[Colorama](https://pypi.org/project/colorama/)

## Befehle
Befehle können groß oder klein geschrieben werden. Eckige Klammern geben optionale Teile an. Runde Klammern zeigen welche Zeichen alle an dieser Stelle stehen können.
* `n[e[w]]`: Neues Spiel
* `(abcdefgh)(12345678)[(abcdefgh)(12345678)][p]`: Figur, die bewegt werden soll. Optional kann ein Ziel angegeben werden, dies wird allerdings nur beachtet, wenn der König bewegt werden soll und es mehrere Zugmöglichkeiten gibt. Das optionale `p` zeigt eine Vorschau aller möglichen Züge der gewählten Figur. 

Beispiel einer Eingabefolge:
* `new`: Neues Spiel
* `e2p`: Zeige Vorschau der möglichen Züge für die Figur auf E2. In diesem Fall ein noch nicht bewegter Bauer, daher werden E3 und E4 markiert.
* `e2`: Bewegt den Bauern auf E2 nach E3 und E4
* `e1`: Bewegt den König von E1 nach E2. Dies ist seine einzige Zugoption.
* `e2`: Der König auf E2 wird nicht bewegt, da er auf D3, E1 oder F3 ziehen kann (anzeigbar durch `e2p`). Es muss ein Ziel angegeben werden.
* `e2d3`: Der König auf E2 zieht nach D3. 

## Fehlende/kommende Funktionen
* Abwechselndes Spielen erzwingen
* Bauer => Dame
* Sperren von Zügen, die ein Schach nicht beheben.
* Analyse der aktuellen Position
