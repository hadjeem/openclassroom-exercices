# Ecrivez vos fonctions ici
def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

salaire_annuel = float(input("Saisissez le salaire annuel : "))
heures_travaillees = float(input("Saisissez le nombre d'heures travaillées par semaine : "))
salaire_mensuel = salaire_mensuel(salaire_annuel)
salaire_hebdomadaire = salaire_hebdomadaire(salaire_mensuel)
salaire_horaire = salaire_horaire(salaire_hebdomadaire, heures_travaillees)
print(f"Votre salaire horaire est de {salaire_horaire} euros.")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()