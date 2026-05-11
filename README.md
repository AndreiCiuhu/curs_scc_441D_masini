# curs_scc_441D_masini# curs_scc_441D_masini

# Funcționalitate Toyota — Baroiu Silvian

## 1. Descriere generală

În cadrul proiectului Servicii Cloud și Containerizare — grupa 441D — tema Mașini, am avut ca sarcină implementarea funcționalității pentru elementul Toyota.

Implementarea respectă structura agreată la nivel de grup și acoperă rutele Flask, funcțiile din biblioteca aplicației, testele unitare, containerizarea cu Docker și automatizarea prin Jenkins.
---

## 2. Funcționalitate adăugată

Pentru elementul Toyota au fost realizate următoarele:

-implementarea funcțiilor culoare_toyota() și descriere_toyota() în app/lib/biblioteca_masini.py;
-definirea Blueprint-ului Flask în noul fișier app/routes/toyota.py;
-înregistrarea Blueprint-ului în aplicația principală masini.py;
-scrierea testelor unitare în app/test/test_biblioteca_masini.py;
-configurarea Dockerfile pentru containerizarea aplicației;
-configurarea Jenkinsfile pentru rularea automată a pipeline-ului;
-actualizarea documentației în README.md.

---

## 3. Fișiere adăugate sau modificate

- app/lib/biblioteca_masini.py
- app/routes/toyota.py
- app/test/test_biblioteca_masini.py
- masini.py
- Dockerfile
- Jenkinsfile
- requirement.txt
- README.md
- docs/screenshots/

---

---

## Structura implementării

Structura proiectului pentru funcționalitatea **Toyota** este următoarea:

```text
curs_scc_441D_masini/
│
├── masini.py
├── Dockerfile
├── Jenkinsfile
├── README.md
├── requirement.txt
├── .gitignore
│
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── test.py
│   │   ├── toyota.py
|   |   └── masini.py
│   │
│   ├── lib/
│   │   ├── __pycache__.py
│   │   └── biblioteca_masini.py
│   │
│   └── test/
|       ├── __pycache__.py
│       ├── __init__.py
│       └── test_biblioteca_masini.py
│
└── docs/
    └── screenshots/ ************************************************************************
        ├── 00_pornire_locala.png
        ├── 01_testare_unitara.png
        ├── 02_browser_toyota.png
        ├── 03_browser_culoare.png
        ├── 04_browser_descriere.png
        ├── 05_docker_images.png
        ├── 06_docker_ps.png
        ├── 07_browser_container_toyota.png
        ├── 08_docker_logs.png
        ├── 09_jenkins_success.png
        └── 10_blue_ocean_pipeline.png
```

În biblioteca_masini.py se găsesc funcțiile culoare_toyota() și descriere_toyota(), care returnează informațiile specifice mărcii Toyota.
Fișierul toyota.py definește Blueprint-ul și expune următoarele rute:

- /masini
- /masini/toyota
- /masini/toyota/culoare
- /masini/toyota/descriere

Testele unitare sunt grupate în test_biblioteca_masini.py, iar capturile de ecran din docs/screenshots/ documentează vizual fiecare etapă a procesului.
---

## 4. Rute implementate

| Rută | Descriere |
|---|---|
| `/` | Pagina principală a aplicației |
| `/masini` | Pagina temei generale „Mașini” |
| `/masini/toyota` | Pagina principală pentru elementul Toyota|
| `/masini/toyota/model` | Afișează informațiile despre un anumit model returnate de funcția `culoare_toyota()` si de functia `descriere_toyota()` |

---

## 5. Stadiul implementării

| Componentă | Status |
|---|---|
| Cod aplicație | Implementat |
| Funcții în bibliotecă | Implementat |
| Rute Flask | Implementat |
| Teste unitare | Implementat |
| Dockerfile | Configurat |
| Jenkinsfile | Configurat |
| Containerizare | Testată |
| Pipeline Jenkins | Rulat cu succes |
| Documentație | Completată |

---

# Testare

## 6. Testare manuală locală

Aplicația a fost pornită local și rutele Toyota au fost verificate direct din browser.

Comanda de pornire:

```bash
PYTHONPATH=app flask --app masini run
```

În captura următoare se observă pornirea aplicației Flask local, pe portul `5000`.

<img src="docs/screenshots/00_pornire_locala.png" width="900">

Rutele testate manual au fost:

- `http://127.0.0.1:5000/masini/toyota`
- `http://127.0.0.1:5000/masini/toyota/model(gr_supra)`

### Pagina Toyota 
Pagina `/masini/toyota` afișează elementul ales și butoanele către informațiile specifice.

<img src="docs/screenshots/02_browser_toyota.png" width="900">

### Pagina „Model Toyota”

Pagina `/masini/Toyota/gr_supra` afișează rezultatul funcției `descriere_Toyota()`.

<img src="docs/screenshots/03_browser_model.png" width="900">


---

## 7. Testare unitară

Testele unitare au fost implementate în fișierul:

```text
app/test/test_biblioteca_masini.py
```

Comandă de rulare:

```bash
PYTHONPATH=. python -m unittest discover -s app/test
```

Rezultatul obținut a fost `OK`, fiind rulate două teste unitare pentru funcțiile Toyota.

<img src="docs/screenshots/01_testare_unitara.png" width="900">

---

## 8. Containerizare cu Docker

Aplicația a fost containerizată folosind Docker.

Imaginea Docker a fost construită cu comanda:

```bash
sudo docker build -t masini-app .
```

Imaginea Docker `masini-app` a fost creată cu succes și apare în lista imaginilor locale.

<img src="docs/screenshots/05_docker_images.png" width="900">

Containerul a fost pornit astfel:

```bash
sudo docker run -d -p 5000:5000 --name masini-container masini-app
```

Containerul `masini-container` a fost pornit și a expus aplicația pe portul `5000`.

<img src="docs/screenshots/06_docker_ps.png" width="900">

Aplicația rulată în container a fost accesată din browser la ruta:

```text
http://127.0.0.1:5000/masini/Toyota
```

<img src="docs/screenshots/07_browser_container_toyota.png" width="900">

Logurile containerului confirmă cererile HTTP cu status 200 pentru rutele Toyota.

<img src="docs/screenshots/08_docker_logs.png" width="900">

---

## 9. Testare cu Jenkins

Pipeline-ul a fost rulat pe branch-ul:

```text
dev_baroiu_silvian
```

Toate etapele au fost finalizate cu succes, rezultatul final fiind SUCCESS.

<img src="docs/screenshots/09_jenkins_success.png" width="900">

### Vizualizare pipeline în Blue Ocean

În Blue Ocean se observă că toate etapele pipeline-ului au fost executate cu succes:

- `Install dependencies`
- `Run tests`
- `Build image`
- `Deploy`

<img src="docs/screenshots/10_blue_ocean_pipeline.png" width="900">

---

## 10. Fișier Jenkins

Fișierul `Jenkinsfile` definește un pipeline declarativ pentru automatizarea testării și containerizării aplicației.

Etapele pipeline-ului sunt:

| Stage | Rol |
|---|---|
| `Install dependencies` | Creează mediul Python și instalează dependențele din `requirement.txt` |
| `Run tests` | Rulează testele unitare din `app/test` |
| `Build image` | Construiește imaginea Docker `masini-app` |
| `Deploy` | Pornește containerul `masini-container` |

---

## 11. Integrare GitHub

Dezvoltarea a avut loc pe branch-ul:

```text
dev_baroiu_silvian
```

Integrarea se va face printr-un Pull Request către:

```text
main_baroiu_silvian
```

Fluxul de lucru:

```text
dev_baroiu_silvian -> main_baroiu_silvian
```

Status:
Pull Request-ul va fi trimis spre review utilizatorului:

```text
@Varlam-Cosmin
```

Review-ul este reciproc — colegul va verifica funcționalitatea Toyota implementată de mine, iar eu voi revizui Pull Request-ul său.

Status integrare:

```text
În așteptare review și aprobare.
În așteptare creare Pull Request, review și aprobare.
```

---