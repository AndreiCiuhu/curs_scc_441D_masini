# Proiect SCC - Mașini - Fiat

## Date student

Student: Dumbrava Teodor  
Grupa: 441D  
Tema: Mașini  
Element ales: Fiat  

## Funcționalitate adăugată

În cadrul proiectului am adăugat funcționalitate pentru marca auto Fiat.

Au fost implementate două funcții în fișierul:

`app/lib/biblioteca_masini.py`

Funcțiile adăugate sunt:

- `descriere_fiat()`
- `modele_fiat()`

## Rute adăugate

În aplicația Flask au fost adăugate următoarele rute:

- `/masini/fiat`
- `/masini/fiat/descriere`
- `/masini/fiat/modele`

Ruta principală `/` conține link-uri către funcționalitatea Fiat.

## Testare locală

A fost creat fișierul de test:

`app/test/test_fiat.py`

Testele au fost rulate local cu următoarea comandă:

```bash
pytest
