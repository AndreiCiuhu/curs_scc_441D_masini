### Proiect SCC 441D - Mașini

#### Dezvoltator

Pamfir Cosmin

#### Tema proiectului

Skoda

#### Descriere proiect

Acest proiect reprezintă o aplicație web realizată în Flask, având ca scop prezentarea unor informații despre marca Skoda. Aplicația conține pagini dedicate pentru informații generale, descriere și alte detalii despre mașină.

Proiectul folosește Git pentru versionare, Docker pentru containerizare și Jenkins pentru automatizarea etapelor de build, testare și verificare a codului.

#### Tehnologii folosite

- Python
- Flask
- Docker
- Jenkins
- Git / GitHub
- Pytest
- Unittest
- Pylint
- Gunicorn

#### Structura proiectului

- `masini.py` - fișierul principal al aplicației Flask
- `app/routes/` - rutele aplicației
- `app/lib/` - funcțiile folosite în proiect
- `app/test/` - testele automate
- `Dockerfile` - fișierul folosit pentru construirea imaginii Docker
- `Jenkinsfile` - fișierul care definește pipeline-ul Jenkins
- `requirement.txt` - bibliotecile necesare proiectului
- `docs/` - capturi de ecran pentru documentație

#### Rulare locală

Se creează mediul virtual:

```bash
python3 -m venv .venv
```

Se activează mediul virtual:

```bash
source .venv/bin/activate
```

Se instalează dependențele:

```bash
pip install -r requirement.txt
```

Se pornește aplicația:

```bash
python3 masini.py
```

Aplicația poate fi accesată în browser la adresa:

```text
http://127.0.0.1:5000
```

#### Rulare cu Docker

Se construiește imaginea Docker:

```bash
docker build -t masini-skoda-pamfir .
```

Se pornește containerul:

```bash
docker run --name container-skoda-pamfir -p 5000:5000 masini-skoda-pamfir
```

Aplicația poate fi accesată în browser la adresa:

```text
http://127.0.0.1:5000/masini/skoda
```

Pentru verificarea containerului pornit se folosește:

```bash
docker ps
```

#### Testare

Testele automate au fost rulate folosind Pytest:

```bash
PYTHONPATH=. pytest app/test
```

De asemenea, testele au fost rulate și cu Unittest:

```bash
PYTHONPATH=. python3 -m unittest discover -s app/test
```

Rezultatul obținut a fost trecerea cu succes a testelor.

#### Jenkins

Pentru integrare continuă a fost folosit Jenkins. Pipeline-ul conține etape pentru:

- Build;
- verificarea calității codului cu Pylint;
- rularea testelor cu Pytest;
- rularea testelor cu Unittest;
- etapa de Deploy.

Pipeline-ul s-a finalizat cu succes, ceea ce confirmă că proiectul este configurat corect.

#### Capturi de ecran

##### Teste automate rulate cu succes

![Teste automate](readme_individual/pamfir_cosmin/docs/poza1.jpeg)

##### Container Docker pornit

![Docker ps](readme_individual/pamfir_cosmin/docs/poza2.jpeg)

##### Build și rulare Docker

![Docker build si run](readme_individual/pamfir_cosmin/docs/poza3.jpeg)

##### Consolă Jenkins

![Jenkins console](readme_individual/pamfir_cosmin/docs/Jenkins1.png)

##### Pipeline Jenkins finalizat cu succes

![Jenkins pipeline](readme_individual/pamfir_cosmin/docs/Jenkins2.png)

#### Concluzie

Proiectul demonstrează realizarea unei aplicații web simple folosind Flask, gestionarea codului prin Git și GitHub, rularea testelor automate, containerizarea aplicației cu Docker și automatizarea verificărilor prin Jenkins.# curs_scc_441D_masini