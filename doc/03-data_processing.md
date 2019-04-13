# Data Parser / Data Processing


## Funktionsumfang

Mit der Klasse Data_Parser werden alle Funktionalitäten im Zusammenhang mit der Datenverarbeitung, Auswertung und Konvertierung erledigt.
Das beinhaltet das einlesen der JSON Daten, ausfiltern der relevanten Key:Value Paare, transformieren der relativen Werte sowie die mathematischen umrechnungen auf die geforderten Output Daten (Kraft & Winkel des Einschlags)


### Software Abhängigkeiten

Zum auslesen der JSON Daten wurde die Python Library `json` verwendet. Zur Decodierung und Encodierung wurde das base64 Format verwendet.
Für die Mathematischen Umrechnungen wurden die Libraries `math`, `pandas` sowie `numpy` verwendet.

Für die Umrechnung der relativen Zeiten konnte auf die Standard Library `datetime` zurückgegeriffen werden.

Um während dem Testing ein sauberes Logging zu erhalten, wurde auch hier unsere gemeinsame Log-Klasse `log_helper` eingebunden.


### Prozess des Funktiondesigns

Zu Beginn werden die JSON Input-Daten eingelesen und der Payload extrahiert. Dieser ist im Base64-Format und muss daher zuerst decodiert werden; danach werden die relevanten Key:Value Paare (Beschleunigung, Timestamps) ausgelesen.
Diese Daten werden danach mit einer vordefinierten Kalibration transformiert und mit einem Referenz-G Wert in G-Kräfte umgewandelt.
Zum Schluss erfolgt die Umwandlung der Kräfte in einen Winkel, relativ zur virtuellen Bildmitte.
Zeit, Kraft und Winkel werden danach zur Visualisierung an die Klasse `Damage_drawer` übergeben.


## Klasse DataParser

Teilfunktion: Data Parser

![Klassendiagramm Data Parser](img/STARTHACK_data_parsers_class.png "Klassendiagramm Data Parser")


## Implementierung im Projekt

Innerhalb des Projekts wird die Funktion `parse_input_data` wie folgt benutzt:

Die Json Daten werden an die Klasse "data_parser" übergeben, welche danach die Rückgabewerte Kraft, Winkel und Zeit liefert.
Diese Informationen werden einem drawer-Objekt übergeben, welches anhand dieser Parameter das Einschlagsbild zeichnet.

