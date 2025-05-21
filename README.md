# 🚀 DevPortfolio API – CI/CD avec GitHub Actions + Render

Cette API permet de gérer dynamiquement des **profils développeurs** avec leurs informations personnelles, compétences et projets réalisés.

Elle est développée en **Flask (Python)** et intègre :
- ✅ Tests unitaires avec **pytest**
- ✅ Linting avec **flake8**
- ✅ Intégration continue (**CI**) via **GitHub Actions**
- ✅ Déploiement continu (**CD**) via **Render**

---

## 📘 Fonctionnalités de l’API

| Méthode | Route                          | Description                                      |
|---------|--------------------------------|--------------------------------------------------|
| GET     | `/profiles`                   | Récupère la liste de tous les profils            |
| POST    | `/profiles`                   | Crée un nouveau profil développeur               |
| GET     | `/profiles/<id>`              | Récupère un profil par son ID                    |
| DELETE  | `/profiles/<id>`              | Supprime un profil par son ID                    |
| GET     | `/profiles/skills?skill=XXX`  | Filtre les profils par compétence                |

---

## 📦 Exemple de profil JSON

```json
{
  "name": "Christine",
  "email": "christine@example.com",
  "skills": ["Python", "Flask"]
}
## Installe les dépendances:  pip install -r requirements.txt


## Lance le serveur Flask : python app.py

## L’API est disponible sur : http://127.0.0.1:5000/profiles

## Lancer les tests : pytest

## Vérifier la qualité du code: flake8 .

⚙️ Intégration Continue (CI)


Le pipeline GitHub Actions :

S’exécute sur chaque push ou pull_request sur main

Vérifie le linting (flake8)

Exécute tous les tests (pytest)

Fichier : .github/workflows/ci.yml

🚀 Déploiement automatique avec Render

