# Data Parser / Data Processing


## Funktionsumfgang

Mit der Klasse Data_Parser werden alle Funktionalitäten im Zusammenhang mit der Datenverarbeitung, AUswertung und Konvertierung erledigt.
Das beinhaltet das einlesen der JSON Daten, ausfiltern der relevanten Key:Value Paare, transformieren der relativen Werte sowie die mathematischen Umrechnungen auf die geforderten Output Daten (Kraft & Winkel des Einschlags)


### Software Abhängigkeiten

Zum auslesen der JSON Daten wurde die Python Library `json` verwendet. Zur Decodierung und Encodierung wurde das base64 Format verwendet.
Für die Mathematischen umrechnungen wurden die Libraries `math`, `pandas` sowie `numpy` verwendet.

Für die Umrechnung der relativen Zeiten konnte auf die Standard Library `datetime zurückgegeriffen werden.

Um während dem Testing ein sauberes Logging zu erhalten, wurde auch hier unsere gemeinsame Log Klasse `log_helper` eingebunden.


### Prozess des Funktiondesigns

Zu Beginn werden die JSON Input Daten eingelesen und der Payload extrahiert. dieser wird mit base64 decodiert und danach die relevanten Key:Value Paare (Beuschlunigung x,y,z) ausgelesen.
Diese Daten werden danach mit einer vordefinierten Kalibration transformiert und mit einem Referenz-G Wert in G-Kräfte umgewandelt.
Zum Schluss erfolgt die Umwandlung der Kräfte in einen Winkel, relativ zur virtuellen Bildmitte.
Zeit, Kraft und Winkel werden danach zur Visualisierung an die Klasse `Damage_drawer` übergeben.


## Realisation / Umsetzung

Klassendiagramm und Beschreibung der Funktionen der einzelnen Methoden.


## Klasse DamageImage

Teilfunktion: Damage Image

![Klassendiagramm Data Parser](img/STARTHACK_data_parsers_class.png "Klassendiagramm Data Parser")


### Methode: parse_input_data

```python
def parse_input_data(self, file_path, calibration=True, custom_offset=0):
```

Die Methode `parse_input_data` wird von extern verwendet und führt alle Teilfunktionen zusammen. Das JSON File wird entweder als Objekt oder als Filepath übergeben und danach verarbeitet. Zusätzlich besteht die Möglichkeit die Berechnungen ohne Kalibration auszuführen (nur für Testzwecke nützlich). Ausserdem kann via `custom_offset` ein beliebiger Offset in Millisekunden angegeben werden, standardmässig werd der Zeitpunkt der grössten Krafteinwirkung selbst berechnet.

Als Rückgabeparameter liefert die Methode: `angle_impact`, `max_force`, `damage_id`, `crash_time` und `max_force_offset`.


### Methode: get_rel_times

```python
def get_rel_times(self, jsonfile):
```

Die Methode `get_rel_times` wandelt die Relativen Zeiten Anhand des Referenzwertes zu realen Zeiten um. Diese Information wird benötigt um den genauen Zeitpunkt zurückzugeben, an dem am meisten Kräfte auf das Auto wirkten.


### Methode: __base64_decode

```python
def __base64_decode(self, base64_string):
```

Die Methode `__base64_decode` wandelt einen base64 Payload in einen UTF-8 json Paylod um.


### Methode: __convert_timestamps

```python
def __convert_timestamps(self, data, timestamp, reference_time):
```

Die Methode `__convert_timestamps` wandelt die relativen Zeiten der einzelnen Beschleunigungsmessungen in reale Zeiten um.


### Methode: calibrate_impact_data

```python
def calibrate_impact_data(self, rx, ry, rz, calibration):
```

Die Methode `calibrate_impact_data` wandelt die Arrays der x,y und z Beschleunigungen mit der von Autosense vorgegebenen Kalibration um, somit erhält man die Beschleunigungsvektoren relativ zur Auto Mitte.


### Methode: __norm_with_g

```python
def __norm_with_g(self, acceleration, one_g):
```

Die Methode `__norm_with_g` berechnet anhand der vorgegebenen G-Kraft die normierte G-Kraft des Beschleunigungsvektors.


### Methode: __calculate_forces

```python
def __calculate_forces(self, acceleration):
```

Die Methode `__calculate_forces` berechnet mittels Wurzelrechnung die effektiven Kräfte.


### Methode: __calculate_max_force

```python
def __calculate_max_force(self, acceleration):
```

Die Methode `__calculate_max_force` berechnet, wann die grösste Kraft in der Messung auftrat und gibt diese Kraft zurück.


### Methode: __calculate_offset_max_force

```python
def __calculate_offset_max_force(self, rel_time, acceleration):
```
Die Methode `__calculate_offset_max_force` berechnet, wann die grösste Kraft in der Messung auftrat und gibt den Zeitpunkt als Offset zurück.


### Methode: __calculate_custom_offset_force


```python
def __calculate_custom_offset_force(self, custom_offset, acceleration):
```
Die Methode `__calculate_custom_offset_force` berechnet, wann die Kraft zu einem beliebigen Offset in der Messung und gibt diese Kraft zurück.


### Methode: __calculate_angle

```python
def __calculate_angle(self, index,
                      predicted_impact_time, rel_time, rx, ry):
```

Die Methode `__calculate_angle` berechnet mittels euklidischer Distanz den Einschlags-Winkel anhand der Kräfte Vektoren.


### Methode: __ringbuffer2array

```python
def __ringbuffer2array(self, ringbuffer):
```

Da die Daten im JSON als Ringbuffer gespeichert werden, sortier die Methode `__ringbuffer2array` die Werte zuerst chronologisch.


### Methode: __read_json_from_filesystem

```python
def __read_json_from_filesystem(self, path2file):
```

Die Methode `__read_json_from_filesystem` liest die Input JSON Daten entweder vom Filesystem oder direkt aus einem String.


### Methode: __get_b64payload_from_basejson

```python
def __get_b64payload_from_basejson(self, base_json):
```

Die Methode `__get_b64payload_from_basejson` extrahiert den Base64 Payload aus dem Input JSON.


### Methode: __encoded_payload_to_list

```python
def __encoded_payload_to_list(self, encodedjsonstring):
```

Die Methode `__encoded_payload_to_list` konvertiert den encodierten JSON String in eine Python List zur besseren weiterverarbeitung.


## Implementierung im Projekt

Innerhalb von dem Projekt werden wir die Funktion `parse_input_data` wie folgt benutzt:

Die Json Daten werden an die Klasse "data_parse" übergeben, welche danach die Rückgabewerte Kraft, Winkel und Zeit liefert.
Diese Informationen werden einem drawer-Objekt übergeben, welches anhand dieser Parameter das EInschlagsbild zeichnet (siehe Kapitel 4.5 & 4.6)

