# Damage drawer


## Funktionsumfgang

Mit der Klasse DamageImage (File: `damage_image.py`) werden alle Funktionalitäten im Zusammenhang mit der Bild zusammengebündelt. Die Umfasst als Beispiel das Erkennen der Kulturen von dem Auto, das Zeichnen der Beschädigung wie auch das Beschriften der Milisekunden des Aufpralls, die Crash-ID und weiter Informationen.


## Funktiondesign


### Software Abhängigkeiten

Für die Erkennung der Kulturen wurde die Bildverarbeitungs Library OpenCV (Open Source Computer Vision Library) verwendet. Die Kulturen werden verwendet um den Eintrittspunkt der Beschädigung zu berechnen.

Für die Berechnung innderhalb der Klasse DamageImage wurde auf die bekannte Python Library Numpy (http://www.numpy.org) zurückgefriffen.

Die Python Standardbibliothek `os` / `math` / `shutil` werden für kleinere Funktionen benötigt.


### Prozess des Funktiondesigns

Zu Beginn wurde mittels OpenCV die Datei eingelesen und hardcoded ein Kreis und ein Pfeil gezeichnet. Mit dieser Version haben wir dann im Team das Zieldesign der Bilddatei mittels iPad und Pen gezeichnet.

|Erste Version Damage Image                                                         |
|:---------------------------------------------------------------------------------:|
|![Erste Version Damage Image](img/first_version.png "Erste Version Damage Image"){ width=300px }  |

|Skizze Damage drawer                                                 |
|:-------------------------------------------------------------------:|
|![Skizze Damage drawer](img/skizze_damage.png "Skizze Damage drawer"){ width=300px }|


## Klasse DamageImage

Teilfunktion: Damage Image

![Klassendiagramm Damage drawer](img/STARTHack_damage_image.png "Klassendiagramm Damage drawer")


## Implementierung im Projekt

Innerhalb von dem Projekt werden wir die Funktion `get_image` wie folgt benutzt:

![Verwendung von dem Damage drawer](img/STARTHack_damage_image_usage.png "Verwendung von dem Damage drawer")

Innerhalb vom `server.py` wird ein Damage drawer Objekt erstellt und mittels der Funktion `get_image` die fertig gerenderte Bilddatei zurückgegeben und auf der Webseite dargestellt.


## Mögliche Darstellung der Datei in einem Portal

Ein möglicher Einsatzbereich von unserem Projekt könnte ein Portal von einer Versicherung sein. Hier würde bei Autounfällen der Ort von dem Schaden wie auch das Ausmass der Beschädigung aufgezeigt werden. So kann ein Mehrwert in Form von mehr Informationen an dem Kunde einer Autoversicherung entstehen.

|Anwendungsmöglichkeit in einem Portal                                              |
|:---------------------------------------------------------------------------------:|
|![Anzeige in einem Portal](img/insurance_portal.jpeg "Damage drawer on a Portal"){ width=400px } |


