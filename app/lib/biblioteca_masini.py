def culoare_alpine() -> str:
    return (
        "Alpine este disponibilă în culori precum Bleu Alpine, Noir Profond, "
        "Blanc Irisé și Gris Tonnerre. Bleu Alpine este una dintre cele mai "
        "reprezentative culori ale mărcii."
    )


def descriere_alpine() -> str:
    return (
        "Alpine este o marcă franceză de automobile sport, cunoscută pentru "
        "mașini compacte, ușoare și orientate spre performanță. Modelul A110 "
        "este cel mai cunoscut model modern al mărcii."
    )


def modele_alpine() -> list[dict[str, str]]:
    return [
        {
            "nume": "Alpine A110",
            "descriere": "Model sport compact, inspirat de modelul clasic A110.",
            "caracteristici": "Greutate redusă, tracțiune spate, comportament sportiv."
        },
        {
            "nume": "Alpine A110 GT",
            "descriere": "Variantă orientată spre confort și utilizare de zi cu zi.",
            "caracteristici": "Interior mai rafinat, performanță ridicată, design elegant."
        },
        {
            "nume": "Alpine A110 S",
            "descriere": "Variantă mai sportivă a modelului A110.",
            "caracteristici": "Suspensie mai fermă, putere crescută, aspect agresiv."
        },
        {
            "nume": "Alpine A110 R",
            "descriere": "Variantă axată pe performanță și greutate redusă.",
            "caracteristici": "Elemente din fibră de carbon, aerodinamică îmbunătățită."
        }
    ]