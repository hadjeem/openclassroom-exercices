def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    nombre_a_gauche = input("Entrez un nombre entier : ")
    nombre_a_droite = input("Entrez un nombre entier : ")
    symbole = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/'] : ")
    result = 0
    
    if not nombre_a_droite.isnumeric or not nombre_a_gauche.isnumeric: 
        print("les 2 nombres ne sont pas des entiers")
    else: 
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)
        
        match symbole :
            case "+":
                result = nombre_a_gauche + nombre_a_droite
            case "-":
                result = nombre_a_gauche - nombre_a_droite
            case "*":
                result = nombre_a_gauche * nombre_a_droite
            case "/":
                if nombre_a_droite == 0:
                    print("Erreur: impossible de diviser par zéro.")
                else:
                    result = nombre_a_gauche / nombre_a_droite
            case _:
                print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    
    print(f"Le résultat de l'opération est: {result}")


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()