# curs_scc_441D_masini

## Functionalitate Rolls-Royce - Neacsu Roxana

### Date student

- Student: Neacsu Roxana
- Grupa: 441D
- Tema proiectului: Masini
- Marca aleasa: Rolls-Royce
- Branch de lucru: dev_neacsu_roxana

---

## Functionalitate adaugata

Am adaugat functionalitatea pentru marca Rolls-Royce in aplicatia Flask a proiectului.

Functionalitatea include o pagina principala pentru Rolls-Royce si doua pagini secundare:

- pagina cu istoricul marcii Rolls-Royce;
- pagina cu informatii despre motorizare;
- linkuri de navigare intre pagini.

---

## Rute implementate

| Ruta | Descriere |
|---|---|
| `/masini/rollsroyce/` | Pagina principala Rolls-Royce |
| `/masini/rollsroyce/istoric` | Pagina cu istoricul marcii Rolls-Royce |
| `/masini/rollsroyce/motorizare` | Pagina cu informatii despre motorizare |

---

## Fisiere adaugate/modificate

- `masini.py` - am inregistrat blueprint-ul pentru Rolls-Royce si am adaugat linkul in pagina principala.
- `app/lib/biblioteca_masini.py` - contine functiile pentru descriere, istoric si motorizare Rolls-Royce.
- `app/routes/rollsroyce.py` - contine rutele Flask pentru marca Rolls-Royce.
- `app/test/test_rollsroyce.py` - contine testele unitare pentru functii si rute.
- `Dockerfile` - fisier pentru containerizarea aplicatiei.
- `Jenkinsfile` - pipeline Jenkins pentru instalare dependinte, rulare teste si build Docker.

---

## Testare locala

Aplicatia a fost rulata local cu:

```bash
python3 masini.py
