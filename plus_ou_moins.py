import random

def my_input(texte, valeur_defaut=0):
    valeur=" "
    while valeur.isdigit() == False:
        print(texte, end="")
        valeur = input()
        if valeur == "":
            return valeur_defaut
        if valeur.isdigit():
            return int(valeur)

def initialisation():
    NbMin = my_input("Donnez le nombre min pour le nbre mystère (0 par défaut): ", 0)
    NbMax = my_input("Donnez le nombre max pour le nbre mystère (100 par défaut): ", 100)
    
    while NbMax < NbMin:
        NbMax = my_input("Le nombre max doit être supérieur à nombre "+ str(NbMin)+". Veuillez saisir un autre max:")
    return NbMin, NbMax

def jeu_1(NbMin, NbMax):
    """
    Programme du jeu où la personne cherche un nombre compris entre nb_min et nb_max.
    Pour se faire, le joueur propose des hypothèses et l'ordinateur répond s'il est inférieur,
    supérieur ou s'il correspond au nombre mystère.
    """
    NbMystère = random.randint(NbMin, NbMax)
    hypo = my_input("Donnez une hypothèse :")
    coup = 1
    while hypo != NbMystère:
        coup += 1
        if hypo > NbMystère:
            hypo = my_input("Trop grand. Hypothèse :")
        else:
            hypo = my_input("Trop petit. Hypothèse :")
    print("Coups :", coup)

def jeu_2(nb_min, nb_max):
    """
    Programme du jeu où la personne fait chercher à l'ordinateur un nombre compris entre nb_min et nb_max.
    Pour se faire, l'ordinateur propose des hypothèses au joueur qui répond 1, 2 ou 3 pour -, = ou +
    """
    input("Veuillez imaginer votre nombre mystère compris entre"+str(nb_min)+" et "+str(nb_max)+". Puis appuyez sur Entrée.")
    réponse = 0
    coup = 0
    print("Tapez : \n1 si votre nombre est plus élevé que la proposition\n2 si l'ordinateur à trouvé votre nombre\n3 si le nombre est moins élevé que la proposition.")
    while réponse !=2 and nb_min <= nb_max:
        hypothèse = (nb_min + nb_max)//2
        réponse = my_input("Je pense que c'est " + str(hypothèse)+" : ")
        coup += 1
        if réponse == 1:
            nb_min = hypothèse + 1
        elif réponse ==3:
            nb_max = hypothèse - 1
    
    # Teste si les bornes nb_min et nb_max ne se sont pas croisées.
    if nb_min <= nb_max:
        print("L'ordinateur a trouvé en", coup, "coups.")
    else:
        print("Votre nombre est compris entre", nb_min,"et", nb_max, "ou vous vous êtes trompé.")

# Corps principal
jeu = my_input("1 Jeu 1\n2 Jeu 2\n3 Règles\n")
while jeu !=2 and jeu != 1:
    texte = "Jeu 1: Le joueur cherche un nombre compris entre nb_min et nb_max. Pour se faire, le joueur propose des hypothèses et l\'ordinateur répond s'il est inférieur,\
             supérieur ou s\'il correspond au nombre mystère.\n\
             Jeu 2 : la personne fait chercher à l\'ordinateur un nombre compris entre nb_min et nb_max.\
             Pour se faire, l\'ordinateur propose des hypothèses au joueur qui répond 1, 2 ou 3 pour -, = ou +\
             Tapez 1 ou 2 :"
    jeu = my_input(texte)
nb_min, nb_max = initialisation()
if jeu == 1:
    jeu_1(nb_min, nb_max)
elif jeu == 2:
    jeu_2(nb_min, nb_max)
