### curs_scc_441D_masini

#### Funcționalitate Mercedes-Benz — Sterpan Alexandru

---

#### Descriere generală

În cadrul proiectului am implementat funcționalitatea aferentă elementului **Mercedes-Benz**.

Funcționalitatea permite accesarea unor pagini dedicate mărcii Mercedes-Benz, unde sunt prezentate informații despre descrierea mărcii, originea acesteia și tipurile de motorizări folosite.

Aplicația este realizată în Flask. Logica funcționalității este separată în fișierul `mercedes.py`, rutele sunt definite separat în `app/routes/mercedes_routes.py`, iar interfața grafică este realizată prin fișiere HTML și CSS.

Proiectul include și teste unitare, un fișier `Jenkinsfile` pentru automatizarea pașilor de testare/build/deploy și un `Dockerfile` pentru rularea aplicației într-un container.

---

#### Branch-uri utilizate

Pentru realizarea proiectului au fost folosite următoarele branch-uri:

- `dev_sterpan_alexandru` - branch-ul de dezvoltare;
- `main_sterpan_alexandru` - branch-ul personal principal;
- `main` - branch-ul principal al proiectului.

Fluxul de lucru folosit:

```text
dev_sterpan_alexandru -> main_sterpan_alexandru -> main
```

Fișiere adăugate sau modificate

Pentru implementarea funcționalității Mercedes-Benz au fost adăugate sau modificate următoarele fișiere:

mercedes.py
masini.py
app/routes/mercedes_routes.py
templates/mercedes.html
static/mercedes.css
app/test/test_mercedes_functions.py
requirements.txt
Jenkinsfile
Dockerfile
.dockerignore
README.md

Funcții implementate

În fișierul mercedes.py au fost implementate următoarele funcții:

descriere_mercedes()
origine_mercedes()
motorizare_mercedes()

Rolul funcțiilor:

descriere_mercedes() returnează o descriere generală a mărcii Mercedes-Benz;
origine_mercedes() returnează informații despre originea mărcii;
motorizare_mercedes() returnează informații despre tipurile de motorizări folosite de Mercedes-Benz.


Rute implementate:

| Rută                          | Descriere                                 |
| ----------------------------- | ----------------------------------------- |
| `/`                           | Pagina principală a aplicației            |
| `/masini`                     | Pagina generală pentru tema Mașini        |
| `/masini/mercedes`            | Pagina principală Mercedes-Benz           |
| `/masini/mercedes/descriere`  | Pagina cu descrierea mărcii Mercedes-Benz |
| `/masini/mercedes/origine`    | Pagina cu originea mărcii Mercedes-Benz   |
| `/masini/mercedes/motorizare` | Pagina cu informații despre motorizare    |

Interfață grafică

Interfața grafică pentru Mercedes-Benz este realizată folosind:

templates/mercedes.html pentru structura paginii;
static/mercedes.css pentru stilizarea paginii.

Pagina are un design propriu, cu fundal închis, carduri informative și butoane de navigare către secțiunile dedicate.

Testare manuală

Au fost testate manual următoarele rute:

http://127.0.0.1:5000/masini/mercedes
http://127.0.0.1:5000/masini/mercedes/descriere
http://127.0.0.1:5000/masini/mercedes/origine
http://127.0.0.1:5000/masini/mercedes/motorizare

<img width="1158" height="870" alt="image" src="https://github.com/user-attachments/assets/673b8dcf-9953-4252-bdfc-fb2a4d71e7b3" />

<img width="1158" height="870" alt="image" src="https://github.com/user-attachments/assets/fcbff609-7692-4777-9548-946609b67782" />

<img width="580" height="322" alt="image" src="https://github.com/user-attachments/assets/badb1f85-f46a-4db0-bfd3-3f8dda804481" />

<img width="587" height="318" alt="image" src="https://github.com/user-attachments/assets/7303f40d-c3f4-497a-9b4a-c8f60a7be4ac" />

<img width="1143" height="656" alt="image" src="https://github.com/user-attachments/assets/7c2590fc-ce47-43b0-8d56-8be363ca140e" />

<img width="400" height="234" alt="image" src="https://github.com/user-attachments/assets/30365b81-0d12-4c6f-937e-761b3a85d32b" />

<img width="404" height="126" alt="image" src="https://github.com/user-attachments/assets/7892b591-fc7c-44b4-a9ba-7ae8a3445660" />

Testare unitară

Testele unitare au fost adăugate în fișierul:

app/test/test_mercedes_functions.py

Testele verifică funcțiile definite în mercedes.py.

Comanda pentru rularea testelor:

pytest app/test/test_mercedes_functions.py

Jenkins

A fost adăugat fișierul Jenkinsfile.

Pipeline-ul Jenkins conține următoarele stage-uri:

Install dependencies
Run unit tests
Build Docker image
Deploy container

Rolul fiecărui stage:

Install dependencies creează mediul virtual și instalează dependențele;
Run unit tests rulează testele unitare cu pytest;
Build Docker image construiește imaginea Docker a aplicației;
Deploy container pornește containerul aplicației.

<img width="1227" height="677" alt="image" src="https://github.com/user-attachments/assets/b13d9fed-48af-4b5f-acb6-ad43c91d30df" />

<img width="852" height="40" alt="image" src="https://github.com/user-attachments/assets/8c7dab3e-a2f1-41b5-8c1d-9bc67e229910" />


<img width="584" height="298" alt="image" src="https://github.com/user-attachments/assets/ad8d9ca6-6ff3-419d-8797-08a0eede03c2" />