from masini import app


def test_ruta_index():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Masini" in response.data


def test_ruta_mercedes_home():
    client = app.test_client()
    response = client.get("/masini/mercedes")

    assert response.status_code == 200
    assert b"Mercedes-Benz" in response.data


def test_ruta_mercedes_descriere():
    client = app.test_client()
    response = client.get("/masini/mercedes/descriere")

    assert response.status_code == 200
    assert b"producator german" in response.data


def test_ruta_mercedes_origine():
    client = app.test_client()
    response = client.get("/masini/mercedes/origine")

    assert response.status_code == 200
    assert b"Germania" in response.data


def test_ruta_mercedes_motorizare():
    client = app.test_client()
    response = client.get("/masini/mercedes/motorizare")

    assert response.status_code == 200
    assert b"motorizari" in response.data
