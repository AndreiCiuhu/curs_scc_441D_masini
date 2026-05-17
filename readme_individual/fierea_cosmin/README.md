### curs_scc_441D_masini

### Implementare Porsche — Fierea Cosmin

#### 1. Date proiect

- Student: Fierea Cosmin
- Grupa: 441D
- Tema proiectului: Mașini
- Element ales: Porsche
- Branch dezvoltare: `dev_fierea_cosmin`
- Branch personal principal: `main_fierea_cosmin`

---

#### 2. Prezentare generală

În cadrul proiectului am ales marca **Porsche** și am implementat o secțiune web dedicată acesteia în aplicația Flask a grupei.

Partea mea din proiect conține:

- pagină principală pentru Porsche;
- pagină cu modele Porsche;
- pagină cu istoria modelului Porsche 911;
- funcții separate în biblioteca aplicației;
- teste unitare;
- configurare Docker;
- configurare Jenkins;
- documentație cu pașii de rulare și testare.

Aplicația are o interfață simplă, fără design încărcat, pentru ca informațiile să fie ușor de urmărit.

---

#### 3. Funcționalități implementate

Activarea mediului virtual Python

```bash
    source venv/bin/activate
```

Funcționalitățile pentru Porsche sunt definite în fișierul:

`app/lib/biblioteca_masini.py`

Au fost implementate următoarele funcții:

##### 3.1 `descriere_porsche()`

Această funcție returnează o scurtă descriere generală a mărcii Porsche.

Descrierea este afișată pe pagina principală Porsche.

---

##### 3.2 `modele_porsche()`

Această funcție returnează o listă de modele Porsche.

Pentru fiecare model sunt afișate informații precum:

- marca;
- modelul;
- anul;
- categoria;
- motorul;
- puterea;
- tracțiunea;
- combustibilul.

Modelele incluse în aplicație sunt:

- Porsche 911;
- Porsche Cayenne;
- Porsche Taycan.

---

##### 3.3 `istorie_porsche_911()`

Această funcție returnează informații despre mai multe generații importante ale modelului Porsche 911.

Pentru fiecare generație sunt afișate:

- numele generației;
- perioada;
- o descriere scurtă.

---

#### 4. Rute implementate

| Rută | Descriere |
|---|---|
| `/` | Default |
| `/masini` | Redirecționează către pagina Porsche |
| `/masini/porsche/` | Pagina principală Porsche |
| `/masini/porsche/modele` | Pagina cu modelele Porsche |
| `/masini/porsche/istorie-911` | Pagina cu istoria modelului Porsche 911 |

---

#### 5. Fișiere adăugate sau modificate

Pentru implementarea funcționalității Porsche au fost adăugate sau modificate următoarele fișiere:

- `masini.py`
- `app/lib/__init__.py`
- `app/lib/biblioteca_masini.py`
- `app/routes/porsche.py`
- `app/test/test_porsche_fierea_cosmin.py`
- `Dockerfile`
- `Jenkinsfile`
- `.dockerignore`
- `README.md`
- `docs/poze_readme/`

---

### Testare aplicație

#### 6. Testare locală

Testele unitare au fost create în fișierul:

`app/test/test_porsche_fierea_cosmin.py`

Comanda folosită pentru rularea testelor:

```bash
PYTHONPATH=app python3 -m unittest discover -s app/test
```

Rezultatul obținut:

```text
Ran 5 tests

OK
```

Testele verifică:

- funcția `modele_porsche()`;
- funcția `istorie_porsche_911()`;
- ruta `/masini/porsche/`;
- ruta `/masini/porsche/modele`;
- ruta `/masini/porsche/istorie-911`.

##### Captură testare locală

![Teste unitare Porsche](readme_individual/fierea_cosmin/docs/poze_readme/teste_unitare.png)

---

#### 7. Rulare locală a aplicației

Aplicația se pornește local cu următoarea comandă:

```bash
PYTHONPATH=app python3 masini.py
```

După pornire, aplicația rulează pe portul `5000`.

Rutele verificate manual au fost:

```text
http://127.0.0.1:5000/masini/porsche/
http://127.0.0.1:5000/masini/porsche/modele
http://127.0.0.1:5000/masini/porsche/istorie-911
```

##### Pagina principală Porsche

![Pagina Porsche](readme_individual/fierea_cosmin/docs/poze_readme/pagina_porsche.png)

##### Pagina Modele Porsche

![Pagina Modele Porsche](readme_individual/fierea_cosmin/docs/poze_readme/pagina_modele_porsche.png)

##### Pagina Istoria Porsche 911

![Pagina Istoria Porsche 911](readme_individual/fierea_cosmin/docs/poze_readme/pagina_istorie_911.png)

---

### Docker

#### 8. Crearea fișierului Dockerfile

Pentru containerizarea aplicației a fost creat fișierul:

`Dockerfile`

Acesta definește pașii necesari pentru rularea aplicației Flask într-un container Docker.

Fișierul Dockerfile:

- folosește o imagine Python;
- setează directorul de lucru în container;
- copiază fișierul `requirement.txt`;
- instalează dependențele;
- copiază codul aplicației;
- expune portul `5000`;
- pornește aplicația cu `python3 masini.py`.

A fost creat și fișierul:

`.dockerignore`

pentru a evita copierea fișierelor inutile în imaginea Docker.

---

#### 9. Construirea imaginii Docker

Pentru construirea imaginii Docker a fost folosită comanda:

```bash
sudo docker build -t masini-porsche-fierea .
```

În timpul construirii imaginii, Docker descarcă imaginea de bază Python și execută pașii definiți în `Dockerfile`.

##### Începerea construirii imaginii Docker

![Docker build start](readme_individual/fierea_cosmin/docs/poze_readme/docker_build_start.png)

##### Imagine Docker construită cu succes

![Docker build success](readme_individual/fierea_cosmin/docs/poze_readme/docker_build_success.png)

La finalul procesului apare mesajul:

```text
Successfully built
Successfully tagged masini-porsche-fierea:latest
```

Acest mesaj confirmă faptul că imaginea Docker a fost creată corect.

---

#### 10. Verificarea imaginii Docker

Pentru verificarea imaginilor Docker existente s-a folosit comanda:

```bash
sudo docker images
```

În listă apare imaginea:

```text
masini-porsche-fierea
```

##### Captură imagine Docker

![Imagine Docker](readme_individual/fierea_cosmin/docs/poze_readme/docker_images.png)

---

#### 11. Rularea containerului Docker

Containerul Docker a fost pornit cu următoarea comandă:

```bash
sudo docker run -d -p 5000:5000 --name masini-porsche-container masini-porsche-fierea
```

Pentru verificarea containerului pornit s-a folosit comanda:

```bash
sudo docker ps
```

Containerul `masini-porsche-container` a rulat cu succes și a expus aplicația pe portul `5000`.

##### Captură container pornit

![Container Docker pornit](readme_individual/fierea_cosmin/docs/poze_readme/docker_ps.png)

---
####12. Accesarea aplicației din container și verificarea log-urilor

După pornirea containerului, aplicația a fost accesată în browser la adresa:

```bash
    http://127.0.0.1:5000/masini/porsche/
```

 Au fost verificate și paginile:

```bash
    http://127.0.0.1:5000/masini/porsche/modele
    http://127.0.0.1:5000/masini/porsche/istorie-911
```

##### Captură aplicație rulată din container

![Aplicație rulată din container](readme_individual/fierea_cosmin/docs/poze_readme/docker_browser.png)

Pentru verificarea accesării aplicației din container s-a folosit comanda:

```bash
    sudo docker logs masini-porsche-container
```

Această comandă afișează log-urile containerului și arată cererile HTTP făcute din browser către aplicația Flask.

---

#### 13. Oprirea containerului Docker

După testare, containerul a fost oprit cu:

```bash
sudo docker stop masini-porsche-container
```

Apoi containerul a fost șters cu:

```bash
sudo docker rm masini-porsche-container
```

Pentru verificare s-a folosit:

```bash
sudo docker ps
```

După oprire și ștergere, containerul nu mai apare în lista containerelor active.

---

### Jenkins

#### 14. Testare automată cu Jenkins

Pornirea Jenkins

```bash
    sudo systemctl start jenkins
```

Verificarea statusului Jenkins

```bash
    sudo systemctl status jenkins
```

Pentru automatizarea testării a fost creat fișierul:

`Jenkinsfile`

Pipeline-ul Jenkins a fost configurat pe branch-ul:

`dev_fierea_cosmin`

Pipeline-ul conține următoarele etape:

| Etapă | Rol |
|---|---|
| `Checkout SCM` | Preia codul din repository |
| `Install dependencies` | Creează mediul virtual și instalează dependențele |
| `Run unit tests` | Rulează testele unitare |
| `Build Docker image` | Construiește imaginea Docker |

Pipeline-ul a rulat cu succes, iar toate etapele au fost finalizate fără erori.

##### Captură Jenkins

![Jenkins SUCCESS](readme_individual/fierea_cosmin/docs/poze_readme/jenkins_success.png)

##### Pipeline Jenkins

![Jenkins Pipeline](readme_individual/fierea_cosmin/docs/poze_readme/jenkins_pipeline.png)

---

### Integrare GitHub

#### 15. Branch-uri folosite

Codul a fost dezvoltat pe branch-ul:

```text
dev_fierea_cosmin
```

Branch-ul personal principal este:

```text
main_fierea_cosmin
```

Fluxul de integrare este:

```text
dev_fierea_cosmin -> main_fierea_cosmin
```

După aprobarea Pull Request-ului, modificările pot fi integrate mai departe în branch-ul principal al grupei.

---

#### 16. Pull Request

Pull Request-ul va fi creat din:

```text
dev_fierea_cosmin
```

către:

```text
main_fierea_cosmin
```

##### Captură Pull Request
![Pull Request](readme_individual/fierea_cosmin/docs/poze_readme/pull_request.png)

---

#### 17. Pull Request-uri la care am făcut review

```text
PR #<9> — Review pentru funcționalitatea <Neacsu Roxana / Rolls-Royce>.
PR #<10> — Review pentru funcționalitatea <Poting Stefan / McLaren>.
```

---

#### 18. Stadiu final

| Componentă | Status |
|---|---|
| Cod Porsche | Finalizat |
| Funcții în bibliotecă | Finalizat |
| Rute Flask | Finalizat |
| Teste unitare | Finalizat |
| Testare locală | Finalizată |
| Dockerfile | Finalizat |
| Imagine Docker | Creată |
| Container Docker | Testat |
| Jenkinsfile | Finalizat |
| Jenkins Pipeline | Rulat cu succes |
| README.md | Completat |
| Pull Request | Finalizat |
| Review coleg | Finalizat |

---

#### 19. Ce mai este de făcut

- crearea Pull Request-ului din `main_fierea_cosmin` către `main`;