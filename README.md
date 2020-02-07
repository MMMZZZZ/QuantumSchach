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

## Einstellungen
Einstellungen können zu Beginn der `QuantumSchach.py` Datei festgelegt werden.
* `fieldSizeX`, `fieldSizeY`: Anzahl an Zeichen in Breite und Höhe, die verwendet werden, um ein Feld des Schachbretts darzustellen. So können die Felder immer (annähernd) quadratisch und in beliebiger Größe dargestellt werden. Beispiel: Die Zeichen in der Konsole sind 10x20 Pixel groß. Dann wird durch eine Feldgröße von 4x2 Zeichen das resultierende Feld in der Konsole mit 40x40 Pixeln quadratisch sein. Soll es größer sein, kann z.B. 6x3 angegeben werden. 
* `fieldEmpty`: Figuren werden mit Buchstaben dargestellt. Die restlichen Felder mit diesem Zeichen. Üblicherweise ein einzelnes Leerzeichen. Am besten so lassen ;) 
* `previewMarker`: Keinen sichtbaren Einfluss a.k.a. warum willst du daran herumspielen? Muss in jedem Fall eindeutig sein. 
* `previewBackColors`: Die Farben, mit denen Vorschaufelder eingefärbt werden. Normalerweise `Back.YELLOW` und `Back.LIGHTYELLOW_EX`. Sollte jeweils nur eine Farbe sein und nur den Hintergrund (`Back.*`) betreffen. Achtung: manche Farben führen zu Fehlern - liegt nicht an mir.
* `normalBackColors`: Farbe des normalen Spielfeldes. Erst die für dunkle Felder, dann die für helle. Normalerweise `Back.BLACK` und `Back.WHITE` Sollte jeweils nur eine Farbe sein und nur den Hintergrund (`Back.*`) betreffen. Achtung: manche Farben führen zu Fehlern - liegt nicht an mir.
* `(black|white)PlayerColor`: Textfarbe der Figuren beider Spieler. Normalerweise `Fore.LIGHTWHITE_EX` und `Fore.LIGHTWHITE_EX`. Sollte jeweils nur eine Farbe sein und nur die Textfarbe (`Fore.*`) betreffen. Achtung: manche Farben führen zu Fehlern - liegt nicht an mir.

## Fehlende/kommende Funktionen
* Abwechselndes Spielen erzwingen
* Bauer => Dame
* Sperren von Zügen, die ein Schach nicht beheben.
* Analyse der aktuellen Position
