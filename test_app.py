from app import app

def test_get_profiles():
    client = app.test_client()
    response = client.get('/profiles')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_profile():
    client = app.test_client()
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "skills": ["Python", "Flask"]
    }
    response = client.post('/profiles', json=payload)
    assert response.status_code == 201
    assert response.json["name"] == "Alice"
    assert "id" in response.json

def test_get_profile_by_id():
    client = app.test_client()
    # Créer un profil d'abord
    payload = {
        "name": "Bob",
        "email": "bob@example.com",
        "skills": ["Java"]
    }
    post_response = client.post('/profiles', json=payload)
    profile_id = post_response.json["id"]

    # Récupérer ce profil
    response = client.get(f'/profiles/{profile_id}')
    assert response.status_code == 200
    assert response.json["name"] == "Bob"

def test_get_profile_not_found():
    client = app.test_client()
    response = client.get('/profiles/999')
    assert response.status_code == 404

def test_delete_profile():
    client = app.test_client()
    # Créer un profil à supprimer
    payload = {
        "name": "Charlie",
        "email": "charlie@example.com",
        "skills": ["Docker"]
    }
    post_response = client.post('/profiles', json=payload)
    profile_id = post_response.json["id"]

    # Supprimer ce profil
    response = client.delete(f'/profiles/{profile_id}')
    assert response.status_code == 200
    assert response.json["message"] == "Profil supprimé"

def test_get_profiles_by_skill():
    client = app.test_client()
    # Créer un profil avec la skill "DevOps"
    payload = {
        "name": "Diana",
        "email": "diana@example.com",
        "skills": ["DevOps"]
    }
    client.post('/profiles', json=payload)

    # Vérifier filtrage par skill
    response = client.get('/profiles/skills?skill=DevOps')
    assert response.status_code == 200
    assert any("DevOps" in p.get("skills", []) for p in response.json)
