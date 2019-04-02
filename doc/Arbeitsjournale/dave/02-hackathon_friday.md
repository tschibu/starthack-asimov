# Freitag 7. März 2019

*Der Tag steht ganz im Zeichen von AI, Deep-Learning, Blockchain und noch mehr #Buzzwords.*

## - 14.00 Uhr - Anreise

Um 14:00 Uhr ging es Los. Mit vollbepacktem Auto Richtung STARThack. Auf dem Weg haben wir schon viele Gedanken und Ideen in einem Brainstorming ausgetauscht. Neben den STARThack Challenges gibt es immer die Möglichkeit ein eigenes Projekt zu verfolgen.
Wir einigten uns darauf die Challenges abzuwarten bevor wir uns festlegen, den mit den aufgelisteten Partnern wie Microsoft, Swisscom & Bosch ist definitiv ein grosses Potential für spannende Projekte vorhanden.

## - 16.00 Uhr - Anmeldung und Einrichten

Wir sind an der Uni St. Gallen angekommen und suchen zuerst mal einen Parkplatz, an dem wir unser Ganzes Material abladen können. Nachdem wir einen geeigneten "HSLU Ecken" an der Uni St. Gallen gefunden haben, ging es weiter zur Akkreditierung, wo wir unser Team registrieren konnten und unsere STARThack Pässe erhielten.
Als nächster Punkt auf der Tagesordnung stand die Opening Ceremony sowie die Präsentation der Challenges.
Bis dahin, richteten wir unsere Arbeitsplätze noch optimal ein. Bildschirm, Maus und Tastatur werden installiert.
Der Raspberry bleibt vorerst noch in der Tasche.


## - 19.00 Uhr - Case Präsentationen / Opening Ceremony

Im grossen Hörsaal der HSG ging es dann los mit der Opening Ceremony.
Angefangen mit einer sehr Interessanten Key Note von Damion Borth (aka Germanys Mr. Deep Learning) über Ai, Machine Learning und neuronale Netze.
Danach ging es los mit der Präsentation der 8 verschiedenen Challenges:

- Microsoft: Microsoft AI
- Volvo: Car Sharing App
- Autosense: Generating and Visualizing Crash Data
- Leica: Accurate Augmented Reality
- FLETA: Blockchain
- INVENTEX: Trust Systems
- SBB: Coffee Cup Recycling
- BOSCH: New Car Features

Die detaillierten Case Beschreibungen findet man hier: http://live.STARThack.ch/case-descriptions/

## - 20.00 Uhr Brainstorming

Wir hatten nach den kurz Präsentationen noch Zeit 2 Cases im Details anzuhören. Wir entschieden uns für autoSense und BOSCH.

Im **BOSCH** Case ging es darum, neue Features für ein "modernes" Auto zu entwickeln, welche die Umweltbilanz, Sicherheit und/oder Gesundheit des Fahrers verbessern sollen.
Dabei stellte BOSCH ein Auto zur Verfügung, bei welchem Sensor Daten über eine API abgefragt werden konnte.
Ausserdem bestand die Möglichkeit ein Tablet sowie die Stereoanlage im Auto zu manipulieren - mehr jedoch nicht.
Ein kontrolliertes abbremsen des Fahrzeuges bei einem Sekundenschlaf wäre nicht möglich über die angebotene API.

Im **Autosense** Case ging um eine SensorBox welche via OBD Sensor-Daten vom Auto ausliest.
Zusätzlich besitzt die Autosense-OBD-Box noch eigene Sensoren wie ein Accelerometer, welches als "Crash Sensor" fungiert.
Die Challenge bestand darin, mithilfe der Sensor Daten zu berechnen wo im Auto der Einschlag, bei einem Umfall, war.
Das ganze sollte danach als 3D Modell visualisiert und via REST-Schnittstelle zur Verfügung gestellt werden.

Bis 22 Uhr hatten wir Zeit uns für ein Thema zu entscheiden.
Aufgrund des Mathematischen Charakters wählten wir die **Autosense** Challenge und erhielten die Bestätigung um 22:00 Uhr - es geht los.


## - 22.00 Uhr Planung

Zuerst ging es mal um die Planung. Wir überlegten was alles zu tun ist und was die besten Mittel zum Ziel sind.
Wir entschieden uns, das sich jeder zuerst eine halbe Stunde in die Materie einliest und wir uns danach für ein Stand-Up treffen.

Wir waren uns zum Glück schnell einig, was für Komponenten für die Lösung notwendig sind.
Im Stand-Up definierten wir dann auch gleich die einzusetzenden Werkzeuge/Libraries:

- Daten Transformation: JSON Parser, Mathematische Berechnungen
- Webserver für REST API: Sanic
- Visualisierung der Daten: OpenCV
- Cloud Kompatibilität: Docker

Danach teilten wir die Aufgaben auf. Steve kümmerte sich um den Webserver, Remo um die Visualisierung und Serge und ich um den JSON Parser und die Mathematischen Berechnungen.

## - 23.30 Uhr Start Coding (till drop)

jetzt ging es also Effektiv los mit dem Coding. Jeder erstellte im Git Development Branch ein Feature und begann zu Coden.

Ich schaut mir zuerst mal das JSON genau an, um herauszufinden was für Daten relevant sind für die Berechnung und wie sie codiert sind.
Dabei sah ich schon die erste Hürde, die ganzen Daten sind unleserlich: Base64 Codiert.

Zuerst erstellte ich also eine Hilfsfunktion zum dekodieren auf UTF-8.
Danach konnte ich im Parser die Daten weiter analysieren. Vor allem die Beschleunigungsdaten (x, y und z-Achse), sowie
die Referenzwerte zu g (Anziehungskraft) und der sogenannte "Time Offset" - also die relative Zeit, zum Start des
Crash-Recording, an dem eine spezifische Beschleunigung gemessen wurde - waren wichtig.

Ca. um 02:30 Uhr haben Serge und ich uns abgesprochen, schon etwas müde entschieden wir uns, dass wir die Offset Zeiten unbedingt in reale Zeiten umwandeln müssen für eine akkurate Berechnung. Das beschäftigte uns bis ca. 03:30 Uhr und stellte sich dann als absolut nutzlos heraus - zurück auf Anfang also.

Die Offset Zeiten belassen wir nun wie sie waren, nach einem kurzen Stand-Up definierten wir, was effektiv wichtig ist für die Berechnung des Einschlagwinkels und der Einschlagkraft:

- Die Beschleunigungen x und y-Achse
- Umwandlung der Beschleunigungen in g (mit Hilfe des g-Referenz Parameters)
- Winkel des Einschlags mittels Vektorgeometrie

Um 04:30 waren wir soweit bereit mit dem Parser. Alles relevante wurde umgerechnet, nun ging es um die Mathematik.
Nach Bald 24h ohne Schlaf war mein Gehirn aber nicht mehr in der Lage für simple Mathematik, sämtliche Berechnungen die ich bis 06:00 gemacht habe waren falsch.

Um 06:00 war es dann soweit und mein Körper verlangte dringend Schlaf. Ich legte mich auf die Luftmatratze neben unserem
Pult und schlief für ein paar Stunden.
