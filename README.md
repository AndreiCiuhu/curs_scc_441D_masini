# Proiect SCC 441D - Masini

## Dezvoltator

Vlad Alexandru

## Branch-uri folosite

- main_vlad_alexandru
- dev_vlad_alexandru

## Tema proiectului

Masini

## Element ales

Mazda

## Functionalitate adaugata

A fost dezvoltata o aplicatie Flask pentru prezentarea brandului Mazda.

Aplicatia contine trei pagini principale:

- Acasa
- Istoric
- Motorizare

Pagina Acasa afiseaza mesajul:
"Va rog sa apasati pe unul dintre butoane pentru a selecta ce doriti sa aflati despre Mazda"

Pagina Istoric prezinta pe scurt brandul Mazda.

Pagina Motorizare prezinta cateva dintre cele mai importante motoare fabricate de Mazda.

## Rute implementate

- /
- /masini
- /masini/mazda
- /masini/mazda/istoric
- /masini/mazda/motorizare

## Fisiere adaugate sau modificate

- masini.py
- app/routes/test.py
- app/lib/biblioteca_masini.py
- templates/page.html
- static/style.css
- tests/test_masini.py
- Jenkinsfile
- Dockerfile
- .dockerignore
- requirement.txt
- README.md

## Testare manuala

Aplicatia a fost rulata local cu:

python masini.py

Au fost verificate in browser urmatoarele rute:

http://127.0.0.1:5000/masini/mazda
http://127.0.0.1:5000/masini/mazda/istoric
http://127.0.0.1:5000/masini/mazda/motorizare

## Testare automata

Testele unitare au fost rulate cu pytest:

python -m pytest

Rezultat obtinut:

2 passed

## Jenkins

A fost creat fisierul Jenkinsfile.

Pipeline-ul contine urmatoarele etape:

- Build
- Create virtual environment
- pylint - calitate cod
- Unit Testing cu pytest
- Deploy

Testele unitare sunt rulate automat cu pytest.

## Docker

A fost creat fisierul Dockerfile pentru containerizarea aplicatiei.

Imaginea Docker a fost construita cu:

docker build -t masini-vlad-alexandru .

Containerul a fost pornit cu:

docker run --name masini-vlad-alexandru-container -p 5000:5000 masini-vlad-alexandru

Aplicatia rulata in container a fost accesata din browser la:

http://127.0.0.1:5000/masini/mazda

## Capturi de ecran

### Imagine Docker creata

![Imagine Docker](docs/images/docker_images.png)

### Container Docker pornit

![Container Docker](docs/images/docker_ps.png)

### Pagina Acasa

![Pagina Acasa](docs/images/browser_home.png)

### Pagina Istoric

![Pagina Istoric](docs/images/browser_istoric.png)

### Pagina Motorizare

![Pagina Motorizare](docs/images/browser_motorizare.png)

### Consola containerului

![Consola container](docs/images/container_logs.png)

## Integrare

Codul a fost adaugat pe branch-ul:

dev_vlad_alexandru

Urmatorul pas este crearea unui Pull Request catre:

main_vlad_alexandru

## Review

Pull Request-ul trebuie verificat de minim un coleg.

## Stadiu proiect

- functionalitate adaugata
- teste unitare adaugate
- Jenkinsfile creat
- Dockerfile creat
- aplicatie rulata local
- aplicatie rulata in container
- capturi adaugate in README

## Ce mai este de facut

- commit si push pe branch-ul dev_vlad_alexandru
- creare Pull Request catre main_vlad_alexandru
- rulare Jenkins
- atasare rezultat Jenkins in Pull Request
- obtinere review de la un coleg
