#!/usr/bin/env python3

def descriere_mclaren():
    return (
        "McLaren este o marcă britanică de automobile sport și supercaruri, "
        "cunoscută pentru performanță ridicată, design aerodinamic și tehnologii "
        "inspirate din motorsport și Formula 1."
    )


def modele_mclaren():
    return [
        "McLaren Artura",
        "McLaren 720S",
        "McLaren 765LT",
        "McLaren P1",
        "McLaren Senna"
    ]


def afiseaza_informatii():
    print("=== Proiect SCC - Tema: Mașini ===")
    print("Grupa: 441D")
    print("Element ales: McLaren")
    print()
    print("Descriere:")
    print(descriere_mclaren())
    print()
    print("Modele reprezentative:")
    for model in modele_mclaren():
        print(f"- {model}")


if __name__ == "__main__":
    afiseaza_informatii()
