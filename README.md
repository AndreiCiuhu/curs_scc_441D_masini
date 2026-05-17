# curs_scc_441D_masini
# Proiect SCC - Masini - Renault

## Dezvoltator

Nume: Florin Cernat  
Branch principal: main_Florin_Cernat  
Branch dezvoltare: dev_Florin_Cernat  
Marca aleasa: Renault

---

## Functionalitate adaugata

In cadrul proiectului am adaugat functionalitatea pentru marca Renault.

Au fost implementate:

- doua functii in biblioteca aplicatiei:
  - culoare_renault()
  - descriere_renault()

- rutele cerute pentru aplicatia Flask:
  - /
  - /masini
  - /masini/renault
  - /masini/renault/culoare
  - /masini/renault/descriere

---

## Fisiere modificate sau adaugate

- app/lib/biblioteca_masini.py
- app/lib/__init__.py
- app/routes/renault.py
- app/test/test_biblioteca_masini.py
- masini.py
- Dockerfile
- Jenkinsfile
- .gitignore
- README.md

---

## Functii implementate

### culoare_renault()

Returneaza culorile disponibile pentru marca Renault.

### descriere_renault()

Returneaza o scurta descriere pentru marca Renault.

---

## Rute implementate

| Ruta | Descriere |
|---|---|
| / | Pagina principala |
| /masini | Pagina temei masini |
| /masini/renault | Pagina marcii Renault |
| /masini/renault/culoare | Afiseaza rezultatul functiei culoare_renault() |
| /masini/renault/descriere | Afiseaza rezultatul functiei descriere_renault() |

---

## Stadiul implementarii

- [x] Cod Flask
- [x] Functii biblioteca
- [x] Rute Renault
- [x] Unit teste
- [x] Dockerfile
- [x] Jenkinsfile
- [x] Testare manuala
- [x] Containerizare Docker
- [ ] Testare Jenkins
- [ ] Pull Request
- [ ] Review Pull Request

---

## Testare locala

Aplicatia a fost pornita local folosind comanda:

    python -m flask --app masini.py run --host=0.0.0.0

Au fost testate in browser urmatoarele rute:

    http://127.0.0.1:5000/
    http://127.0.0.1:5000/masini
    http://127.0.0.1:5000/masini/renault
    http://127.0.0.1:5000/masini/renault/culoare
    http://127.0.0.1:5000/masini/renault/descriere

Rezultat: rutele au functionat corect.

---

## Testare unitara

Testele au fost rulate cu:

    PYTHONPATH=. python3 -m unittest app/test/test_biblioteca_masini.py

Rezultat:

    Ran 2 tests

    OK

---

## Containerizare Docker

Imaginea Docker a fost construita cu:

    sudo docker build -t masini-renault-app .

Containerul a fost pornit cu:

    sudo docker run -d -p 5000:5000 --name masini-renault-container masini-renault-app

Containerul a fost verificat cu:

    sudo docker ps

Aplicatia a fost testata in browser la:

    http://127.0.0.1:5000/masini/renault

Rezultat: aplicatia a rulat corect in container Docker.

---

## Jenkinsfile

Fisierul Jenkinsfile contine un pipeline cu urmatoarele etape:

1. Build Docker image
2. Run tests in Docker
3. Run container

Pipeline-ul construieste imaginea Docker, ruleaza testele unitare si porneste aplicatia intr-un container.

---

## Integrare

Pull Request planificat:

    dev_Florin_Cernat -> main_Florin_Cernat

Status PR: in asteptare.

---

## Review PR

PR-uri la care am facut review:

    Momentan nu a fost realizat review-ul.

---

## Ce mai este de facut

- rularea pipeline-ului in Jenkins
- realizarea unui screenshot cu rezultatul Jenkins PASS
- crearea Pull Request-ului
- realizarea unui review pentru un PR al unui coleg
