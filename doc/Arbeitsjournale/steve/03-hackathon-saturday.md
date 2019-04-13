# Samstag, 8. März 2019

*Coden, Schlafen/Dösen, Richtig Schlafen, Auf Touren kommen, Docker & UI, Pizza Time, UI & Testing*

## - 00.00 Uhr - Coding

Bei unserem Case mussten wir eine REST API implementieren, sodass unser Code, zur Berechnung von Schäden bei einem
Umfall, getestet werden konnte. Ich habe diese Aufgabe übernommen, da ich schon für das Modul PREN eine REST API
implementiert habe. Für die Implementierung haben wir Python verwendet. Als Bibliothek für die REST API haben wir
'sanic' (ein Python Framework) verwendet. Die Bibliothek ermöglicht es Routen zu definieren und mit Funktionen zu
verbinden. So hatte ich schnell die erste funktionierende Applikation, welche Dummy Daten zurückgibt und verarbeitet. Die
korrekten Routen und Parameter der Anfragen sind definiert und funktionieren.
Als nächstes habe ich mich mit Docker auseinandergesetzt, um unsere Applikation in einem Container laufen zu lassen.
Dies ist notwendig, da in Beschrieb der Challenge gestanden ist, dass die Applikation einfach Gehostet werden kann.
Langsam aber sicher wurde ich aber müde und musste mir eine passende Schlafgelegenheit suchen.

## - 06.30 Uhr - Schlafen/Dösen

Ich habe mich zuerst in den Ball-Pool zurückgezogen und habe versucht zu schlafen. Mit wenig Erfolg. Ich habe zwar etwas
entspannt aber bin immer noch Müde. Deswegen habe ich nach einer anderen alternative gesucht und habe dann die
Schlafgelegenheit von Remo gekapert.

## - 08.00 Uhr - Richtig Schlafen

Endlich konnte ich richtig schlafen.

## - 11.00 Uhr - Auf Touren kommen

Nach gut drei Stunden richtig schlafen bin ich noch sichtlich Müde. Aber ich konnte nicht mehr weiterschlafen.
Deswegen habe ich frische Luft geschnappt und bin etwas Essen gegangen.

## - 13.00 Uhr - Docker & UI

Wieder fokussiert und motiviert ging es weiter mit Coding. Ich habe die Arbeit am Docker Container abgeschlossen und
habe die ersten Versuche mit den Bibliotheken, welche die anderen geschrieben haben, gemacht.
Um die Anforderungen schnell und einfach zu testen, haben wir uns dazu entschieden ein Web UI zu implementieren.
Ich habe mir also erstmal überlegt, wie ich die Anfragen vom Browser an unser Server senden kann und wie die Seite etwa
aussehen soll. Ich habe unser existierende REST API erweitert, sodass sie auch eine HTML Seite zurückgeben kann unter
einer bestimmten URL. Für die Anfragen vom Browser aus habe ich normales JavaScript verwendet.
Da Design sekundär, da wir primär auf die Funktionalität angewiesen sind.

## - 19.00 Uhr - Pizza Time

Zum Nachtessen gab es feine Pizza. Ich musste aber schummeln um ein zweites Stück zu ergattern.
Später am Abend kam heraus, dass sie noch viel Resten haben und man doch noch ein Pizza stück bekommen kann.

## - 20.00 Uhr - UI & Testing

Ich habe das UI so erweitert, dass man ein beliebiges JSON File hochladen kann. Dieses wird dann an das Backend
gesendet. Falls es ein JSON ist, welches unsere API unterstützt wird der Schaden berechnet und ein Bild kommt
zurück. Auf dem die Schäden des Unfalls eingezeichnet sind. Ausserdem werden noch Kennwerte angezeigt welche von der anderen Anfrage
zurückkommen. In diesem Moment war noch nicht die Ganze Bibliothek der Anderen in Betrieb. Ein Teil war noch simuliert
und wurde nun Schritt für Schritt finalisiert. Am Ende des Abends hatten wir die erste funktionierende Version.
Ob alles Akkurat ist haben wir aber noch nicht im Detail überprüft.
