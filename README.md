# 🧪 Grader - Service de correction automatique de code

## 🎯 Objectif

Le **Grader** est un composant serveur autonome dont le rôle est d'assurer la **correction automatique et sécurisée** de soumissions de code, principalement en langage C (d'autres langages seront ajoutés par la suite).

Il est conçu pour être appelé par un serveur principal (via API ou via une file locale) et pour exécuter le code utilisateur dans un environnement isolé, le comparer à des cas de test et retourner un résultat précis.

## ⚙ Fonctionnement global

1. Le Grader surveille une **file locale** contenant des fichiers `.json` (soumissions).
2. Chaque fichier décrit :

   * Le chemin du code utilisateur
   * Le chemin du fichier de tests associé (immuable)
   * L'utilisateur concerné
   * L'ID de soumission, le langage, les flags de compilation, etc.
3. Le Grader lit les informations, compile et exécute le code dans un conteneur Docker.
4. Il compare les sorties aux résultats attendus.
5. Il stocke les résultats (succès, erreurs, logs, messages) dans un fichier ou une base.

## 🔒 Sécurité

* Tous les codes sont exécutés dans des conteneurs Docker isolés.
* Les tests sont immuables et non modifiables par les utilisateurs.
* Les soumissions peuvent être authentifiées via des clés API (pour usage en mode déployé).

## 📌 Remarques

* Le fichier de tests est généré une seule fois à la création de l'exercice.
* Le code utilisateur est récupéré via un chemin local pour l'instant (plus tard via API).
* Le Grader est déployable en plusieurs instances pour distribuer la charge.

---

Ce Grader est conçu pour être l'élément technique central de l'automatisation de correction dans une plateforme d'apprentissage de la programmation.
