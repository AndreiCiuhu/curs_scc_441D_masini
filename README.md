# Proiect SCC - Hyundai

## Functionalitate adaugata
- Biblioteca pentru Hyundai
- Functii:
  - culoare_hyundai()
  - descriere_hyundai()
- Rute Flask:
  - /masini
  - /masini/hyundai
  - /masini/hyundai/culoare
  - /masini/hyundai/descriere

## Stadiul implementarii
- [x] Cod
- [x] Teste
- [x] Jenkinsfile
- [x] Dockerfile

## Testare manuala
Rutele au fost accesate din browser:
- /masini
- /masini/hyundai
- /masini/hyundai/culoare
- /masini/hyundai/descriere

## Testare cu Jenkins
Pipeline Jenkins ruleaza:
- instalare dependinte
- rulare teste unitare

## Fisier Jenkins
Pipeline-ul foloseste Dockerfile pentru build si ruleaza testele unitare cu unittest.

## Integrare
PR urmeaza sa fie trimis din:
dev_Maravela_Viorel -> main_Maravela_Viorel

## Containerizare
Aplicatia ruleaza in container Docker pe portul 5000.

## PR-uri la care am facut review
- urmeaza

## Ce mai este de facut
- creare PR
- review PR coleg
- screenshot Jenkins PASS
- screenshot Docker si browser

