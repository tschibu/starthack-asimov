
# Management Summary 

## Inspiration
Die Challange von autoSense (autoSense ist eine Tochtergesellschaft der Swisscom AG) hatte wir bereits ein breites Wissen von Teilaufgaben, wie Physik, Visualisierung, Präsentation und Kommunikation durch Webtechnologien. Das war dann auch unsere Motivation, uns in dieser Challange zu messen.


## Um was geht es?
Die Lösung empfängt json-Dateien durch ein ansprechendes Web-UI und verarbeitet diese. Als Ergebnis soll die grössen Beschädigung die auf das Auto eingewirkt hat, visualisiert werden. Die Visualisierung soll noch mit zusätzliche Informationen wie G-Force, Zeitpunkt des Crashs und den Offset in der Zeitreihe angereichert werden.


## Wie wurde es umgesetzt?
Als Fundament haben wir einen Sanic v18 Webserver verwendet, um die API-Aufrufe zu implementieren. Im Hintergrund sind alle logischen Funktionen und Klassen mit Python sauber implementiert. Für den Visualisierungsteil haben wir uns für OpenCV 4.0 entschieden. Wir haben das gesamte Projekt auch als Docker Container umgesetzt, so dass es überall und jederzeit eingesetzt werden kann.

Um dem Projekt einige Extras hinzuzufügen, haben wir uns entschieden, ein kleines, übersichtliches WebUI zu erstellen, in dem wir grundlegende HTML5, CSS und natürlich Javascript verwendet haben.


## Herausforderungen
Die Physik, um den Aufprall zu berechnen, hat definitiv sehr viel Zeit in Anspruch genommen.
Wir haben manchmal einige komische Werte bekommen - dass war zum Teil darum, weil wir auf ein Transformationsproblem gestossen sind. Nach der Behebung von diesen Problemen sahen dann die Visualisierungen einheitlicher aus.


## Accomplishments
Wir sind stolz darauf:
* Solide Mathematik
* maintainable Code
* Clean Code
* Visualisierung


## Was wir gelernt haben
Wir haben viel Mathematik/Physik angewendet und natürlich OpenCV, was wir in der Schule einmal gelernt haben aber zum Teil wieder vergessen wurde.
Der Hackathon war für uns als Gruppe ein wirklich gutes Training, wir haben gelernt, wie man besser und effizienter miteinander zusammenarbeitet, um ein grösseres Projekt wie die autoSense-Challange anzugehen.


## What's next?
Als nächstes wollen wir unsere Lösung aufpolieren, auch würden wir gerne noch ein paar Crash-Daten und ein paar Realbilder bekommen, damit wir überprüfen können, ob wir die richtigen Dinge berechnet haben. Außerdem gibt es einen Azure Webspace, der darauf wartet, dass unsere App veröffentlicht wird.


## Built with <3
* python
* docker
* vanillajs
* html5
* css
* azure
* opencv
* sanic
* javascript


## Githup Repo
[Github Repo](https://github.com/tschibu/starthack-asimov "Github Repo")

