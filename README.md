# curs_scc_441D_masini

Aplicatie Flask pentru proiectul de curs Servicii Cloud si Containerizare.

## Functionalitate adaugata

- Tema: masini
- Element ales: Lamborghini
- Dezvoltator: Laur Andronie
- Functii adaugate in `app/lib/biblioteca_masini.py`:
  - `culoare_lamborghini()`
  - `descriere_lamborghini()`

## Rute disponibile

- `/` - pagina principala
- `/masini` - ruta pentru tema
- `/masini/lamborghini` - ruta pentru elementul ales
- `/masini/lamborghini/culoare` - informatii despre culori Lamborghini
- `/masini/lamborghini/descriere` - descriere Lamborghini

## Testare

Testele sunt in `app/test/test_masini.py` si pot fi rulate cu:

```bash
python3 -m unittest discover -s app/test
```

## Rulare locala

```bash
python masini.py
```

Aplicatia porneste pe `http://localhost:5000`.

## Containerizare

Construire imagine:

```bash
docker build -t curs_scc_441d_masini .
```

Rulare container:

```bash
docker run -p 5000:5000 curs_scc_441d_masini
```

## Stadiu

- Cod functionalitate: adaugat
- Teste pytest: adaugate
- Jenkinsfile: configurat
- Dockerfile: configurat
- Integrare PR: de completat dupa creare PR
- Review PR-uri: de completat cu ID-urile PR-urilor revizuite
