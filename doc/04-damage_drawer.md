# Damage drawer


## Funktionsumfgang


sads
asd



## Funktiondesign


Print-Screen Tablet
Skizze

![Skizze Damage drawer](Ximg/skizze_damage.png "Skizze Damage drawer")

## Umsetzung

Klassendiagramm und Beschreibung der einzelnen Methoden

## Klasse DamageImage

![Klassendiagramm Damage drawer](img/STARTHack_damage_image.png "Klassendiagramm Damage drawer")

### Init

```python
def __init__(self, angle_impact, max_force, damage_id, crash_time, max_force_offset=None):
```

### Kulturen Auto 

```python
def __cut_car(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Zeichnen

```python
def __draw(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Zeichnen - Pfeil

```python
def __draw_arrow(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Zeichnen - Kreis

```python
def __draw_circle(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Text auf das Bild 

```python
def __add_text(self, off_set_in_milliseconds):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Berechnung Beschädigung

```python
def __dynamic_damage_calc(self, damage):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

### Schreiben der Bilddatei

```python
def __write_image(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Pfad der geschriebene Datei

```python
def get_image(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


### Löschen von allen gerendert Dateien

```python
def remove_all_rendered_image(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

### Anzeige der Datei auf dem Bildschirm

```python
def show_image(self):
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.


## Implementierung im Projekt

Aufruf bei /api/v1/getCrashImage wie auch bei /api/v1/play


## Mögliche Darstellung der Datei in einem Protal


![Anzeige in einem Portal](img/insurance_portal.jpeg "Damage drawer on a Portal")


