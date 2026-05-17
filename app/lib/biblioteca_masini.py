def descriere_renault() -> str:
    return (
        "Renault S.A este o companie franceză producătoare de autovehicule, fondată în 1899. Are sediul în Boulogne-Billancourt, Franța și este unul dintre cei mai mari producători de automobile din țară. Compania produce o gamă largă de vehicule, inclusiv mașini, camioane, autobuze și vehicule electrice. Renault este cunoscut pentru design-urile sale inovatoare și a fost lider în dezvoltarea vehiculelor electrice, în special în Europa. În urma alianței cu grupul japonez Nissan, a devenit unul dintre cei mai mari constructori auto din lume.În anul 2010, grupul a raportat vânzări record de 2,63 de milioane de unități, datorită în parte succesului mașinilor cu prețuri reduse, după ce în anii anteriori a înregistrat scăderi din cauza crizei economice."
    )


MODELE_RENAULT = {
    "clio": {
        "nume": "Renault Clio",
        "tip_caroserie": "Hatchback, 5 usi, 5 locuri",
        "descriere": (
            "Renault Clio este un model compact, potrivit pentru oras, naveta "
            "si utilizare zilnica."
        ),
        "culori": ["Alb", "Negru", "Gri", "Rosu", "Albastru"],
        "motorizari": [
            "1.0 TCe",
            "1.0 TCe GPL",
            "1.6 E-Tech Hybrid",
            "1.6 E-Tech Hybrid Multimode",
        ],
        "dotari": [
            "sistem multimedia",
            "climatizare automata",
            "senzori de parcare",
            "asistenta la mentinerea benzii",
            "franare automata de urgenta",
            "camera pentru marsarier",
        ],
        "informatii_generale": [
            "numar de locuri: 5",
            "transmisie: manuala sau automata, in functie de motorizare",
            "tractiune: fata",
            "utilizare recomandata: oras, naveta, consum redus",
        ],
    },
    "megane": {
        "nume": "Renault Megane",
        "tip_caroserie": "Sedan / Hatchback, in functie de versiune",
        "descriere": (
            "Renault Megane este un model compact potrivit pentru utilizare zilnica, "
            "drumuri urbane si extraurbane."
        ),
        "culori": ["Alb", "Negru", "Gri", "Albastru", "Rosu"],
        "motorizari": [
            "1.5 Blue dCi (115 CP) EDC",
            "1.5 Blue dCi (115 CP)",
            "1.3 TCe (140 CP) EDC",
            "1.3 TCe (140 CP)",
            "1.0 TCe (115 CP)",
        ],
        "dotari": [
            "climatizare automata",
            "senzori de parcare",
            "camera pentru marsarier",
            "sistem multimedia",
            "pilot automat",
            "faruri LED",
        ],
        "informatii_generale": [
            "numar de locuri: 5",
            "transmisie: manuala sau automata, in functie de motorizare",
            "tractiune: fata",
            "utilizare recomandata: familie, oras, drumuri lungi",
        ],
    },
    "captur": {
        "nume": "Renault Captur",
        "tip_caroserie": "Crossover / SUV compact, 5 usi, 5 locuri",
        "descriere": (
            "Renault Captur este un crossover urban, mai spatios decat Clio, "
            "potrivit pentru oras si drumuri mixte."
        ),
        "culori": ["Alb", "Negru", "Gri", "Portocaliu", "Albastru"],
        "motorizari": [
            "1.0 TCe",
            "1.0 TCe GPL",
            "1.3 TCe",
            "1.6 E-Tech Hybrid",
            "1.6 E-Tech Plug-in Hybrid",
            "1.8 E-Tech Full Hybrid",
        ],
        "dotari": [
            "senzori de parcare",
            "camera pentru marsarier",
            "sistem multimedia",
            "climatizare automata",
            "pilot automat",
            "asistenta la mentinerea benzii",
        ],
        "informatii_generale": [
            "numar de locuri: 5",
            "transmisie: manuala sau automata, in functie de motorizare",
            "tractiune: fata",
            "utilizare recomandata: familie mica, oras, drumuri mixte",
        ],
    },
    "austral": {
        "nume": "Renault Austral",
        "tip_caroserie": "SUV, 5 usi, 5 locuri",
        "descriere": (
            "Renault Austral este un SUV orientat spre confort, tehnologie "
            "si utilizare de familie."
        ),
        "culori": ["Alb", "Negru", "Gri", "Rosu", "Albastru"],
        "motorizari": [
            "1.2 E-Tech Full Hybrid",
            "1.2 E-Tech Full Hybrid 160 CP",
            "1.2 E-Tech Full Hybrid 200 CP",
            "1.3 Mild Hybrid",
        ],
        "dotari": [
            "camera 360",
            "faruri LED Matrix",
            "pilot automat adaptiv",
            "sistem multimedia avansat",
            "senzori de parcare",
            "asistenta la franare",
        ],
        "informatii_generale": [
            "numar de locuri: 5",
            "transmisie: automata, in functie de versiune",
            "tractiune: fata, in functie de configuratie",
            "utilizare recomandata: familie, drumuri lungi, confort",
        ],
    },
    "arkana": {
        "nume": "Renault Arkana",
        "tip_caroserie": "SUV Coupe, 5 usi, 5 locuri",
        "descriere": (
            "Renault Arkana este un SUV coupe, cu design sportiv si spatiu "
            "potrivit pentru utilizare zilnica."
        ),
        "culori": ["Alb", "Negru", "Gri", "Rosu", "Albastru"],
        "motorizari": [
            "1.3 TCe (140 CP) EDC",
            "1.3 TCe mild hybrid",
            "1.6 E-Tech Hybrid (143 CP) Multimode",
        ],
        "dotari": [
            "sistem multimedia",
            "camera pentru marsarier",
            "senzori de parcare",
            "pilot automat",
            "asistenta la mentinerea benzii",
            "faruri LED",
        ],
        "informatii_generale": [
            "numar de locuri: 5",
            "transmisie: automata, in functie de motorizare",
            "tractiune: fata",
            "utilizare recomandata: familie, oras, drumuri extraurbane",
        ],
    },
    "talisman": {
        "nume": "Renault Talisman",
        "tip_caroserie": "Sedan / Combi, in functie de versiune",
        "descriere": (
            "Renault Talisman este un model de clasa medie, orientat spre confort, "
            "spatiu si drumuri lungi."
        ),
        "culori": ["Alb", "Negru", "Gri", "Albastru", "Rosu"],
        "motorizari": [
            "1.3 TCe (160 CP) EDC FAP",
            "1.3 TCe (160 CP) 4CONTROL EDC FAP",
            "1.7 Blue dCi (150 CP)",
            "1.7 Blue dCi (150 CP) 4CONTROL",
            "2.0 Blue dCi (160 CP) EDC",
            "2.0 Blue dCi (200 CP) EDC",
            "1.8 TCe (225 CP) EDC FAP",
        ],
        "dotari": [
            "climatizare automata",
            "pilot automat adaptiv",
            "sistem multimedia",
            "senzori de parcare",
            "camera pentru marsarier",
            "faruri LED",
            "sistem 4CONTROL, in functie de versiune",
        ],
        "informatii_generale": [
            "numar de locuri: 5",
            "transmisie: manuala sau automata, in functie de motorizare",
            "tractiune: fata",
            "utilizare recomandata: familie, confort, drumuri lungi",
        ],
    },
}


def modele_renault() -> dict:
    return MODELE_RENAULT


def detalii_model_renault(model_id: str) -> dict | None:
    return MODELE_RENAULT.get(model_id)


def culoare_renault() -> str:
    return (
        "Informatiile despre culorile Renault sunt disponibile in pagina Modele Renault, "
        "pentru fiecare model in parte."
    )


def dotari_renault() -> str:
    return (
        "Informatiile despre dotarile Renault sunt disponibile in pagina Modele Renault, "
        "pentru fiecare model in parte."
    )
