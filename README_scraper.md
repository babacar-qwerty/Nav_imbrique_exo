# Scraper de Citations — quotes.toscrape.com

Script Python qui scrape automatiquement toutes les citations du site [quotes.toscrape.com](https://quotes.toscrape.com) et les stocke en mémoire.

---

## Fonctionnement

1. Parcourt toutes les pages du site en suivant la pagination automatiquement
2. Pour chaque page, récupère toutes les citations et leurs auteurs
3. Stocke chaque citation dans une liste sous forme de dictionnaire
4. Affiche le nombre de citations trouvées par page
5. S'arrête automatiquement quand le bouton "Next" disparaît (dernière page atteinte)

---

## Exemple de sortie

```
Page 1 — 10 quotes
Page 2 — 10 quotes
Page 3 — 10 quotes
...
Page 10 — 10 quotes
We have 100 quotes for 10 pages
```

---

## Structure des données

Chaque citation est stockée dans `all_quotes` sous cette forme :

```python
{
    'quote': "The world as we have created it...",
    'author': "Albert Einstein"
}
```

---

## Logique de pagination

```
Page 1 → scrape → bouton Next présent ? → Page 2
Page 2 → scrape → bouton Next présent ? → Page 3
...
Page N → scrape → bouton Next absent   → STOP
```

---

## Technologies utilisées

- **Python 3**
- `requests` — récupération du contenu HTML des pages
- `BeautifulSoup` — parsing et extraction des données HTML
- `lxml` — parser HTML rapide utilisé par BeautifulSoup

## Installation des dépendances

```bash
pip install requests beautifulsoup4 lxml
```
