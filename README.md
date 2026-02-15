# ⚡ FastAPI Authentication System (MVC & Docker)

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-black?style=for-the-badge&logo=json-web-tokens)

> Un micro-service d'authentification robuste construit avec **FastAPI**, structuré selon le pattern **MVC** et conteneurisé avec **Docker**.

## 🏗️ Architecture du Projet (MVC)

Le projet suit une séparation stricte des responsabilités pour assurer la maintenabilité :

* 📂 **Controllers** (`/controllers`) : Logique métier et gestion des requêtes.
* 📂 **Models** (`/models`) : Définition des schémas de données (Pydantic).
* 📂 **Routes** (`/routes`) : Définition des endpoints API.
* 📂 **Auth** (`/auth`) : Gestion de la sécurité et des tokens JWT.
* 📂 **DB** (`/db`) : Connexion et interaction avec la base de données.

## ✨ Fonctionnalités Clés
* 🔐 **Authentification JWT :** Login, Inscription et protection des routes.
* 🐳 **Docker Ready :** Déploiement facile via `docker-compose`.
* 🚀 **Haute Performance :** Utilisation de FastAPI (Asynchrone).
* 🛡️ **Validation des Données :** Utilisation de Pydantic.

## ⚙️ Configuration (.env)

Avant de lancer le projet, créez un fichier `.env` à la racine et ajoutez vos variables :
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=fastapi_auth_db
SECRET_KEY=votre_cle_secrete_super_longue
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🛠️ Installation et Démarrage

### Option 1 : Via Docker (Recommandé)
```bash
# Lancer le conteneur
docker-compose up --build
```
### Option 2 : Manuelle (Local)
```bash
# 1. Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le serveur
uvicorn main:app --reload
```

## 📚 Documentation API (Swagger)
Une fois le serveur lancé, accédez à la documentation interactive :
* **Swagger UI :** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc :** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 👤 Auteur
**Youssef Barakat**
