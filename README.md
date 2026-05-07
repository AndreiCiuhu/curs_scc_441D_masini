# Proiect SCC 441D - Mașini

## Dezvoltator

Ștefan Potîng

## Branch-uri folosite

- `main_poting_stefan`
- `dev_poting_stefan`

## Tema proiectului

Mașini

## Element ales

McLaren

## Funcționalitate adăugată

Am dezvoltat o contribuție individuală pentru marca **McLaren**, în cadrul aplicației Flask a proiectului de grup.

Funcționalitatea adăugată include:

- pagină pentru tema generală: Mașini;
- pagină pentru elementul ales: McLaren;
- rută pentru culoarea mărcii McLaren;
- rută pentru descrierea mărcii McLaren;
- funcții separate în biblioteca aplicației;
- teste unitare pentru funcțiile implementate;
- configurare Docker pentru containerizarea aplicației;
- configurare Jenkins pentru rularea automată a testelor.

## Structura fișierelor adăugate/modificate

```text
app/
├── __init__.py
├── lib/
│   ├── __init__.py
│   └── biblioteca_masini.py
├── routes/
│   ├── __init__.py
│   └── mclaren.py
└── test/
    ├── __init__.py
    └── test_biblioteca_masini.py

Dockerfile
Jenkinsfile
.dockerignore
requirement.txt
masini.py
README.md

## Capturi de ecran

### Testare manuală Flask

Pagina principală:

![Pagina principală Flask](docs/screenshots/01_flask_home.png)

Pagina temei Mașini:

![Pagina Mașini](docs/screenshots/02_flask_masini.png)

Pagina McLaren:

![Pagina McLaren](docs/screenshots/03_flask_mclaren.png)

### Containerizare Docker

Imagine Docker creată:

![Docker images](docs/screenshots/04_docker_images.png)

Container Docker pornit:

![Docker ps](docs/screenshots/05_docker_ps.png)

Loguri container:

![Docker logs](docs/screenshots/06_docker_logs.png)

### Testare cu Jenkins

Rezultat Jenkins SUCCESS:

![Jenkins SUCCESS](docs/screenshots/07_jenkins_success.png)

### Teste unitare locale

Rezultat unittest local:

![Teste unitare locale](docs/screenshots/08_unittest_local.png)

