### Proiect SCC - Grupa 441D - Masini

Dezvoltarea unei aplicatii colaborative de baza in Python/Flask pentru a exersa lucrul cu Git/GitHub, Jenkins si Docker.

#### Detalii Implementare
* **Tema grupei:** Masini
* **Element individual ales:** Volvo (Modele acoperite: XC60, V50, V90)
* **Baza de date:** `app/lib/biblioteca_masini.py`.

#### Rutele Aplicatiei
Aplicatia contine rutele cerute in tema:
1. **Ruta pentru tema (Generala):** `/`
2. **Ruta pentru element:** `/masini/volvo`
3. **Ruta pentru lista de elemente:** `/masini/volvo/modele`
4. **Ruta pentru informatii specifice:** `/masini/volvo/detalii?model=XC60`

#### Containerizare (Docker)
Pentru a rula aplicatia containerizata, folositi urmatoarele comenzi in directorul unde se afla fisierul `Dockerfile`:

1. **Creare imagine Docker:**
```bash
docker build -t masini-app .
```

2. **Rulare container:**
```bash
docker run -d -p 5055:5055 --name masini-container masini-app
```
Dupa rularea comenzilor, aplicatia poate fi accesata din browser la adresa: `http://localhost:5055`

3. **Oprire si stergere container (cand doriti sa actualizati/reconstruiti):**
```bash
docker stop masini-container
docker rm masini-container
```

#### Rulare Teste (Local)
Inainte de a trimite codul pe GitHub pentru a fi rulat de Jenkins, testele pot fi rulate local (din folderul radacina) folosind:
```bash
python -m unittest discover -s app/test -p "test_*.py"
```

#### Testare si Rezultate

**1. Imaginea creata**

![Imaginea creata cu succes](documentatie_generata/malanca_gabriel/assets/image.png)

**2. Containerul ruland**

![Containerul Docker ruland](documentatie_generata/malanca_gabriel/assets/image-1.png)

**3. Accesarea aplicatiei din browser**
![Accesare ruta generala](documentatie_generata/malanca_gabriel/assets/image-2.png)
![Accesare ruta element](documentatie_generata/malanca_gabriel/assets/image-3.png)
![Accesare lista de elemente](documentatie_generata/malanca_gabriel/assets/image-4.png)
![Accesare detalii element](documentatie_generata/malanca_gabriel/assets/image-5.png)

**4. Log-urile din consola care confirma accesarea**
![Log-uri consola](documentatie_generata/malanca_gabriel/assets/image-6.png)

#### Pull Requests

Review:
-alexsterpan