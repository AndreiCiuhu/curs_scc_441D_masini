### curs_scc_441D_masini
### Functionalitate BMW - Vlad Cubic

#### Functionalitate adaugata

Am implementat integrarea cu un serviciu extern pentru a gestiona si prelua datele tehnice ale marcii BMW, respectand arhitectura proiectului (Grupa 441D).

Fisiere adaugate si modificate:
* app/lib/biblioteca_masini.py - implementarea functiilor modele_bmw() si detalii_bmw() folosind modulul requests pentru apeluri API.
* app/routes/bmw.py - blueprint-ul asociat rutelor web specifice.
* app/test/test_biblioteca_masini.py - crearea unit testelor folosind framework-ul unittest si functionalitatea de mock pentru decuplarea de API-ul extern.
* Dockerfile - instructiunile de build pentru imaginea de container bazata pe Python.
* Jenkinsfile - definirea pipeline-ului declarativ pentru automatizarea procesului de CI/CD.

Rute adaugate:
* / - pagina principala cu lista masinilor disponibile
* /masini/bmw - pagina de prezentare a producatorului BMW
* /masini/bmw/modele - lista modelelor BMW preluata via API Ninjas
* /masini/bmw/detalii?model=<nume> - detalii tehnice specifice pentru modelul interogat

#### Stadiul implementarii

* [x] Cod adaugat
* [x] Teste adaugate
* [x] Jenkinsfile configurat
* [x] Dockerfile creat

#### Testare

##### Testare manuala
Aplicatia a fost pornita in mediul de dezvoltare local. Toate rutele au fost accesate si validate din browser. Testele unitare au fost rulate in consola cu succes.

<details>
  <summary>Vezi captura de ecran: Testare manuala</summary>
  <img src="readme_individual/cubic_vlad/assets/ss7.png" alt="Testare manuala">
</details>

##### Testare cu Jenkins
Automatizarea testarii a fost confirmata prin executia cu succes a pipeline-ului. Testele au fost rulate si au trecut (status PASS).

<details>
  <summary>Vezi captura de ecran: Executie Jenkins</summary>
  <img src="readme_individual/cubic_vlad/assets/ss8.png" alt="Jenkins Pipeline">
</details>

#### Fisier Jenkins

A fost utilizat un pipeline declarativ structurat in 4 stage-uri:
1. Install dependencies
2. Run tests
3. Build image
4. Deploy

#### Containerizare

Aplicatia a fost containerizata si izolata cu succes. Se pot vizualiza mai jos dovezile executiei.

<details>
  <summary>Vezi captura de ecran: Imagine creata</summary>
  <img src="readme_individual/cubic_vlad/assets/ss1.png" alt="Imagine creata">
</details>

<details>
  <summary>Vezi captura de ecran: Container creat si functional</summary>
  <img src="readme_individual/cubic_vlad/assets/ss2.png" alt="Pornire container">
  <img src="readme_individual/cubic_vlad/assets/SS3.png" alt="Status container">
</details>

<details>
  <summary>Vezi captura de ecran: Browser accesand aplicatia din container</summary>
  <img src="readme_individual/cubic_vlad/assets/ss_final.png" alt="Browser acces">
</details>

<details>
  <summary>Vezi captura de ecran: Consola cu log-uri</summary>
  <img src="readme_individual/cubic_vlad/assets/ss5.png" alt="Log-uri container">
</details>

<details>
  <summary>Vezi captura de ecran: Curatare resurse dupa testare</summary>
  <img src="readme_individual/cubic_vlad/assets/ss6.png" alt="Curatare resurse">
</details>

#### Integrare

PR creat din branch-ul dev_Cubic_Vlad in main. Status: Aprobat si integrat cu succes (Merged).

#### Pull Request-uri la care am facut review

Am acordat review (Approve) pentru PR-ul unui coleg din grupa, respectand cerintele de verificare incrucisata.

#### Ce mai este de facut

Proiectul este finalizat 100% si nu mai exista task-uri restante. 
Toate etapele de dezvoltare, testare automata, containerizare și integrare a codului si a documentatiei prin PR au fost realizate si validate cu succes. Proiectul este gata pentru evaluare.