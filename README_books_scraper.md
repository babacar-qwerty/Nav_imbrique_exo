# Scraper de Livres — books.toscrape.com

Script Python qui scrape les 1000 livres du site [books.toscrape.com](https://books.toscrape.com) et les stocke dans une base de données SQLite.

---

## Fonctionnement

1. Crée (ou ouvre) une base de données `books.db`
2. Crée la table `Books` si elle n'existe pas encore
3. Parcourt les 50 pages du catalogue via pagination automatique
4. Pour chaque livre, entre dans sa fiche produit pour extraire les détails
5. Insère chaque livre dans la base de données (les doublons sont ignorés)
6. S'arrête automatiquement quand le bouton "Next" disparaît

---

## Structure de la base de données

**Fichier :** `books.db`

**Table :** `Books`

| Colonne | Type | Description |
|---|---|---|
| `titre` | TEXT | Titre du livre |
| `prix` | REAL | Prix en £ |
| `description` | TEXT UNIQUE | Description du livre |

> `UNIQUE` sur la description permet d'ignorer les doublons avec `INSERT OR IGNORE`.

---

## Exemple de sortie

```
---!!!Élément N°1  enregistré!!!---
---!!!Élément N°2  enregistré!!!---
...
---!!!Élément N°1000  enregistré!!!---
Il y'a 50 pages!
```

---

## Logique de scraping

```
Page catalogue 1
    └── Livre 1 → fiche produit → titre, prix, description → INSERT en DB
    └── Livre 2 → fiche produit → titre, prix, description → INSERT en DB
    └── ...
Page catalogue 2
    └── ...
...
Page 50 → bouton Next absent → STOP
```

---

## Technologies utilisées

- **Python 3**
- `requests` — récupération du contenu HTML
- `BeautifulSoup` — parsing et extraction des données HTML
- `lxml` — parser HTML rapide
- `sqlite3` — stockage des données en base de données locale

---

## Installation des dépendances

```bash
pip install requests beautifulsoup4 lxml
```

> `sqlite3` est inclus nativement dans Python, aucune installation nécessaire.
