# Samstag, 8. März 2019


## - 06.00 Uhr - Schlafen

Schlafen war etwas gewöhnungsbedürftig, das Licht brannte und um uns herum war voller Betrieb, viele Leute waren noch wach oder bereits wieder wach.
Also hies es Kopfhörer rein, Decke über den Kopf und versuchen zu schlafen.


## - 09.00 Uhr - Hacking / Coding

Wie wunderbar 3 Stunden schlaf wirken können! Als ich aufwachte war ich zwar nicht wirklich erholt aber mein Kopf funktionierte wieder.
Nach dem Frühstück sah ich mir meine Berechnungen von gestern an, schmunzelte über mich selbst, und machte die Berechnungen nochmals neu, diesmal stimmten sie.

Der Trick war, die EUklidische Distanz mittels x und y Kräften zu berechnen, so konnte schlussendlich auf den Einschlagswinkel abgeleitet werden.

Der erste Testrun ergab aber merkwürdige Resultate, da sah ich dass die Beschleunigungswerte von Autosense nicht ohne weitere umgerechnet werden konnten, sondern zuerst
mittels einer weiteren Hilfsvariable (genannte Calibration) umgerechnet werden mussten. Denn die Beschleunigungswerte sind auch nur "relativ" zur am Anfang gemessenen Calibration.

## - 12.00 Uhr - Lunch

Um 12:00 Uhr ging es dann zum Lunch, Spätzlipfanne mit Speckwürfeln.
Übrigens, was die Ganze Verfplegung und die Organisation rund um den Hackathon anbelangt: Resepkt.

Rund um die Uhr war Staff vom Starthack anwesend der einem helfen konnte.
Überall standen Kühlschränke mit Getränken. Und es gab sogar separate immer volle Redbull Kühlschränke (ich glaube ich habe 20 Redbull an diesem Wochenende getrunken)

## - 13.00 Uhr - Hacking / Coding



Nach der Mittagspause ging es dann weiter. Ich vervollständigte meinen teil des Parsers sowie die Berechnungen.
Der Webserver schien soweit auch schon fast bereit zu sein.

Gegen 17 Uhr funktionierten dann die Berechnungen soweit zuverlässig.
Ich konnte dann noch Remo unterstützen, via OpenCV eine Grafik der Einschlagskraft sowie des Winkels zu berechnen.
Auch hier war wieder etwas Mathmematik notwendig um aus dem Winkel einen Pfeil zu machen.
Auch hier weider, Trigonometrie dein Freund und Helfer. Mittels Sinus und Cosinus sowie einem "virtuellen" Punkt in der Bildmitte konnten wir akkurate den Einschlagswinkel visualisieren.
Bei der Visualisierung der Einschlagskraft entschieden wir uns für einen Ring, welche je nach grösse der Einschlagskraft (in unseren Testdaten zwischen 2 und 11g) grösser wurde.

Nach dem Abendessen ging es dann um die Kombination aller Teilsysteme.
Um ca 22 Uhr hatten wir dann ein funktionierendes Docker Image, welches die Daten als JSON entgegennimmt, berechnet und visualisiert.

Soweit waren wir also eigentlich fertig, ein gutes Gefühl. Da wir uns aber nicht mit der Grundfunktionalität alleine Zufrieden geben, definierten wir noch die "Stretch Goals":

- HTMl/CSS Website
- JSON Daten via Drag&Drop einlesen
- Weitere nützliche Infos (Crash Date, Offset...)
- Azure Webservice

Um ca 2:00 Uhr hatten wir eine halbwegs vernünftige Website kreiert. Die Müdigkeit war bei uns allen aber so gross das wir es für heute gut sein liesen und uns Schlafen legten.

