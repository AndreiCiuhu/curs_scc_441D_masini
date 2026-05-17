### Proiect SCC 441D - Masini

#### Dezvoltator

Vlad Alexandru

#### Branch-uri folosite

- main_vlad_alexandru
- dev_vlad_alexandru

#### Tema proiectului

Masini

#### Element ales

Mazda

#### Obiectivul proiectului

Obiectivul proiectului a fost realizarea unei aplicatii web simple in Flask si parcurgerea unui flux complet de dezvoltare software.

In proiect au fost folosite urmatoarele tehnologii si concepte:

- masina virtuala
- Git si GitHub
- Python Flask
- mediu virtual Python
- teste unitare
- Jenkins
- Docker
- Pull Request
- review de la coleg

Scopul principal nu a fost realizarea unei aplicatii complexe, ci folosirea practica a unor unelte intalnite in dezvoltare, testare, integrare si livrare software.

#### Functionalitate adaugata

A fost dezvoltata o aplicatie Flask pentru prezentarea brandului Mazda.

Aplicatia contine trei pagini principale:

- Acasa
- Istoric
- Motorizare

Pagina Acasa afiseaza mesajul:

"Va rog sa apasati pe unul dintre butoane pentru a selecta ce doriti sa aflati despre Mazda"

Pagina Istoric prezinta pe scurt brandul Mazda.

Pagina Motorizare prezinta cateva dintre cele mai importante motoare fabricate de Mazda, cu detalii tehnice scurte.

#### Rute implementate

- /
- /masini
- /masini/mazda
- /masini/mazda/istoric
- /masini/mazda/motorizare

#### Structura proiectului

Fisiere si foldere importante:

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
- docs/images

#### 1. Masina virtuala

Proiectul a fost realizat intr-o masina virtuala Ubuntu, rulata in VirtualBox.

Virtualizarea permite rularea unui sistem de operare separat fata de sistemul principal. In acest caz, Ubuntu a fost folosit ca mediu de lucru pentru Git, Python, Flask, Docker si Jenkins.

Avantajul este faptul ca proiectul ruleaza intr-un mediu Linux separat si controlat.

Comenzi folosite:

```bash
cd ~/Desktop
git clone https://github.com/AndreiCiuhu/curs_scc_441D_masini.git
cd curs_scc_441D_masini
```

#### 2. Git si GitHub

Git a fost folosit pentru versionarea codului.

GitHub a fost folosit pentru gazduirea repository-ului, crearea branch-urilor, crearea Pull Request-ului si realizarea review-ului.

Comenzi folosite pentru clonarea proiectului:

```bash
git clone https://github.com/AndreiCiuhu/curs_scc_441D_masini.git
cd curs_scc_441D_masini
```

Verificarea branch-urilor:

```bash
git branch -a
```

Crearea branch-urilor personale:

```bash
git checkout main
git pull origin main
git checkout -b main_vlad_alexandru
git push -u origin main_vlad_alexandru
git checkout -b dev_vlad_alexandru
git push -u origin dev_vlad_alexandru
```

Branch-ul folosit pentru dezvoltare:

```text
dev_vlad_alexandru
```

Branch-ul folosit pentru integrare:

```text
main_vlad_alexandru
```

Comenzi folosite pentru salvarea modificarilor:

```bash
git add .
git commit -m "Adauga functionalitate Mazda pentru Vlad Alexandru"
git push origin dev_vlad_alexandru
```

#### 3. Aplicatia Flask

Flask este framework-ul Python folosit pentru realizarea aplicatiei web.

Fisierul principal al aplicatiei este:

```text
masini.py
```

Acesta creeaza aplicatia Flask si inregistreaza rutele definite in:

```text
app/routes/test.py
```

Logica pentru informatiile despre Mazda este separata in:

```text
app/lib/biblioteca_masini.py
```

Functiile folosite sunt:

- istoric_mazda()
- motorizari_mazda()

Aceasta separare ajuta la organizarea proiectului. Rutele se ocupa de afisarea paginilor, iar biblioteca se ocupa de informatiile returnate.

#### 4. Interfata HTML si CSS

Pentru afisare au fost adaugate:

```text
templates/page.html
static/style.css
```

Fisierul page.html contine structura paginii.

Fisierul style.css contine stilizarea paginii.

Aplicatia are titlul MAZDA si trei butoane:

- Acasa
- Istoric
- Motorizare

##### Pagina Acasa

![Pagina Acasa](readme_individual/vlad_alexandru/docs/images/browser_home.png)

##### Pagina Istoric

![Pagina Istoric](readme_individual/vlad_alexandru/docs/images/browser_istoric.png)

##### Pagina Motorizare

![Pagina Motorizare](readme_individual/vlad_alexandru/docs/images/browser_motorizare.png)

#### 5. Mediu virtual Python

A fost folosit un mediu virtual Python, numit .venv.

Mediul virtual izoleaza pachetele Python ale proiectului fata de pachetele instalate global in sistem.

Diferenta fata de masina virtuala:

- masina virtuala izoleaza un sistem de operare intreg
- venv izoleaza doar mediul Python al proiectului

Comenzi folosite:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirement.txt
```

Dupa activare, in terminal apare:

```text
(.venv)
```

Dependentele proiectului sunt trecute in:

```text
requirement.txt
```

Dependente folosite:

- flask
- pytest
- pylint
- gunicorn

#### 6. Rulare locala

Aplicatia a fost rulata local cu:

```bash
python masini.py
```

Aplicatia a fost accesata din browser la:

```text
http://127.0.0.1:5000/masini/mazda
```

Au fost verificate urmatoarele rute:

```text
http://127.0.0.1:5000/masini/mazda
http://127.0.0.1:5000/masini/mazda/istoric
http://127.0.0.1:5000/masini/mazda/motorizare
```

Aplicatia a functionat corect local.

##### Dovada rulare pagina Acasa

![Pagina Acasa](readme_individual/vlad_alexandru/docs/images/browser_home.png)

##### Dovada rulare pagina Istoric

![Pagina Istoric](readme_individual/vlad_alexandru/docs/images/browser_istoric.png)

##### Dovada rulare pagina Motorizare

![Pagina Motorizare](readme_individual/vlad_alexandru/docs/images/browser_motorizare.png)

#### 7. Testare automata cu pytest

Pentru testare a fost folosit pytest.

Fisierul de test este:

```text
tests/test_masini.py
```

Testele verifica functiile din:

```text
app/lib/biblioteca_masini.py
```

Comanda folosita:

```bash
python -m pytest
```

Rezultat obtinut:

```text
2 passed
```

Acest rezultat confirma ca testele unitare au trecut.

#### 8. Verificarea codului cu pylint

pylint a fost folosit pentru verificarea calitatii codului Python.

Comanda folosita local:

```bash
python -m pylint --exit-zero app/lib/*.py app/routes/*.py tests/*.py masini.py
```

Optiunea --exit-zero permite ca procesul sa continue chiar daca pylint gaseste avertismente de stil.

In proiect, pylint este inclus si in pipeline-ul Jenkins.

#### 9. Jenkins

Jenkins a fost folosit pentru automatizarea etapelor de build, verificare, testare si deploy.

Fisierul folosit este:

```text
Jenkinsfile
```

Pipeline-ul Jenkins contine urmatoarele etape:

- Build
- Create virtual environment
- pylint - calitate cod
- Unit Testing cu pytest
- Build image
- Deploy

Rolul fiecarei etape:

Build:

- afiseaza locatia proiectului
- listeaza fisierele
- verifica versiunea Python

Create virtual environment:

- creeaza un mediu virtual nou
- instaleaza dependentele din requirement.txt

pylint - calitate cod:

- verifica fisierele Python din proiect
- verifica app/lib, app/routes, tests si masini.py

Unit Testing cu pytest:

- ruleaza testele unitare
- verifica rezultatul testelor

Build image:

- construieste imaginea Docker a aplicatiei

Deploy:

- porneste containerul Docker

Pipeline-ul Jenkins a rulat cu succes.

Toate etapele au status PASS.

##### Dovada Jenkins PASS

![Jenkins PASS](readme_individual/vlad_alexandru/docs/images/jenkins_pass.png)

#### 10. Docker si containerizare

Docker a fost folosit pentru containerizarea aplicatiei.

Containerizarea inseamna impachetarea aplicatiei impreuna cu dependentele necesare pentru rulare.

In proiect au fost create:

```text
Dockerfile
.dockerignore
```

Dockerfile descrie pasii necesari pentru crearea imaginii Docker.

Dockerfile-ul:

- porneste de la o imagine Python
- seteaza folderul de lucru
- copiaza requirement.txt
- instaleaza dependentele
- copiaza fisierele proiectului
- expune portul 5000
- porneste aplicatia Flask

#### 11. Imagine Docker

Imaginea Docker este sablonul aplicatiei.

Ea contine:

- codul aplicatiei
- Python
- dependentele instalate
- comanda de pornire

Comanda folosita pentru construirea imaginii:

```bash
docker build -t masini-vlad-alexandru .
```

Verificarea imaginii:

```bash
docker images
```

In lista de imagini apare:

```text
masini-vlad-alexandru
```

##### Dovada imagine Docker creata

![Imagine Docker](readme_individual/vlad_alexandru/docs/images/docker_images.png)

#### 12. Container Docker

Containerul este instanta pornita a imaginii Docker.

Diferenta:

- imaginea Docker este sablonul
- containerul Docker este aplicatia rulata efectiv

Comanda folosita pentru pornirea containerului:

```bash
docker run --name masini-vlad-alexandru-container -p 5000:5000 masini-vlad-alexandru
```

Portul:

```text
-p 5000:5000
```

inseamna ca portul 5000 din container este legat la portul 5000 al masinii virtuale.

Aplicatia rulata in container a fost accesata la:

```text
http://127.0.0.1:5000/masini/mazda
```

Verificarea containerului pornit:

```bash
docker ps
```

##### Dovada container Docker pornit

![Container Docker](readme_individual/vlad_alexandru/docs/images/docker_ps.png)

#### 13. Consola containerului

In consola containerului au aparut request-uri de tip GET cu status 200.

Exemple:

```text
GET /masini/mazda HTTP/1.1 200
GET /masini/mazda/istoric HTTP/1.1 200
GET /masini/mazda/motorizare HTTP/1.1 200
```

Acest lucru confirma ca browserul a accesat aplicatia rulata in container.

##### Dovada consola containerului

![Consola container](readme_individual/vlad_alexandru/docs/images/container_logs.png)

#### 14. .dockerignore

Fisierul .dockerignore exclude fisierele inutile din imaginea Docker.

Au fost excluse:

- .venv
- .git
- __pycache__
- *.pyc
- .pytest_cache

Rolul acestui fisier este sa pastreze imaginea Docker mai curata si sa nu copieze fisiere generate automat.

#### 15. Pull Request si review

Codul a fost adaugat pe branch-ul:

```text
dev_vlad_alexandru
```

A fost creat Pull Request catre branch-ul:

```text
main_vlad_alexandru
```

Pull Request-ul a primit raspuns si review.

Review-ul confirma ca modificarile au fost verificate de un coleg inainte de integrare.

##### Dovada Pull Request review

![Pull Request review](readme_individual/vlad_alexandru/docs/images/pull_request_review.png)

#### 16. Comenzi utile pentru prezentare

Intrare in proiect:

```bash
cd ~/Desktop/curs_scc_441D_masini
```

Verificare branch:

```bash
git branch
```

Trecere pe branch-ul de dezvoltare:

```bash
git checkout dev_vlad_alexandru
```

Verificare status Git:

```bash
git status
```

Activare mediu virtual:

```bash
source .venv/bin/activate
```

Instalare dependente:

```bash
python -m pip install -r requirement.txt
```

Rulare teste:

```bash
python -m pytest
```

Pornire aplicatie local:

```bash
python masini.py
```

Construire imagine Docker:

```bash
docker build -t masini-vlad-alexandru .
```

Verificare imagine Docker:

```bash
docker images
```

Stergere container vechi:

```bash
docker rm -f masini-vlad-alexandru-container 2>/dev/null || true
```

Pornire container:

```bash
docker run --name masini-vlad-alexandru-container -p 5000:5000 masini-vlad-alexandru
```

Verificare container pornit:

```bash
docker ps
```

Oprire container:

```bash
docker rm -f masini-vlad-alexandru-container
```

#### 17. Stadiu proiect

- functionalitate Mazda adaugata
- interfata HTML si CSS adaugata
- teste unitare adaugate
- testele pytest ruleaza cu succes
- Jenkinsfile creat
- Jenkins rulat cu succes
- Dockerfile creat
- imagine Docker construita
- container Docker pornit
- aplicatie rulata local
- aplicatie rulata in container
- capturi adaugate in README
- Pull Request creat
- review primit