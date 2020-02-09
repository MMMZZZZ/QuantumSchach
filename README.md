# QuantumSchach
Spielereien rund um https://github.com/pippinbarr/chesses

Python3 Skript, interaktive Konsole
## Voraussetzungen
Python >=3.8

[Colorama](https://pypi.org/project/colorama/)

## Neueste Features
* Spielerfolge ab jetzt erzwungen; weiß und schwarz müssen abwechselnd spielen
* Illegale Züge nicht mehr durchführbar und auch nicht mehr als Vorschlag möglich.
* Autoplay gegen den Computer
* Angepasstes Rating. Anzahl der Damen wird berücksichtigt. Der Wert "funktioniert", der höchste Wert scheint tatsächlich für den besten (oder zumindest sehr guten) Zug zu stehen, wirkt aber nicht soo nachvollziehbar. 

## Befehle
Befehle können groß oder klein geschrieben werden. Eckige Klammern geben optionale Teile an. Runde Klammern zeigen welche Zeichen alle an dieser Stelle stehen können.
* `n[e[w]]`: Neues Spiel
* `b[a[c[k]]]`: Gehe zurück zur letzten Stellung.
* `a[u[t[o]]]`: Computer spielt ab jetzt für den aktuellen Spieler. Nach Eingabe wird der Computerzug sofort ausgeführt. Eine erneute Eingabe beendet das automatische Ausführen des bestbewerteten Zugs für den Gegner. Achtung! Der Computer kann aktuell nur mit den Damen spielen! Sollte durch ein Schach kein Damenzug möglich sein geschehen womöglich seltsame Dinge... 
* `(abcdefgh)(12345678)[(abcdefgh)(12345678)][p]`: Figur, die bewegt werden soll. Optional kann ein Ziel angegeben werden, dies wird allerdings nur beachtet, wenn der König bewegt werden soll und es mehrere Zugmöglichkeiten gibt. Das optionale `p` zeigt eine Vorschau aller möglichen Züge der gewählten Figur. 
* ` ` (leere Eingabe): Führe vorgeschlagenen Zug aus. 

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
* `(black|white)PlayerColor`: Textfarbe der Figuren beider Spieler. Normalerweise `Fore.LIGHTWHITE_EX` und `Fore.RED`. Sollte jeweils nur eine Farbe sein und nur die Textfarbe (`Fore.*`) betreffen. Achtung: manche Farben führen zu Fehlern - liegt nicht an mir.
* `borderColor`: Summe aller Farbparameter für die Spielfeldberandung. Normalerweise `Back.GREEN + Fore.LIGHTYELLOW_EX`. Achtung: manche Farben führen zu Fehlern - liegt nicht an mir.

## Fehlende/kommende Funktionen
* Keine Illegalen Züge in der Vorschau. Obwohl nicht durchführbar, werden sie als mögliche Vorschau angezeigt. In der jetzigen Umsetzung schwierig zu ändern (warum es wohl unter dieser Überschrift steht...).
* Bauer => Dame
* Tiefenanalyse der aktuellen Position. Im Moment wird nur eine mathematische Bewertung der jetztigen Position durchgeführt, ohne eine wirkliche Untersuchung der Gewinnchancen. 
