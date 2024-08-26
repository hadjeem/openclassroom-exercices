# Écrivez votre code ici !
from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

title = soup.title.string
h1_text = soup.h1.string
products = soup.find_all('li')
products_list = []
for product in products:
    name = product.h2.string
    price = product.find('p', string=lambda s: 'Prix' in s).string
    products_list.append((name, price))

descriptions_list = []
for product in products:
    description = product.find('p', string=lambda s: 'Description' in s).string
    descriptions_list.append(description)

print(f"Titre de la page :{title}")
print("Texte de la balise h1 :", h1_text)
print("Liste des produits :", products_list)
print("Liste des descriptions de produits :", descriptions_list)

for i, (name, price) in enumerate(products_list):
    # filtre applique la première fonction au deuxième argument
    euro_price_str = ''.join(filter(str.isdigit, price.split()[2])) 
    euro_price = int(euro_price_str)
    dollar_price = euro_price * 1.2
    products_list[i] = (name, f"{dollar_price}$")

print("Liste des produits :", products_list)