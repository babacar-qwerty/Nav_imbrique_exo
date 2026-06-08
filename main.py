# ============================================================
# SCRIPT : Scraper de livres — books.toscrape.com
# ============================================================
# Ce script récupère les informations des 1000 livres du site
# books.toscrape.com et les stocke dans une base de données SQLite.
#
# ÉTAPES :
# 1. Connexion à la base de données books.db (créée si inexistante)
# 2. Création de la table Books (titre, prix, description)
# 3. Parcours des 50 pages du catalogue via pagination automatique
# 4. Pour chaque livre sur la page :
#       - Récupération du lien vers la fiche produit
#       - Entrée dans la fiche pour extraire le titre, le prix
#         et la description
#       - Insertion dans la base de données (doublons ignorés)
# 5. Arrêt automatique quand le bouton "next" disparaît
#
# RÉSULTAT : 1000 livres enregistrés dans books.db
# ============================================================

from bs4 import BeautifulSoup
import lxml
import requests
import sqlite3


page=1
count=1

# Création de la base de données:
db=sqlite3.connect("books.db")
cursor=db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
               titre TEXT,
               prix REAL,
               description TEXT UNIQUE)""")
# Parcourir toutes les pages:
while 1:
    base_url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    html_text= requests.get(base_url).text
    soup = BeautifulSoup(html_text,'lxml')
    article = soup.find_all('article', class_='product_pod')
    next_btn=soup.find('li', class_='next') 

    # Arrêter la boucle quand le bouton next disparait:
    if next_btn is None:
        break

    # Récupérer tous les href vers les pages de description
    for each in article:
        href= each.a['href']
        # url de la page descriptive
        full_url= 'https://books.toscrape.com/catalogue/'+ href
        # recup le html de la page descriptive
        desc_html= requests.get(full_url).text
        desc_soup=BeautifulSoup(desc_html,'lxml')

        # récupérer le titre:
        prod_title=desc_soup.find('h1').text
        # récupérer le prix:
        prod_price=desc_soup.find('p',class_='price_color').text[1:]
        # print(prod_price)
        # prends seulement la balise <p> de la description
        prod_desc=desc_soup.find_all('p')[3].text

        # Lié a la base de données
        cursor.execute("""
            INSERT OR IGNORE INTO Books(titre,prix,description)
            VALUES(?,?,?)""", (prod_title,prod_price,prod_desc))
        db.commit()
        print(f"---!!!Élément N°{count}  enregistré!!!---")
        count+=1
        print()

        # print(len(href))
    

    page+=1

print(f"Il y'a {page} pages!")
db.close()
