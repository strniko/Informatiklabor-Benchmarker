# Benutzeranleitung für meinen Benchmarker

## 1. Voraussetzungen
Für die Ausführung meines Benchmarkers werden folgende Komponenten benötigt:

- Python: Version 3.12 oder höher (Siehe Schritt 2)
- pandas: Version 3.1.1 oder höher (Siehe Schritt 2)
- Java Runtime Environment
- Ausführbare JAR-Datei des Informatiklabors

Java muss über den Befehl `java` aus der Kommandozeile erreichbar sein. Die Python-Abhängigkeit pandas wird zur Verarbeitung und Speicherung der Messergebnisse benötigt.

## 2. Installation und Vorbereitung
Zunächst muss das Repository heruntergeladen werden:
```bash
git clone https://github.com/strniko/Informatiklabor-Benchmarker.git
cd Informatiklabor-Benchmarker
```
Anschließend empfiehlt sich die Einrichtung einer isolierten Python-Umgebung mit [uv](https://docs.astral.sh/uv/), da so direkt die korrekten Python und pandas versionen installiert werden:
```bash
uv sync
source .venv/bin/activate
```
Außerdem wird die ausführbare JAR-Datei des zu untersuchenden Programms benötigt. Diese muss lokal auf dem Rechner vorhanden sein.

## 3. Ausführung des Benchmarks
Der Benchmarker wird über die Kommandozeile gestartet.

Die Syntax wird mit `python main.py --help` ausgegeben.


### Beispiel
Ein vollständiger Aufruf mit 32 Workern und einem separaten Ausgabeverzeichnis sieht folgendermaßen aus:
```bash
python main.py beispiel@unibas.ch Simulation.jar \
    --workers 32 \
    --out_dir ./CSVs
```

### Ablauf einer Benchmark-Ausführung
Nach dem Start führt das Programm folgende Schritte aus:
1.  Initialisierung des Benchmarkers mit der angegebenen E-Mail-Adresse und der JAR-Datei.
2.  Erstellung eines Thread-Pools mit der angegebenen Anzahl an Workern.    
3.  Durchführung der Messungen für Algorithmus 1 insgesamt dreimal.
4.  Durchführung derselben Messungen für Algorithmus 2, ebenfalls dreimal.  
5.  Speicherung der Ergebnisse jedes Durchlaufs in einer eigenen CSV-Datei.
    
**Hinweis:** Die Reihenfolge der Zeilen entspricht der Reihenfolge, in der die parallelen Aufgaben abgeschlossen wurden. Sie ist daher nicht notwendigerweise aufsteigend nach dem Eingabewert sortiert.