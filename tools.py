def my_input(texte, valeur_defaut=0):
    valeur=" "
    while valeur.isdigit() == False:
        print(texte, end="")
        valeur = input()
        if valeur == "":
            return valeur_defaut
        if valeur.isdigit():
            return int(valeur)