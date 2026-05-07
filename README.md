# curs_scc_441D_masini

# Functionalitate Kia — Aniculesei Mihnea

## Functionalitate adaugata
Fisiere adaugate:
- `app/lib/biblioteca_masini.py` - functiile `modele_kia()` si `detalii_kia()`
- `app/routes/kia.py` - blueprint cu rutele Kia
- `app/test/test_biblioteca_masini.py` - unit teste

Rute adaugate:
- `/` - pagina principala cu lista masinilor disponibile
- `/masini/kia` - pagina elementului Kia
- `/masini/kia/modele` - lista modele Kia via API Ninjas
- `/masini/kia/detalii?model=<nume>` - detalii tehnice pentru un model specific


## Stadiul implementarii
- [x] Cod adaugat
- [x] Teste adaugate
- [x] Jenkinsfile configurat
- [x] Dockerfile creat

## Testare

### Testare manuala
Aplicatia a fost pornita local si rutele au fost accesate din browser.
<img width="1199" height="169" alt="image" src="https://github.com/user-attachments/assets/59b4a6ba-bb38-4fcb-8316-e4b32715fbf6" />

<img width="934" height="344" alt="image" src="https://github.com/user-attachments/assets/29156c6e-806d-42f5-b532-a1fddff426fe" />
<img width="743" height="35" alt="image" src="https://github.com/user-attachments/assets/3de58ddb-64b2-4ab0-8bef-61459de40efc" />


<img width="965" height="986" alt="image" src="https://github.com/user-attachments/assets/26061281-7860-46e6-a388-9e72e492225e" />
<img width="838" height="31" alt="image" src="https://github.com/user-attachments/assets/16882b54-d644-474c-846c-076888d958c5" />


<img width="954" height="502" alt="image" src="https://github.com/user-attachments/assets/8ea9cfb0-a40b-47f8-96fe-dde7b5c0f2ec" />
<img width="977" height="33" alt="image" src="https://github.com/user-attachments/assets/60ab334a-c9f8-4ead-bb51-2c35fafb5dc0" />


### Testare cu Jenkins
Testele au fost rulate cu Jenkins si au trecut.
<img width="1242" height="466" alt="image" src="https://github.com/user-attachments/assets/61a0344d-5558-4c91-aaef-d21e45c2c2eb" />

## Fisier Jenkins
Pipeline declarativ cu 4 stage-uri:
- Install dependencies
- Run tests
- Build image
- Deploy

## Containerizare
Imaginea creata:
<img width="1160" height="119" alt="image" src="https://github.com/user-attachments/assets/7b8ec3c5-3eb1-4774-9373-12ce006b59cb" />

Containerul creat:
<img width="1209" height="151" alt="image" src="https://github.com/user-attachments/assets/0e90f620-544c-482d-9589-4fef9ccec8d7" />

Browser care acceseaza aplicatia din container:
<img width="955" height="355" alt="image" src="https://github.com/user-attachments/assets/b5adb1d7-f29a-4e0d-a5da-af3fa2da2bb3" />

Consola cu log-uri container:
<img width="1215" height="205" alt="image" src="https://github.com/user-attachments/assets/1c74fbe1-650d-4f09-9cd2-ed8d033a00a4" />


## Integrare
PR creat din `dev_aniculesei_mihnea` in `main_aniculesei_mihnea`.
Status: Finalizat.



## Ce mai este de facut
- Integrare in main
