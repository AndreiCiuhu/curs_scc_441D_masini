# curs_scc_441D_masini

# Funcționalitate Bentley — Ispas Ariana-Elena

## 1. Descriere generală

În cadrul proiectului **Servicii Cloud și Containerizare — grupa 441D — tema Mașini**, am implementat funcționalitatea aferentă elementului **Bentley**.

Funcționalitatea dezvoltată respectă structura proiectului de grup și include rute Flask, funcții dedicate în biblioteca aplicației, teste unitare, containerizare cu Docker și rulare automată prin Jenkins.

---

## 2. Funcționalitate adăugată

Funcționalitatea Bentley este compusă din:

- definirea funcțiilor `culoare_bentley()` și `descriere_bentley()` în fișierul `app/lib/biblioteca_masini.py`;
- crearea fișierului `app/routes/bentley.py`, care conține Blueprint-ul pentru rutele Bentley;
- înregistrarea Blueprint-ului Bentley în aplicația principală `masini.py`;
- adăugarea testelor unitare în `app/test/test_biblioteca_masini.py`;
- configurarea fișierului `Dockerfile` pentru containerizarea aplicației;
- configurarea fișierului `Jenkinsfile` pentru rularea pipeline-ului Jenkins;
- completarea documentației în fișierul `README.md`.

---

## 3. Fișiere adăugate sau modificate

- `app/lib/biblioteca_masini.py`
- `app/routes/bentley.py`
- `app/test/test_biblioteca_masini.py`
- `masini.py`
- `Dockerfile`
- `Jenkinsfile`
- `requirement.txt`
- `README.md`
- `docs/screenshots/`

---

## Structura implementării

Structura proiectului pentru funcționalitatea **Bentley** este următoarea:

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
│   │   └── bentley.py
│   │
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_masini.py
│   │
│   └── test/
│       ├── __init__.py
│       └── test_biblioteca_masini.py
│
└── docs/
    └── screenshots/
        ├── 00_pornire_locala.png
        ├── 01_testare_unitara.png
        ├── 02_browser_bentley.png
        ├── 03_browser_culoare.png
        ├── 04_browser_descriere.png
        ├── 05_docker_images.png
        ├── 06_docker_ps.png
        ├── 07_browser_container_bentley.png
        ├── 08_docker_logs.png
        ├── 09_jenkins_success.png
        └── 10_blue_ocean_pipeline.png
```

Fișierul `biblioteca_masini.py` conține funcțiile specifice elementului Bentley, respectiv `culoare_bentley()` și `descriere_bentley()`.

Fișierul `bentley.py` definește Blueprint-ul și rutele Flask aferente paginilor Bentley:

- `/masini`
- `/masini/bentley`
- `/masini/bentley/culoare`
- `/masini/bentley/descriere`

Fișierul `test_biblioteca_masini.py` conține testele unitare pentru funcțiile implementate în bibliotecă.

Folderul `docs/screenshots/` conține capturile utilizate în documentație pentru testarea manuală, testarea unitară, containerizarea cu Docker și rularea pipeline-ului Jenkins.

---

## 4. Rute implementate

| Rută | Descriere |
|---|---|
| `/` | Pagina principală a aplicației |
| `/masini` | Pagina temei generale „Mașini” |
| `/masini/bentley` | Pagina principală pentru elementul Bentley |
| `/masini/bentley/culoare` | Afișează informațiile returnate de funcția `culoare_bentley()` |
| `/masini/bentley/descriere` | Afișează informațiile returnate de funcția `descriere_bentley()` |

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

Aplicația a fost pornită local, iar rutele aferente funcționalității Bentley au fost accesate din browser.

Comanda folosită pentru pornirea aplicației:

```bash
PYTHONPATH=app flask --app masini run
```

În captura următoare se observă pornirea aplicației Flask local, pe portul `5000`.

<img src="docs/screenshots/00_pornire_locala.png" width="900">

Rutele testate manual au fost:

- `http://127.0.0.1:5000/masini/bentley`
- `http://127.0.0.1:5000/masini/bentley/culoare`
- `http://127.0.0.1:5000/masini/bentley/descriere`

### Pagina Bentley

Pagina `/masini/bentley` afișează elementul ales și butoanele către informațiile specifice.

<img src="docs/screenshots/02_browser_bentley.png" width="900">

### Pagina „Culoare Bentley”

Pagina `/masini/bentley/culoare` afișează rezultatul funcției `culoare_bentley()`.

<img src="docs/screenshots/03_browser_culoare.png" width="900">

### Pagina „Descriere Bentley”

Pagina `/masini/bentley/descriere` afișează rezultatul funcției `descriere_bentley()`.

<img src="docs/screenshots/04_browser_descriere.png" width="900">

---

## 7. Testare unitară

Testele unitare au fost implementate în fișierul:

```text
app/test/test_biblioteca_masini.py
```

Comanda folosită pentru rularea testelor unitare:

```bash
PYTHONPATH=. python -m unittest discover -s app/test
```

Rezultatul obținut a fost `OK`, fiind rulate două teste unitare pentru funcțiile Bentley.

<img src="docs/screenshots/01_testare_unitara.png" width="900">

---

## 8. Containerizare cu Docker

Aplicația a fost containerizată folosind Docker.

Comanda folosită pentru construirea imaginii Docker:

```bash
sudo docker build -t masini-app .
```

Imaginea Docker `masini-app` a fost creată cu succes și apare în lista imaginilor locale.

<img src="docs/screenshots/05_docker_images.png" width="900">

Containerul a fost pornit cu următoarea comandă:

```bash
sudo docker run -d -p 5000:5000 --name masini-container masini-app
```

Containerul `masini-container` a fost pornit și a expus aplicația pe portul `5000`.

<img src="docs/screenshots/06_docker_ps.png" width="900">

Aplicația rulată în container a fost accesată din browser la ruta:

```text
http://127.0.0.1:5000/masini/bentley
```

<img src="docs/screenshots/07_browser_container_bentley.png" width="900">

Logurile containerului confirmă accesarea rutelor Bentley din browser cu status HTTP `200`.

<img src="docs/screenshots/08_docker_logs.png" width="900">

---

## 9. Testare cu Jenkins

Testarea automată a fost realizată cu Jenkins, pe branch-ul:

```text
dev_ispas_ariana
```

Pipeline-ul Jenkins a rulat cu succes și a folosit fișierul `Jenkinsfile` din repository.

Rezultatul rulării a fost `SUCCESS`.

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

Codul a fost dezvoltat pe branch-ul personal de dezvoltare:

```text
dev_ispas_ariana
```

Integrarea se va realiza prin Pull Request către branch-ul personal principal:

```text
main_ispas_ariana
```

Fluxul de integrare respectat este:

```text
dev_ispas_ariana -> main_ispas_ariana
```

După crearea Pull Request-ului, acesta va fi trimis spre review colegului:

```text
@AntonDarius921
```

Review-ul a fost stabilit în mod reciproc: colegul va verifica implementarea mea pentru funcționalitatea **Bentley**, iar eu voi verifica Pull Request-ul realizat de acesta.

Status integrare:

```text
În așteptare creare Pull Request, review și aprobare.
```

---

## 12. Review-uri planificate și efectuate

Pentru respectarea cerinței de lucru colaborativ, a fost stabilit un review reciproc cu utilizatorul GitHub:

```text
@AntonDarius921
```

După crearea Pull Request-urilor, vor fi realizate următoarele acțiuni:

- @AntonDarius921 va realiza review pentru Pull Request-ul meu: `dev_ispas_ariana -> main_ispas_ariana`;
- eu voi realiza review pentru Pull Request-ul colegului @AntonDarius921;
- după verificare și aprobare, modificările vor putea fi integrate în branch-ul personal principal.

Status review:

```text
Review reciproc stabilit, în așteptare creare Pull Request-uri.
```


## 13. Ce mai este de făcut

- Obținerea unui review de la un coleg;
- Efectuarea unui review pentru Pull Request-ul unui coleg;
- Integrarea modificărilor după aprobare.
