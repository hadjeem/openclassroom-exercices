def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    liste = input("Saisissez une liste de nombres séparés par des virgules : ")
    liste = liste.split(",")
    print("Liste des nombres :", liste)
    somme = 0
    for nombre in liste:
        somme += int(nombre)
    print("Somme des nombres :", somme)
    moyenne = somme / len(liste)
    print("Moyenne des nombres :", moyenne)
    nombre_sup_moyenne = 0
    for nombre in liste:
        if int(nombre) > moyenne:
            nombre_sup_moyenne += 1
    print("Nombre de nombres supérieurs à la moyenne :", nombre_sup_moyenne)
    nombre_pairs = 0
    for nombre in liste:
        if int(nombre) % 2 == 0:
            nombre_pairs += 1
    print("Nombre de nombres pairs :", nombre_pairs)


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()