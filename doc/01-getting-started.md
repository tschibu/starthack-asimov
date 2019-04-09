
# Getting Started

## Inspiration
Die Challenge von autoSense (autoSense ist eine Tochtergesellschaft der Swisscom AG) bot Teilaufgaben wie physikalische Berechnungen, Visualisierung, Präsentation und Kommunikation durch Webtechnologien, zu welchen wir bereits ein fundiertes Wissen besassen. Das war dann auch unsere Motivation, uns in dieser Challenge zu messen.


## Um was geht es?
Die Lösung empfängt JSON-Dateien von Auto-Unfall-Daten über eine REST API. Als Ergebnis soll die
Beschädigung, die auf das Auto eingewirkt hat, visualisiert werden. Die Visualisierung soll noch mit zusätzlichen
Informationen wie G-Force, Zeitpunkt des Crashs und dem Offset in der Zeitreihe angereichert werden.


## Wie wurde es umgesetzt?
Als Fundament haben wir einen Webserver (sanic) verwendet, um die API-Aufrufe zu implementieren. Im Hintergrund sind
alle Funktionen und Klassen mit Python implementiert. Für die Visualisierung haben wir uns für OpenCV 4.0 entschieden. Wir haben das
gesamte Projekt auch als Docker Image umgesetzt, so dass es überall und jederzeit eingesetzt werden kann.

Um dem Projekt einige Extras hinzuzufügen, haben wir uns entschieden, ein kleines, übersichtliches Web UI zu erstellen, in dem wir grundlegendes HTML5, CSS und natürlich JavaScript verwendet haben.


## Herausforderungen
Die Mathematik, um den Aufprall zu berechnen, hat definitiv sehr viel Zeit in Anspruch genommen.
Wir haben manchmal einige komische Werte bekommen - dass lag zum Teil daran, dass wir auf ein Transformation-Problem gestossen sind. Nach der Behebung von diesen Problemen sahen dann die Visualisierungen einheitlicher aus.


## Accomplishments
Wir sind stolz darauf:
* Solide Mathematik
* Maintainable Code
* Clean Code
* Visualisierung


## Was wir gelernt haben
Wir haben viel Mathematik/Physik angewendet, das meiste haben wir in der Schule einmal gelernt aber nie richtig angewendet.
Der Hackathon war für als Gruppe ausserdem ein wirklich gutes Training. Wir haben gelernt, wie man besser und effizienter miteinander zusammenarbeitet, um ein grösseres Projekt wie die autoSense-Challenge anzugehen.


## What's next?
Als nächstes wollen wir unsere Lösung aufpolieren. Wir würden gerne noch ein paar Crash-Daten und ein paar Realbilder
einholen, um damit zu überprüfen, ob wir die richtigen Dinge berechnet haben. Außerdem gibt es einen Azure Webspace der
darauf wartet, dass unsere App veröffentlicht wird.


## Built with <3 and:
* Python
* Docker
* vanillaJS
* HTML5
* CSS
* Microsoft Azure
* OpenCV
* Web Framework 'sanic'


## Github Repository
[STARThack Team 'asimov' Github Repository](https://github.com/tschibu/starthack-asimov "STARThack Team 'asimov' Github Repository")
