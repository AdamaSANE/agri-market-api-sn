# 🌾 AgriMarket API Sénégal (Data-as-a-Service)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API_REST-009688?style=for-the-badge&logo=fastapi)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analytics-150458?style=for-the-badge&logo=pandas)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase)

AgriMarket est un backend "Data-as-a-Service" (DaaS) conçu pour ingérer, stocker et analyser les prix quotidiens des denrées agricoles sur les marchés locaux sénégalais (Sandaga, Thiaroye, Diaobé, etc.).

## 🚀 Fonctionnalités & Architecture

Ce projet démontre une architecture hybride orientée "Data & Backend" :

- **Ingestion Sécurisée :** Validation stricte des données entrantes (types, valeurs positives) via `Pydantic`.
- **Persistance Cloud :** Stockage relationnel sur une instance `PostgreSQL` managée par `Supabase`.
- **Moteur Analytique (Pandas) :** Une route dédiée (`/api/analytics/averages`) extrait les données brutes, calcule dynamiquement les prix moyens par marché et par denrée avec `Pandas`, et expose le résultat formaté en JSON.

## 💻 Structure du Projet

L'API respecte le principe de séparation des préoccupations (Clean Architecture) :

- `app/models/` : Schémas de validation des données (Pydantic).
- `app/core/` : Gestion centralisée et sécurisée de la connexion base de données.
- `app/services/` : Logique métier et pipelines d'analyse (Pandas).
- `app/main.py` : Point d'entrée de l'application et exposition des routes.

## 🛠️ Installation & Démarrage local

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/AdamaSANE/agri-market-api-sn.git https://github.com/AdamaSANE/agri-market-api-sn.git
   cd agri-market-api-sn
   ```
