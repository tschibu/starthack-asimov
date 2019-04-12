# Samstag, 8. März 2019


## - 06.00 Uhr - Schlafen

Schlafen war etwas gewöhnungsbedürftig, das Licht brannte und um uns herum war voller Betrieb. Viele Leute waren noch wach oder bereits wieder wach.
Also hiess es Kopfhörer rein, Decke über den Kopf und versuchen weiter zu schlafen.

## - 09.00 Uhr - Hacking / Coding

Wie wunderbar, was 3 Stunden schlaf bewirken können! Als ich aufwachte war ich zwar nicht wirklich erholt aber mein Kopf funktionierte wieder.
Nach dem Frühstück sah ich mir meine Berechnungen vom Vorabend an, schmunzelte über mich selbst und machte die Berechnungen nochmals neu. Diesmal stimmten sie.

Der Trick war, die Euklidische Distanz mittels x und y Kräften zu berechnen, so konnte schlussendlich auf den Einschlagwinkel abgeleitet werden.

Der erste Testrun ergab aber merkwürdige Resultate, da sah ich dass die Beschleunigungswerte von autoSense nicht ohne
weiteres umgerechnet werden konnten. Es musste zuerst mittels einer weiteren Hilfsvariable (Calibration genannt) umgerechnet werden. Denn die Beschleunigungswerte sind auch nur "relativ" zur am Anfang gemessenen Calibration.

## - 12.00 Uhr - Lunch

Um 12:00 Uhr ging es dann zum Lunch, Reis und Chili con Carne.
Übrigens, was die Ganze Verpflegung und die Organisation rund um den Hackathon anbelangt: Respekt.

Rund um die Uhr war der hilfsbereite Staff vom STARTHack anwesend.
Überall standen Kühlschränke mit Getränken. Und es gab sogar separate, immer volle, RedBull Kühlschränke (ich glaube ich habe 20 RedBull an diesem Wochenende getrunken).

## - 13.00 Uhr - Hacking / Coding

Nach der Mittagspause ging es dann weiter. Ich vervollständigte meinen Teil des Parsers sowie die Berechnungen.
Der Webserver schien soweit auch schon fast bereit zu sein.

Gegen 17 Uhr funktionierten dann die Berechnungen soweit zuverlässig.
Ich konnte dann noch Remo unterstützen, um via OpenCV eine Grafik der Einschlagkraft und des Winkels zu berechnen.
Auch hier war wieder etwas Mathematik notwendig, um aus dem Winkel einen Pfeil zu machen.
Auch hier wieder, Trigonometrie dein Freund und Helfer. Mittels Sinus und Cosinus sowie einem "virtuellen" Punkt in der Bildmitte konnten wir akkurat den Einschlagwinkel visualisieren.
Bei der Visualisierung der Einschlagkraft entschieden wir uns für einen Ring, welcher je nach Grösse der Einschlagkraft (in unseren Testdaten zwischen 2 und 11g) grösser wurde.

Nach dem Abendessen ging es dann um die Kombination aller Teilsysteme.
Um ca. 22 Uhr hatten wir dann ein funktionierendes Docker Image, welches die Daten als JSON entgegennimmt, berechnet und visualisiert.

Soweit waren wir also eigentlich fertig, ein gutes Gefühl. Da wir uns aber nicht mit der Grundfunktionalität alleine Zufrieden geben, definierten wir noch die "Stretch Goals":

- HTMl/CSS Website
- JSON Daten via Drag&Drop einlesen
- Weitere nützliche Infos (Crash Date, Offset...)
- Azure Webservice

Um ca. 2:00 Uhr hatten wir eine halbwegs vernünftige Website kreiert. Die Müdigkeit war bei uns allen aber so gross,
dass wir es für heute gut sein liessen und uns Schlafen legten.
