# Samstag, 8. März 2019

*Coden, Coden, Coden...*

## - 00.00 Uhr - Coding

Unser Case beinhaltet die Berechnung von Schadenslokation und Ausmass eines Autos anhand von Sensordaten (Beschleunigungssensor) und deren Ausgabe via eines Webinterfaces. Dave und ich haben die Aufgabe des Parsings der Eingabedaten und deren Berechnung gefasst.
Die Daten kommen im JSON-Format daher und müssen noch BASE64 decodiert werden. Dank der Nutzung von Python ist das Parsen ein Kinderspiel: import json, import base64 - erste Aufgabe erfüllt.
Dave und ich überlegen uns, welche Funktionen wir brauchen, um die Implementation danach aufzuteilen, damit wir unabhängig voneinander daran arbeiten können. Wir schreiben die Funktions-Signaturen und Doc Strings, um zu definieren, welche Funktion was genau tun soll und machen uns dann an die Implementation.

## - 06.00 Uhr - Schlafen

Nachdem Remo und Dave sich schon hingelegt haben, bemerken Steve und ich, dass wohl auch uns etwas Schlaf gut tun würde. Dank grosser Müdigkeit schlafe ich kurz nach dem Hinlegen ein.

## - 07.15 Uhr - Coding

Nach knapp mehr als einer Stunde Schlaf bin ich wieder wach. Ob es an dem hellen Licht, dem umliegenden Getue, dem Koffein im Blut oder am nicht ganz so bequemen Schlafplatz liegt - egal, wir haben nicht mehr ganz 27 Stunden Zeit und mit viel Schlaf habe ich ja sowieso nicht gerechnet.
Die anderen schlafen noch, also setze ich mich an meinen Laptop, betrachte die bereits gemachte Arbeit und überlege mir, was als nächstes zu tun ist. Ich merke, dass mein Hirn noch nicht ganz wach ist und bin nicht gerade produktiv. Als dann Remo aufwacht und vorschlägt zu frühstücken finde ich das also eine sehr gute Idee.
Das gestrige Essen am Hackathon war zwar keine Gourmet-Küche, entsprach aber meinen Erwartungen und ich hatte nichts daran auszusetzen. Über das Frühstück lässt sich das leider nicht sagen. Müesli mit Milch und Brot mit Butter und Nutella. Nicht wirklich vielseitig; aber naja, besser als nichts. Wer gesund leben möchte ist wohl nicht nur wegen dem Essensangebot an einem Hackathon definitiv falsch am Platz.
Danach geht es wieder an die Arbeit. Wir analysieren die Sensor-Daten und überlegen uns, wie wir die Berechnungen durchführen müssen. Die Daten scheinen aber ziemlich wirr und wir sind uns nicht sicher, wie wir daraus etwas Sinnvolles auslesen sollen. Bei mir macht sich Ernüchterung breit ich frage mich, wieso ich mir das überhaupt antue. Nach weiterem Diskutieren haben wir dann aber festgelegt, wie wir weiterfahren, und mit einem Ziel vor Augen steigt die Motivation wieder.

## - 12.00 Uhr - Lunch

Am Mittag stärken wir uns mit Reis und Chili con Carne. Lecker.

## - 13.00 Uhr - Coding

Die nächsten Stunden verschwimmen vor dem geistigen Auge: Coden und diskutieren. Ich denke, wir machen gute Fortschritte. Später, nach ein paar Refactorings um den Code verständlicher und performanter zu machen ist die Funktionalität der Berechnungen soweit gegeben.

## - 19.00 Uhr - Dinner

Es gibt Pizza - hurra! Ich genehmige mir eine zweite Portion.

## - 20.00 Uhr - Guess what?

Wir coden weiter. Wir arbeiten daran, die verschiedenen Komponenten unseres Systems nun zusammenzufügen: Der Webservice schickt zuerst die Eingangsdaten an den Data-Parser, welcher dann die gesuchten Werte berechnet und zurück gibt und anhand dieser dann das generierte Bild vom Crash-Image-Modul erhält.
Soweit so gut; nun geht es ans Korrigieren, Verbessern und Optimieren; ausserdem entwickeln wir noch ein Web Interface für den Webservice.

\pagebreak
