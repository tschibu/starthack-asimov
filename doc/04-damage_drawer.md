# Damage drawer

## Funktionsumfgang

Mit der Klasse DamageImage (File: `damage_image.py`) werden alle Funktionalitäten im Zusammenhang mit der Bild zusammengebündelt. Die Umfasst als Beispiel das Erkennen der Kulturen von dem Auto, das Zeichnen der Beschädigung wie auch das Beschriften der Milisekunden des Aufpralls, die Crash-ID und weiter Informationen.

## Funktiondesign

### Software Abhängigkeiten 

Für die Erkennung der Kulturen wurde die Bildverarbeitungs Library OpenCV (Open Source Computer Vision Library) verwendet. Die Kulturen werden verwendet um den Eintrittspunkt der Beschädigung zu berechnen.

Für die Berechnung innderhalb der Klasse DamageImage wurde auf die bekannte Python Library Numpy (http://www.numpy.org) zurückgefriffen.

Die Python Standardbibliothek `os` / `math` / `shutil` werden für kleinere Funktionen benötigt. 

### Prozess des Funktiondesigns 

Zu Beginn wurde mittels OpenCV die Datei eingelesen und hardcoded ein Kreis und ein Pfeil gezeichnet. Mit dieser Version haben wir dann im Teamm das Zieldesign der Bilddatei mittels iPad und Pen gezeichnet. 

Erste Version Damage Image                                                         |
:---------------------------------------------------------------------------------:|
![Erste Version Damage Image](img/first_version.png "Erste Version Damage Image")  |

  Skizze Damage drawer                                                 |
:---------------------------------------------------------------------:|
  ![Skizze Damage drawer](img/skizze_damage.png "Skizze Damage drawer")|


## Realisation / Umsetzung

Klassendiagramm und Beschreibung der Funktionen der einzelnen Methoden.

## Klasse DamageImage

Teilfunktion: Damage Image

![Klassendiagramm Damage drawer](img/STARTHack_damage_image.png "Klassendiagramm Damage drawer")

### Methode: Init

```python
def __init__(self, angle_impact, max_force, damage_id, crash_time, max_force_offset=None):
```

Die Init Methode wird aufgerufen bei der Instanzierung von einem Objekt. Als Parameter werden folgende Informationen benötigt:

| Paramenter               | Beschreibung
|--------------------------|------------------------------------------------------------------------------------------------------------|
| `self`                   | Instanz-Referenz                                                                                           |
| `angle_impact`           | Winkel in Grad. Mit diesem Winkel wird der Aufprall der Beschädigung gezeichnet.                           |
| `max_force`              | Numerischer Wert mit dem die Grösse der Beschädigung am Auto berechnet wird.                               |
| `damage_id`              | String. Eindeutiger Crash-Report ID                                                                        |
| `crash_time`             | String. Uhrzeit für die Beschriftung auf dem Bild                                                          |
| `max_force_offset`       | Numerischer Wert. Zeitpunkt, nach wie vielen Millisekunden die Beschädigung berechnet wurde (Default=None) |

Mit den Methoden Parameter werden die jewiligen lokalen / privaten Methodenvariabeln initialisiert und den Wert zugewiesen. Weiter wir de Pfad wo die Bilddatei gespeichert wird aufgrund der `damage_id` und der allfälligen `max_force_offset`. Die Dateine werden in einem speziell definierten Ort (`images_rendered/`) gespeichert. Dies hat den Grund, dass wenn die Bilddatei von den gleichen Crash-Report und dem gleichen `max_force_offset` nicht nochmals neu erstellen und schreiben muss, sondern direkt zurückgeben kann. 

### Methode: Kulturen Auto 

```python
def __cut_car(self):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |

Die Methode `__cut_car` findet mittels OpenCV die Kulturen (Randkulturen) von dem Auto-Bild. Diese Kulturen werden als Pixel-Matrix abgespeichert und später für den Eintrittspunkt der Beschädigung benötigt. Dazu wird das Auto-Bild in Schwarz/Weiss konvertiert und den Threshold für die Linien gesetzt. Mittels der OpenCV Funktion `cv2.findContours` können die äussersten, geschlossenne Linien abgefragt werden.


### Methode: Zeichnen

```python
def __draw(self):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |

Die generelle Zeichnungsmethode `__draw` ist als Wrapper Methode zu verstehen. Wenn gegebenenfalls noch weitere Beschriftungen auf die Bilddatei geschrieben werden soll, kann dies hier eingefügt werden. Hier passiert auch die Entscheidung ob der Text für den Offset der Millisekunten angezeigt wird oder nicht.


### Methode: Zeichnen - Pfeil

```python
def __draw_arrow(self):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |

Hier wird der Pfeil für die Bilddatei gezeichnet. Etwas unschön ist hier, dass auch noch der Nullpunkt des Koordinatensystem in dieser Methode gezeichnet wird. Eine entsprechendes `# TODO:` ist hier vermerkt.


### Methode: Zeichnen - Kreis

```python
def __draw_circle(self):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |

Der Kreis für die für die Grösse der Beschädigung wird hier auf die Bilddatei gezeichnet. Die Grösse von dem Kreis (Radius) wird mit Hilfe der Funktion `__dynamic_damage_calc` berechnet.


### Methode: Text auf das Bild 

```python
def __add_text(self, off_set_in_milliseconds):
```

| Paramenter                            | Beschreibung
|---------------------------------------|----------------------------------------------------------------------------------------------|
| `self`                                | Instanz-Referenz                                                                             |
| `off_set_in_milliseconds`             | Numerischer Wert. Zeitpunkt, nach wie vielen Millisekunden die Beschädigung berechnet wurde  |


Auf der resultierende Bilddatei werden folgende Informationen dargestellt:

* Time-Offset von der maximalen Beschädigung
    * Text: `Rendered crash image after " off_set_in_milliseconds + "[ms]"`
* Eindeutige Bilddatei Beschriftung mit der entsprechender Uhrzeit aus dem Crashreport
    * Text: `crash identifier = " + self.damage_id + " - damage time = " crash_time`


### Methode: Berechnung Beschädigung

```python
def __dynamic_damage_calc(self, damage):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                             |
| `damage`           | Numerischer Wert mit dem die Grösse der Beschädigung am Auto berechnet wird. |


Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

### Methode: Schreiben der Bilddatei

```python
def __write_image(self):
```
| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |


Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Methode: Pfad der geschriebene Datei

```python
def get_image(self):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Methode: Löschen von allen gerendert Dateien

```python
def remove_all_rendered_image(self):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

### Methode: Anzeige der Datei auf dem Bildschirm

```python
def show_image(self):
```

| Paramenter         | Beschreibung
|--------------------|------------------------------------------------------------------------------------------------------------|
| `self`             | Instanz-Referenz                                                                                           |

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


## Implementierung im Projekt

Aufruf bei /api/v1/getCrashImage wie auch bei /api/v1/play


## Mögliche Darstellung der Datei in einem Protal


![Anzeige in einem Portal](img/insurance_portal.jpeg "Damage drawer on a Portal")


