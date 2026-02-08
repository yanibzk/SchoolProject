# Créé par yanibenarezki et thomas Da silva, le 09/02/2025 en Python 3.7
import random # Pour choisir au hasard

caractères_interdits = {"é":"e","è":"e","ê":"e",
                        "à":"a","â":"a",
                        "ç":"c"}

# Affichage du titre "PENDU" en rouge
print("\033[91m" + """

██████╗ ███████╗███╗   ██╗██████╗ ██╗   ██╗
██╔══██╗██╔════╝████╗  ██║██╔══██╗██║   ██║
██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║   ██║
██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║
██║     ███████╗██║ ╚████║██████╔╝╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝
""" + "\033[0m")
#Instructions du jeu
print("\nBienvenue dans le jeu du PENDU !")
print("Devinez le mot mystère en proposant des lettres.")
print("Vous avez droit à 6 ou 8 erreurs en fonction du mode de difficulté avant que le pendu soit complètement dessiné.")
print("Bonne chance !\n")



def choix_mot_mystere():
    """fonction qui permet de choisir aléatoirement un mot parmi ceux d’un dictionnaire
    renvoi:str
    """
    l=[]
    base_python = open("mots_conjugaison.txt", "r", encoding="utf-8")  # Ouvre le fichier "mot_conjugaison.txt" en mode lecture
    L_lignes = base_python.readlines() # Lit toutes les lignes du fichier et les stocke dans une liste
    for i in range (len(L_lignes)) :# Parcourt chaque ligne du fichier
        l.append(L_lignes[i][0:(len(L_lignes[i])-1)])
    base_python.close()# Ferme le fichier
    return random.choice(l) # Choisit un mot au hasard

def correction_mot(l):
    """permet de supprimer et de remplacer du mot tiré, les caractères
    interdits par le jeu
    l: str
    renvoi:str
    """
    mot="" # contiendra le mot corrigé
    for i in l:
        if i in caractères_interdits:
            """ vérifie si le caractère du mot est
            dans le dictionnaire des caractères interdits"""
            mot= mot + caractères_interdits[i]
            #ajoute le caractère corrigé correspondant
        else:
            mot = mot + i
            # le caractère ne doit pas être corrigé on peut l'ajouter au mot
    return mot


def jouer_pendu(mot, mot_mystere, lettre):
    """Fonction qui vérifie si la lettre saisie par le joueur est présente dans le mot mystère
    et met à jour la représentation du mot.
    mot:list
    mot_mystere:list
    lettre:str
    renvoi:list
    """
    for i in range(len(mot_mystere)):  # Parcourt chaque lettre du mot mystère
        if mot_mystere[i] == lettre:  # Vérifie si la lettre devinée est correcte
            mot[i] = lettre  # Remplace "_" par la lettre trouvée

    return mot  # Retourne la version mise à jour du mot en cours de découverte


def mot_trouve(mot, mot_mystere):
    """fonction qui permet de savoir si le joueur a trouvé le mot ou pas
    mot:list
    mot_mystere:list
    renvoi:bool
    """
    return mot == mot_mystere # Vérifie si l'état actuel du mot découvert correspond au mot mystère complet



def afficher_pendu(erreurs, max_erreurs):
    """Affiche le bonhomme du pendu en fonction du nombre d'erreurs possibles.
    erreurs:int
    max_erreurs:int
    """
    rouge = "\033[91m"  # Code couleur pour rouge
    jaune = "\033[93m"  # Code couleur pour jaune
    reset = "\033[0m"   # Code couleur pour réinitialiser
    # Graphiques du pendu pour 6 erreurs possibles
    pendu_6 = [
        jaune + """
        +----+
        |    |
             |
             |
             |
             |
        ========
        """ + reset,
        jaune + """
        +----+
        |    |
        O    |
             |
             |
             |
        ========
        """ + reset,
        jaune + """
        +----+
        |    |
        O    |
        |    |
             |
             |
        ========
        """ + reset,
        rouge + """
        +----+
        |    |
        O    |
       /|    |
             |
             |
        ========
        """ + reset,
        rouge + """
        +----+
        |    |
        O    |
       /|\\   |
             |
             |
        ========
        """ + reset,
        rouge + """
        +----+
        |    |
        O    |
       /|\\   |
       /     |
             |
        ========
        """+ reset,
        rouge+"""
        +----+
        |    |
        O    |
       /|\\   |
       / \\   |
             |
        ========
        """+reset

    ]
        # Graphiques du pendu pour 8 erreurs possibles
    pendu_8 = [
        jaune + """
        +----+
        |    |
             |
             |
             |
             |
        ========
        """ + reset,
        jaune + """
        +----+
        |    |
        O    |
             |
             |
             |
        ========
        """ + reset,
        jaune + """
        +----+
        |    |
        O    |
        |    |
             |
             |
        ========
        """ + reset,
        jaune + """
        +----+
        |    |
        O    |
       /|    |
             |
             |
        ========
        """ + reset,
        rouge + """
        +----+
        |    |
        O    |
       /|\\   |
             |
             |
        ========
        """ + reset,
        rouge + """
        +----+
        |    |
        O    |
       /|\\   |
        |    |
             |
        ========
        """ + reset,
        rouge + """
        +----+
        |    |
        O    |
       /|\\   |
        |    |
       /     |
        ========
        """ + reset,
        rouge + """
        +----+
        |    |
        O    |
       /|\\   |
        |    |
       / \\   |

        ========
        """ + reset,
        rouge + """
        +----+
        |    |
       [X]   |
       /|\\   |
        |    |
       / \\   |
        ========
        """ + reset  # Schéma avec la tête morte
    ]

    # Choisit l'index approprié dans la liste en fonction du nombre d'erreurs
    if max_erreurs == 6:  # Si la difficulté est définie à 6 erreurs
        index = min(erreurs, 6)  # On choisit un index entre 0 et 6, mais ne dépasse pas 6
        print(pendu_6[index])  # Affiche le graphique du pendu pour 6 erreurs possibles
    else:  # Sinon la difficulté est définie à 8 erreurs
        index = min(erreurs, 8)  # On choisit un index entre 0 et 7, mais ne dépasse pas 7
        print(pendu_8[index])  # Affiche le graphique du pendu pour 8 erreurs possibles

    # Avertit le joueur s'il est proche de perdre
    if erreurs == max_erreurs - 1:
        print("⚠️  DERNIÈRE CHANCE !")  # Affiche un message de dernière chance si l'erreur suivante sera fatale
    elif erreurs >= max_erreurs:  # Si le joueur a atteint ou dépassé le nombre d'erreurs autorisées
        print("💀 GAME OVER !")  # Affiche un message de fin de partie

def affiche_mot(mot_tab):
    """Affiche le mot en cours de découverte avec des caractères séparés par un espace.
    mot_tab:list
    """
    for l in mot_tab:# On parcourt chaque élément de la liste mot_tab
        print (l , end=" ")  # Affiche les caractères de la liste côte à côte, séparés par un espace.



def afficher_lettres_proposees(lettres_t):
    """Affiche les lettres déjà proposées par le joueur.
    lettres_t: list
    """
    print(f"Lettres déjà proposées : {' '.join(sorted(lettres_t))}")  # Trie et affiche les lettres proposées

def ajouter_si_pas_dedans(liste, element):
    """Ajoute un élément à une liste uniquement s'il n'est pas déjà présent.
    liste:list
    element:str
    """
    trouve = False  # Variable qui sera utilisée pour vérifier si l'élément est déjà dans la liste
    for item in liste:  # On parcourt tous les éléments de la liste
        if item == element:  # Si l'élément est trouvé dans la liste
            trouve = True  # On marque que l'élément est déjà dans la liste
            break  # On arrête de chercher dès qu'on trouve l'élément
    if not trouve:  # Si l'élément n'est pas trouvé dans la liste
        liste.append(element)  # On ajoute l'élément à la liste

def est_valide(lettre):
    """ Vérifie si une lettre est valide (une seule lettre et dans l'alphabet).
    lettre:str
    renvoi:bool
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Définition de l'alphabet valide
    if len(lettre) != 1:  # Si la lettre n'est pas une seule lettre
        return False  # Ce n'est pas valide
    for l in lettre:  # Parcours chaque caractère de la lettre
        if l not in alphabet:  # Si le caractère n'est pas dans l'alphabet
            return False  # Ce n'est pas valide
    return True  # La lettre est valide si elle est dans l'alphabet et est une seule lettre

def jouer():
    """Fonction principale pour jouer au jeu du pendu.
    Le joueur doit deviner un mot en entrant des lettres une par une.
    La partie prend fin lorsque le joueur gagne (devine toutes les lettres du mot) ou perd (atteint le nombre maximum d'erreurs).
    """
    global max_erreurs  # Déclare la variable max_erreurs comme globale pour qu'elle soit modifiée dans cette fonction

    mode = input("\nChoisissez un mode : Facile (8 erreurs) / Difficile (6 erreurs) : ").lower()
    # Demande à l'utilisateur de choisir un mode de difficulté

    while mode not in ["facile","Facile","Difficile", "difficile"]:  # Vérifie que l'entrée est valide
        mode = input("Veuillez choisir un mode valide : Facile (8 erreurs) / Difficile (6 erreurs) : ").lower()

    if mode == "facile":
        max_erreurs = 8
    else:
        max_erreurs = 6
    # Définit le nombre d'erreurs maximum en fonction du mode choisi

    # Choisit un mot mystère et le corrige si nécessaire
    mot = correction_mot(choix_mot_mystere())  # La fonction 'choix_mot_mystere' choisit un mot, 'correction_mot' le corrige

    mot_tab = ["_" for _ in mot]  # Représente le mot sous forme de "_" à deviner

    erreurs = 0  # Compteur d'erreurs

    lettres_t = []  # Liste des lettres déjà proposées par le joueur


    # Boucle principale du jeu : continue tant qu'il reste des erreurs possibles et des "_" à deviner
    while erreurs < max_erreurs and "_" in mot_tab:
        print("\nMot actuel : ", end="")
        affiche_mot(mot_tab)  # Affiche le mot avec les lettres devinées et les "_"
        afficher_lettres_proposees(lettres_t)  # Affiche les lettres déjà proposées
        print(f"Erreurs restantes : {max_erreurs - erreurs}")  # Affiche le nombre d'erreurs restantes

        # Demande à l'utilisateur de saisir une lettre
        lettre = input("Entrez une lettre : ").lower()

        # Vérifie si la lettre est valide en utilisant la fonction est_valide
        if not est_valide(lettre):
            print("⚠ Erreur : Vous devez entrer UNE seule lettre valide !")
            continue  # Si l'entrée est invalide, on recommence la boucle

        # Vérifie si la lettre a déjà été proposée
        if lettre in lettres_t:
            print("Lettre déjà proposée.")
            continue  # Si la lettre a déjà été proposée, on recommence la boucle
        lettres_t.append(lettre)  # Ajoute la lettre à la liste des lettres proposées

        # Si la lettre est présente dans le mot, on met à jour l'affichage du mot
        if lettre in mot:
            jouer_pendu(mot_tab, mot, lettre)
        else:
            erreurs=erreurs+1  # Si la lettre n'est pas dans le mot, on incrémente le compteur d'erreurs

        # Affiche l'état actuel du pendu en fonction du nombre d'erreurs
        afficher_pendu(erreurs, max_erreurs)

    # Vérification de la fin de la partie
    if "_" not in mot_tab:  # Si le joueur a deviné toutes les lettres du mot
        print("\n🎉 Bravo ! Vous avez gagné ! Le mot était :", mot)
    else:  # Si le joueur a perdu en atteignant le nombre maximal d'erreurs
        print("\n❌ Dommage... Vous avez perdu ! Le mot était :", mot)

    # Demande au joueur s'il souhaite rejouer
    rejouer = input("\nVoulez-vous rejouer ? (oui/non) : ").lower()
    while rejouer not in ["oui", "non"]:  # Si la réponse n'est pas valide, on redemande
        rejouer = input("Réponse invalide. Voulez-vous rejouer ? (oui/non) : ").lower()
    if rejouer == "oui":  # Si le joueur veut rejouer, on relance la fonction jouer
        jouer()
    else:
        print("\nMerci d'avoir joué ! À bientôt. 👋")  # Message de fin si le joueur ne veut pas rejouer

# Lance le jeu
jouer()
