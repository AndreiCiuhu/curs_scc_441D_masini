# Proiect Mașini – Branch `dev_gavra_dragos`

## Funcționalitatea adăugată

Pe acest branch a fost implementată funcționalitatea pentru mașina **Peugeot**, incluzând:

- **Biblioteca de mașini** (`app/lib/biblioteca_masini.py`) – funcții care returnează culoarea (`albastru`) și descrierea (`Masina puternica`) unui Peugeot.
- **Rutele Peugeot** (`app/routes/peugeot.py`) – Blueprint Flask cu 4 rute:
  - `GET /masini` – pagina generală mașini
  - `GET /masini/peugeot` – pagina dedicată Peugeot
  - `GET /masini/peugeot/culoare` – afișează culoarea mașinii
  - `GET /masini/peugeot/descriere` – afișează descrierea mașinii
- **Rutele de test** (`app/routes/test.py`) – Blueprint cu prefixul `/test`, rute `/test/` și `/test/hello`.
- **Paginile HTML** (`templates/peugeot/`) – șabloane Jinja2 pentru peugeot, culoare și descriere.
- **Aplicația principală** (`masini.py`) – înregistrează blueprint-urile Peugeot și Test în aplicația Flask.

---

## Stadiul implementării

| Component | Status |
| --- | --- |
| Biblioteca mașini (`biblioteca_masini.py`) | Implementat |
| Rutele Peugeot (`peugeot.py`) | Implementat |
| Rutele Test (`test.py`) | Implementat |
| Șabloane HTML Peugeot | Implementate |
| Aplicație Flask (`masini.py`) | Implementată |
| Teste unitare (`test_peugeot.py`) | Implementate |
| Dockerfile | Configurat |
| Jenkinsfile | Configurat |

---

## Testele făcute

### Fișierul de teste

Testele unitare se află în `app/test/test_peugeot.py` și folosesc `unittest`. Sunt acoperite două cazuri:

- `test_culoare` – verifică că funcția `culoare_peugeot()` returnează `"albastru"`
- `test_descriere` – verifică că funcția `descriere_peugeot()` returnează `"Masina puternica"`

### Testare manuală

Pornirea aplicației local:

```bash
pip install -r requirement.txt
python masini.py
```

Verificarea rutelor în browser sau cu `curl`:

```bash
curl http://localhost:5000/masini
curl http://localhost:5000/masini/peugeot
curl http://localhost:5000/masini/peugeot/culoare
curl http://localhost:5000/masini/peugeot/descriere
```

Rularea testelor local:

```bash
pytest app/test/ -v
```

### Testare cu Jenkins

Jenkinsfile-ul configurat conține 3 stagii:

1. **Checkout** – clonează branch-ul `dev_gavra_dragos` din repository.
2. **Build** – construiește imaginea Docker cu tag-ul `masini:${BUILD_NUMBER}`.
3. **Test** – rulează testele pytest în interiorul containerului:
   ```bash
   docker run --rm masini:${BUILD_NUMBER} pytest app/test/ -v
   ```

La finalul pipeline-ului (`post { always }`), imaginea Docker este ștearsă automat.

---

## Containerizarea

Aplicația este containerizată folosind **Docker**:

- **Imagine de bază:** `python:3.13-slim`
- **Port expus:** `5000`
- **Server de producție:** `gunicorn` legat pe `0.0.0.0:5000`

### Construirea imaginii

```bash
docker build -t masini-app .
```

### Rularea aplicației

```bash
docker run -p 5000:5000 masini-app
```

### Rularea testelor în container

```bash
docker run --rm masini-app pytest app/test/ -v
```

---

## Integrarea

- Codul a fost dezvoltat pe branch-ul `dev_gavra_dragos`.
- **Se așteaptă review și aprobare** pentru Pull Request-ul către branch-ul `main`.

---

## Pull Request-uri la care s-a făcut review

| ID PR | Descriere |
| --- | --- |
| – | Nu s-au făcut review-uri la PR-uri externe pe acest branch. |

---

## Fișierul README.md

Acest fișier README a fost adăugat pe branch-ul `dev_gavra_dragos` și documentează funcționalitatea, testele, containerizarea și stadiul integrării pentru mașina Peugeot.