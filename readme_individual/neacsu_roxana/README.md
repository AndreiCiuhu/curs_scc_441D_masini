### Proiect SCC 441D - Masini

#### Functionalitate Rolls-Royce - Neacsu Roxana

---

#### 1. Descriere generala

Acest proiect face parte din disciplina **Servicii Cloud si Containerizare**, pentru grupa **441D**, tema generala fiind **Masini**.

Pentru partea mea de proiect am implementat functionalitatea aferenta marcii **Rolls-Royce**. Functionalitatea este integrata intr-o aplicatie web realizata cu **Flask**, respectand structura proiectului de grup.

Scopul implementarii a fost adaugarea unei componente proprii in aplicatie, testarea acesteia, rularea prin Jenkins si containerizarea cu Docker.

---

#### 2. Date student

- **Student:** Neacsu Roxana
- **Grupa:** 441D
- **Tema:** Masini
- **Marca aleasa:** Rolls-Royce
- **Branch de dezvoltare:** `dev_neacsu_roxana`
- **Branch principal personal:** `main_neacsu_roxana`

---

#### 3. Functionalitate adaugata

Am adaugat o sectiune dedicata marcii **Rolls-Royce**.

Functionalitatea include:

- o pagina principala pentru Rolls-Royce;
- o pagina cu istoricul marcii;
- o pagina cu informatii despre motorizare;
- linkuri de navigare intre pagini;
- integrarea rutei Rolls-Royce in pagina principala a aplicatiei.

---

#### 4. Rute implementate

| Ruta | Descriere |
|---|---|
| `/` | Pagina principala a aplicatiei |
| `/masini/rollsroyce/` | Pagina principala Rolls-Royce |
| `/masini/rollsroyce/istoric` | Pagina cu istoricul marcii Rolls-Royce |
| `/masini/rollsroyce/motorizare` | Pagina cu informatii despre motorizare |

---

#### 5. Fisiere adaugate sau modificate

| Fisier | Rol |
|---|---|
| `masini.py` | Inregistreaza blueprint-ul Rolls-Royce si adauga linkul in pagina principala |
| `app/lib/__init__.py` | Marcheaza folderul `lib` ca pachet Python |
| `app/lib/biblioteca_masini.py` | Contine functiile pentru descriere, istoric si motorizare Rolls-Royce |
| `app/routes/rollsroyce.py` | Contine rutele Flask pentru Rolls-Royce |
| `app/test/test_rollsroyce.py` | Contine testele unitare |
| `Dockerfile` | Defineste imaginea Docker a aplicatiei |
| `Jenkinsfile` | Defineste pipeline-ul Jenkins |
| `README.md` | Documentatia proiectului |
| `docs/images/` | Contine capturile de ecran pentru documentatie |

---

#### 6. Stadiul implementarii

| Componenta | Status |
|---|---|
| Functionalitate Rolls-Royce | Implementata |
| Rute Flask | Implementate |
| Functii in biblioteca | Implementate |
| Teste unitare | Implementate si rulate cu succes |
| Rulare locala in browser | Verificata |
| Dockerfile | Creat |
| Imagine Docker | Creata |
| Container Docker | Pornit si testat |
| Jenkinsfile | Creat |
| Pipeline Jenkins | Rulat cu succes |
| Capturi de ecran | Adaugate |
| README | Completat |
| Pull Request | Urmeaza sa fie creat |
| Review coleg | Urmeaza sa fie solicitat |

---

### Testare

#### 7. Testare manuala locala

Aplicatia a fost rulata local cu:

```bash
python3 masini.py
```

Aplicatia a fost accesata in browser la:

```text
http://127.0.0.1:5000
```

Au fost testate manual urmatoarele rute:

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/masini/rollsroyce/
http://127.0.0.1:5000/masini/rollsroyce/istoric
http://127.0.0.1:5000/masini/rollsroyce/motorizare
```

Rezultat: toate paginile au fost afisate corect in browser.

---

#### 8. Testare unitara

Testele unitare se afla in fisierul:

```text
app/test/test_rollsroyce.py
```

Testele verifica:

- functia pentru descrierea Rolls-Royce;
- functia pentru istoricul Rolls-Royce;
- functia pentru motorizare;
- ruta principala Rolls-Royce;
- ruta pentru istoric;
- ruta pentru motorizare.

Comanda folosita pentru rularea testelor:

```bash
python3 -m unittest app/test/test_rollsroyce.py
```

Rezultat obtinut:

```text
Ran 6 tests
OK
```

---

### Docker

#### 9. Containerizare cu Docker

Aplicatia a fost containerizata folosind fisierul `Dockerfile`.

Imaginea Docker a fost construita cu:

```bash
sudo docker build -t masini-rollsroyce-neacsu-roxana .
```

Imaginea creata:

```text
masini-rollsroyce-neacsu-roxana:latest
```

Containerul a fost pornit cu:

```bash
sudo docker run -d -p 5000:5000 --name masini-rollsroyce-container masini-rollsroyce-neacsu-roxana
```

Containerul a fost verificat cu:

```bash
sudo docker ps
```

Aplicatia rulata in container a fost accesata in browser la:

```text
http://127.0.0.1:5000/masini/rollsroyce/
```

Logurile containerului au fost verificate cu:

```bash
sudo docker logs masini-rollsroyce-container
```

In loguri se observa cereri HTTP cu status `200`, ceea ce confirma faptul ca aplicatia din container a fost accesata corect din browser.

---

### Jenkins

#### 10. Rulare cu Jenkins

A fost creat si configurat un pipeline Jenkins pentru branch-ul:

```text
dev_neacsu_roxana
```

Pipeline-ul foloseste fisierul:

```text
Jenkinsfile
```

Stage-urile rulate in Jenkins sunt:

| Stage | Rol |
|---|---|
| Checkout | Preia codul din repository |
| Install dependencies | Instaleaza dependintele din `requirement.txt` |
| Run unit tests | Ruleaza testele unitare |
| Build Docker image | Construieste imaginea Docker |
| Run Docker container | Porneste containerul Docker |

Pipeline-ul Jenkins a rulat cu succes, iar rezultatul final a fost:

```text
Finished: SUCCESS
```

---

### Capturi de ecran

#### 11. Capturi testare in browser

##### Pagina principala

![Pagina principala](readme_individual/neacsu_roxana/docs/images/browser_home.png)

##### Pagina Rolls-Royce

![Pagina Rolls-Royce](readme_individual/neacsu_roxana/docs/images/browser_rollsroyce.png)

##### Pagina Istoric Rolls-Royce

![Istoric Rolls-Royce](readme_individual/neacsu_roxana/docs/images/browser_istoric.png)

##### Pagina Motorizare Rolls-Royce

![Motorizare Rolls-Royce](readme_individual/neacsu_roxana/docs/images/browser_motorizare.png)

---

#### 12. Capturi Docker

##### Imagine Docker creata

![Imagine Docker](readme_individual/neacsu_roxana/docs/images/docker_images.png)

##### Container Docker pornit

![Container Docker](readme_individual/neacsu_roxana/docs/images/docker_ps.png)

##### Loguri container Docker

![Loguri container](readme_individual/neacsu_roxana/docs/images/container_logs.png)

---

#### 13. Capturi Jenkins

##### Pipeline Jenkins executat cu succes

![Jenkins pipeline success](readme_individual/neacsu_roxana/docs/images/jenkins_pipeline_success.png)

##### Console Output Jenkins

![Jenkins console output](readme_individual/neacsu_roxana/docs/images/jenkins_console_output.png)

---

### Integrare GitHub

#### 14. Branch-uri folosite

Codul a fost dezvoltat pe branch-ul personal:

```text
dev_neacsu_roxana
```

Branch-ul principal personal este:

```text
main_neacsu_roxana
```

Fluxul propus pentru integrare este:

```text
dev_neacsu_roxana -> main_neacsu_roxana
```

---

#### 15. Pull Request si review

Pentru integrarea modificarilor realizate pe branch-ul de dezvoltare, a fost creat Pull Request-ul din branch-ul `dev_neacsu_roxana` catre branch-ul personal principal `main_neacsu_roxana`.

- **Pull Request:** `#9`
- **Sursa:** `dev_neacsu_roxana`
- **Destinatie:** `main_neacsu_roxana`
- **Status:** creat, verificat, aprobat si integrat cu succes
- **Review primit de la:** `stefanpoting`
- **Merge realizat de:** `CosminFierea`

Pull Request-ul nu a avut conflicte cu branch-ul de baza, iar modificarile au fost integrate cu succes in `main_neacsu_roxana`.

Status actual:

```text
PR #9 creat, aprobat si merged.
```

---

#### 16. Stadiu final si ce mai este de facut

Pentru partea personala a proiectului, functionalitatea Rolls-Royce este implementata, testata, documentata si integrata in branch-ul `main_neacsu_roxana`.

Activitati finalizate:

- implementarea functionalitatii Rolls-Royce;
- adaugarea testelor unitare;
- rularea testelor local si prin Jenkins;
- containerizarea aplicatiei cu Docker;
- rularea aplicatiei in container;
- completarea README-ului cu documentatie si capturi;
- crearea Pull Request-ului `#9`;
- obtinerea review-ului de la un coleg;
- integrarea modificarilor in `main_neacsu_roxana`;
- efectuarea/verificarea review-ului pentru Pull Request-ul unui coleg.

Activitati ramase, daca sunt solicitate in etapa finala a proiectului:

- integrarea in branch-ul principal al grupei `main`, doar daca este solicitata de coordonator/profesor;
- verificarea finala a documentatiei dupa integrarea in branch-ul principal al grupei.

  ## 17. Concluzie

Functionalitatea Rolls-Royce este implementata si testata.

Au fost realizate:

- rutele Flask pentru Rolls-Royce;
- testele unitare;
- rularea locala in browser;
- containerizarea cu Docker;
- rularea aplicatiei in container;
- pipeline Jenkins cu rezultat `SUCCESS`;
- documentatia README cu capturi de ecran;
- Pull Request-ul `#9`, aprobat si integrat in `main_neacsu_roxana`.

Proiectul este pregatit pentru etapa finala de verificare la nivelul grupei.