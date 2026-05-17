### Proiect SCC - Masini - Honda

#### Informatii student

- **Nume:** Anton Darius
- **Grupa:** 441D
- **Cont GitHub:** AntonDarius921
- **Tema proiectului:** Masini
- **Marca aleasa:** Honda
- **Repository:** curs_scc_441D_masini
- **Branch de dezvoltare:** dev_anton_darius
- **Branch personal principal:** main_anton_darius

---

#### Descriere proiect

Acest proiect face parte din activitatea de la disciplina **Servicii Cloud si Containerizare**.

Scopul proiectului este realizarea unei aplicatii web simple in Flask si utilizarea unor unelte folosite frecvent in dezvoltarea software, precum:

- Git si GitHub;
- branch-uri personale de dezvoltare;
- Pull Request-uri;
- Jenkins pentru testare automata;
- Docker pentru containerizarea aplicatiei;
- documentare prin fisierul README.md.

Pentru grupa **441D**, tema proiectului este **Masini**.

In cadrul acestui proiect, am ales marca **Honda** si am implementat trei pagini web dedicate acesteia.

---

#### Functionalitate adaugata

Pentru marca Honda au fost create urmatoarele pagini:

| Pagina | Ruta |
|---|---|
| Pagina principala Honda | `/masini/honda/` |
| Istoric Honda | `/masini/honda/istoric` |
| Modele Honda | `/masini/honda/modele` |

Paginile contin informatii despre marca Honda, istoricul acesteia si cateva modele reprezentative.

---

#### Rute implementate

##### 1. Pagina principala Honda

```text
/masini/honda/
```

Aceasta pagina prezinta marca Honda si cateva caracteristici generale, precum fiabilitatea, eficienta si modelele populare.

##### 2. Pagina Istoric Honda

```text
/masini/honda/istoric
```

Aceasta pagina contine informatii despre aparitia si evolutia marcii Honda.

##### 3. Pagina Modele Honda

```text
/masini/honda/modele
```

Aceasta pagina prezinta cateva modele cunoscute Honda, precum Civic, Accord si CR-V.

---

#### Fisiere adaugate/modificate

Pentru implementarea functionalitatii Honda au fost adaugate sau modificate urmatoarele fisiere:

```text
masini.py
app/__init__.py
app/lib/__init__.py
app/lib/biblioteca_masini.py
app/routes/__init__.py
app/routes/honda.py
app/test/__init__.py
app/test/test_honda.py
Dockerfile
Jenkinsfile
.gitignore
README.md
```

---

#### Structura implementarii

```text
curs_scc_441D_masini/
│
├── masini.py
├── Dockerfile
├── Jenkinsfile
├── README.md
├── .gitignore
│
├── app/
│   ├── __init__.py
│   │
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_masini.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── honda.py
│   │
│   └── test/
│       ├── __init__.py
│       └── test_honda.py
│
└── docs/
    └── images/
        ├── docker_images.png
        ├── docker_ps.png
        ├── docker_logs.png
        ├── browser_honda_home.png
        ├── browser_honda_istoric.png
        ├── browser_honda_modele.png
        └── jenkins_success.png
```

---

#### Implementare Flask

Aplicatia Flask este pornita din fisierul:

```text
masini.py
```

In acest fisier a fost inregistrat blueprint-ul pentru Honda:

```python
from app.routes.honda import honda_bp

app.register_blueprint(honda_bp)
```

Rutele pentru Honda sunt definite in fisierul:

```text
app/routes/honda.py
```

Functiile care returneaza informatiile despre Honda sunt definite in:

```text
app/lib/biblioteca_masini.py
```

---

#### Testare locala

Pentru testarea rutelor Honda a fost creat fisierul:

```text
app/test/test_honda.py
```

Testele verifica daca paginile Honda raspund corect cu status code `200`.

Comanda folosita pentru rularea testelor:

```bash
python3 -m unittest discover -s app/test -p "test_*.py"
```

Rezultat obtinut:

```text
Ran 3 tests in 0.007s

OK
```

---

#### Rulare locala

Pentru rularea aplicatiei local, se foloseste comanda:

```bash
python3 masini.py
```

Aplicatia poate fi accesata in browser la:

```text
http://localhost:5000/masini/honda/
```

Pagini disponibile:

```text
http://localhost:5000/masini/honda/
http://localhost:5000/masini/honda/istoric
http://localhost:5000/masini/honda/modele
```

---

#### Jenkins

A fost adaugat fisierul:

```text
Jenkinsfile
```

Acesta creeaza un mediu virtual Python, instaleaza dependinta Flask si ruleaza testele unitare.

Branch folosit pentru Jenkins:

```text
dev_anton_darius
```

Branch specifier folosit in Jenkins:

```text
*/dev_anton_darius
```

Comanda rulata de Jenkins pentru teste:

```bash
venv/bin/python -m unittest discover -s app/test -p "test_*.py"
```

Rezultat Jenkins:

```text
Ran 3 tests

OK

Finished: SUCCESS
```

Pipeline-ul Jenkins a fost rulat cu succes, iar testele unitare au trecut.

---

#### Docker

Pentru containerizarea aplicatiei a fost adaugat fisierul:

```text
Dockerfile
```

Imaginea Docker a fost construita cu:

```bash
sudo docker build -t masini-honda-anton-darius .
```

Containerul a fost pornit cu:

```bash
sudo docker run -d --name masini-honda-container -p 5000:5000 masini-honda-anton-darius
```

Containerul a fost verificat cu:

```bash
sudo docker ps
```

Aplicatia rulata in container a fost accesata in browser la:

```text
http://localhost:5000/masini/honda/
```

Logurile containerului au fost verificate cu:

```bash
sudo docker logs masini-honda-container
```

In loguri apar request-uri de forma:

```text
GET /masini/honda/ HTTP/1.1" 200
GET /masini/honda/istoric HTTP/1.1" 200
GET /masini/honda/modele HTTP/1.1" 200
```

Acest lucru confirma ca paginile Honda pot fi accesate din browser prin containerul Docker.

---

#### Capturi de ecran

##### Imagine Docker

![Imagine Docker](documentatie_generata/anton_darius/docs/images/docker_images.png)

##### Container Docker pornit

![Container Docker](documentatie_generata/anton_darius/docs/images/docker_ps.png)

##### Pagina principala Honda

![Pagina Honda](documentatie_generata/anton_darius/docs/images/browser_honda_home.png)

##### Pagina Istoric Honda

![Istoric Honda](documentatie_generata/anton_darius/docs/images/browser_honda_istoric.png)

##### Pagina Modele Honda

![Modele Honda](documentatie_generata/anton_darius/docs/images/browser_honda_modele.png)

##### Loguri Docker

![Loguri Docker](documentatie_generata/anton_darius/docs/images/docker_logs.png)

##### Jenkins - teste rulate cu succes

![Jenkins Success](documentatie_generata/anton_darius/docs/images/jenkins_success.png)

---

#### Git si GitHub

Modificarile au fost realizate pe branch-ul personal de dezvoltare:

```text
dev_anton_darius
```

Pentru salvarea modificarilor au fost folosite comenzile:

```bash
git add .
git commit -m "Adauga functionalitate Honda"
git push origin dev_anton_darius
```

Urmeaza crearea unui Pull Request din:

```text
dev_anton_darius
```

catre:

```text
main_anton_darius
```

---

#### Pull Request

Pull Request-ul va fi creat pentru integrarea modificarilor din branch-ul de dezvoltare in branch-ul personal principal.

```text
Sursa: dev_anton_darius
Destinatie: main_anton_darius
```

Status:

```text
Urmeaza creare PR si review.
```

---

#### Status proiect

| Cerinta | Status |
|---|---|
| Functionalitate Honda | Finalizat |
| Pagina principala Honda | Finalizat |
| Pagina Istoric Honda | Finalizat |
| Pagina Modele Honda | Finalizat |
| Teste unitare | Finalizat |
| Rulare locala | Finalizat |
| Jenkinsfile | Finalizat |
| Rulare Jenkins | Finalizat |
| Dockerfile | Finalizat |
| Imagine Docker | Finalizat |
| Container Docker | Finalizat |
| Accesare aplicatie din container | Finalizat |
| Loguri Docker | Finalizat |
| Capturi de ecran | Finalizat |
| Documentatie README | Finalizat |
| Pull Request | Urmeaza |

---

#### Concluzii

In cadrul proiectului am implementat functionalitatea pentru marca **Honda** in aplicatia Flask a grupei 441D.

Au fost adaugate trei pagini web, teste unitare pentru verificarea rutelor, fisier Jenkinsfile pentru testare automata si Dockerfile pentru containerizarea aplicatiei.

Aplicatia ruleaza local si in container Docker, iar paginile Honda pot fi accesate din browser.

Testele unitare au fost rulate cu succes local si prin Jenkins.