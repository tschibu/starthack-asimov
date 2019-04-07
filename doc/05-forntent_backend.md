# REST API und Frontend
Für die Challenge ist eine REST API notwendig. Diese ist genau spezifiziert und beinhaltet zwei vorgeschriebene
Requests. Wir haben im Verlauf vom Projekt noch ein UI gemacht, um die eigentlichen Requests zu testen und
dem User eine einfache Verwendung zu gewährleisten. Da in der Challenge auch noch erwähnt ist, dass das Hosting
auch berücksichtig werden sollte, haben wir für diese Teilaufgabe Docker genutzt. Die Applikation kann so
überall laufen gelassen werden, wo Docker installiert ist. Heutzutage ist das eine gängige Art und Weise
etwas auf einem Server laufen zu lassen und bietet dazu auch die Möglichkeit eine Applikation zu skalieren

## REST API Requests
### Crash Info
Die 'Crash Info' API Request ist dazu da den 'impactAngle' (Winkel des Einschlags beim Crash) und den
'offsetMaximumForce' (die Maximalkraft die eingewirkt hat) zurückzugeben.
Die Daten werden als JSON verpackt und zurückgegeben.

Der Python Code dazu sieht folgendermaßen aus:

```Python
# POST request 1 - returns JSON:
# {"impactAngle": degrees, "offsetMaximumForce": millisecond}
@app.route('/api/v1/getCrashInfo', methods=['POST',])
async def crash_info(request):
    ''' crash info parses the crash record and returns a JSON object '''
    log.info("Handling '/api/v1/getCrashInfo'")

    angle, max_force_offset, _, _, _ =
    DataParser().parse_input_data(request.body.decode('utf8'))

    return json({'impactAngle': angle,
                 'offsetMaximumForce': max_force_offset})
```

Es ist eine Asynchrone Methode welche als 'POST' Request markiert ist und die 'api/v1/getCrashInfo' Route nutzt. Die
Annotationen werden von dem 'sanic' Framework bereitgestellt.
Ein Log Eintrag hilft beim analysieren. Die Hauptarbeit wird aber in dem 'DatenParser' gemacht welche alle relevanten
Daten zurückgibt. Die Daten (autoSense JSON) für den 'DataParser' werden mithilfe der Request übergeben. Die letzte Zeile baut ein JSON
Objekt und gibt somit die Antwort der Request an den Sender zurück.

### Crash Image
Die Crash Image Methode gibt ein Bild zurück welches den Einschlag und die Maximale Kraft des Umfalls illustriert.

Der Python Code dazu sieht folgendermassen aus:

```python
# POST request 2 - returns a rendered crash image (PNG)
@app.route('/api/v1/getCrashImage', methods=['POST',])
async def crash_image(request):
    ''' crash image parses the crash record and returns a Image '''
    log.info("Handling '/api/v1/getCrashImage'")

    customOffset = 0
    try:
        customOffset = int(request.args.get('timeOffsetMS'))
    except Exception as e:
        log.error(e)

    log.info("Set customOffset: " + str(customOffset) + "ms")

    angle_impact, max_force, damage_id, crash_time, max_force_offset =
    DataParser().parse_input_data(
                        request.body.decode('utf8'),
                        custom_offset=customOffset)

    d = DamageImage(angle_impact, max_force, damage_id,
                    crash_time, max_force_offset)
    return await file(d.get_image())
```

Die Route der Request ist '/api/v1/getCrashImage'. Ein Offset zum Zeitpunkt des Aufpralls kann übergebene werden
('timeOffsetMS'). Zusätzlich muss wieder das JSON vom autoSense Sensor übergeben werden.
Der 'DatenParser' übernimmt wieder die Hauptaufgabe von dieser Request.
Zusätzlich wir die 'DamageImage' Klasse zum generieren des Bildes verwendet. Anschliessend wird das generierte Bild
zurückgegeben

### Play
Zusätzlich zur gegebenen Aufgabenstellung haben wir noch eine Request eingebaut, welche mehrere Bilder zurückgegeben um
den Unfall genauer zu inspizieren.
Es wird quasi das selbe gemacht wie bei der 'Crash Image' Request. Nur wird eine Liste von Bilder zurückgegeben, welche
dann im Browser dargestellt werden können. Diese Methode ist nicht optimal da alle Bilder zuerst berechnet werden
müssen und nicht gestreamt wird.

## Frontend
Das Frontend ist sehr simple Aufgebaut:

![Frontend Design](img/frontend.png "FrontEnd Design")

Das wichtigste ist die Drag & Drop Zone um ein JSON File von autoSense hochzuladen. Sobald man ein valides JSON
hochgeladen hat werden im Hintergrund die beiden API Requests an das Backend gemacht. Anschliessend wird das Bild und die Daten (Filename, impactAngle & offsetMaximumForce) angezeigt. Optional kann noch der 'customOffset'
eingestellt werden nicht die MaximalKraft sondern einen anderen Zeitpunkt des Aufpralls darzustellen.

Frontend mit hochgeladenem JSON:

![Frontend mit geladenem JSON](img/frontend_loaded.png "FrontEnd mit geladenem JSON")


## Docker
Docker ist ein Tool um Images zu kreieren, welche dann in einem Container ausgeführt werden können. Somit kann eine
Applikation unabhängig vom Betriebssystem ausgeführt werden.
Ausserdem wäre es möglich eine Applikation zu skalieren indem mehrere Container auf verschiedenen Systemen ausgeführt
werden und ein Proxy dazwischen geschaltet wird.

Unser Dockerfile, welches das Image beschreibt, sieht folgendermassen aus:

```bash
FROM python:3.7-slim

#Install libs and tools needed for building python wheels
RUN apt-get update
RUN yes | apt-get install build-essential
RUN yes | apt-get install cmake git libgtk2.0-dev \
          pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN yes | apt-get install python-dev python-numpy libtbb2 libtbb-dev \
          libjpeg-dev libpng-dev

#Install python dependencies
COPY requirements.txt /app/
RUN cd /app && pip install -r requirements.txt

#Copy application to /app
COPY data/* /app/data/
COPY frontend/* /app/frontend/
COPY helper/* /app/helper/
COPY images/* /app/images/
COPY *.py /app/

#Change working directory to /app
WORKDIR /app

#Run server
ENTRYPOINT [ "python", "server.py" ]

```

Unser Basis Image ist ein Python3.7 Image von DockerHub (einer öffentlichen Registry bei der Images hochgeladen werden).
Wir installieren zuerst alle Abhängigkeiten damit die zusätzlichen Python Libraries (wie zum Beispiel numpy) installiert
werden können.
Anschliessend werden die Python Abhängigkeiten installiert bevor schlussendlich alle Files der Applikation in das Image
kopiert werden. Zum Schluss wird die Working Directory (WORKDIR) und der Entrypoint (der Webserver) spezifiziert.
