# Créé par yanibenarezki, le 26/11/2024 en Python 3.7
def interets(s,t,n):
    """ fonction qui  permet de calculer les intérêts perçus chaque année sur
    une somme déposée à un certain taux.
    s:float
    t:float
    n:int
    renvoi:tableau de flottants
    """
    interets_annuels = [] # Initialisation d'une liste pour stocker les resultats
    for i in range(1,n+1): # Parcours chaque année de 1 à n inclus
        inter=s*(t/100) # Calcule les intérêts
        s=s+inter # Ajout des intérêts au montant initial pour cette année
        interets_annuels.append(inter)# ajout de la valeur des intérêts dans notre liste
    interets_annuels.append(s)# ajout de la somme finale présente sur le livret
    return interets_annuels # Retourne la liste des montants cumulés

def interets_cumules(s,t,n):
    """fonction qui permet de connaitre le montant total des intérêts perçus
    pour une somme initiale ,un taux d'intérêts, et un nombre d'années.
    s:float
    t:float
    n:int
    renvoi:float
    """
    intercumules=0 # Initialisation du compteur pour additioner tous les intérêts
    for i in range (1,n+1):# Parcours chaque année de 1 à n inclus
        inter=s*(t/100) # Calcule les intérêts
        s=s+inter# Ajout des intérêts au montant initial pour cette année
        intercumules=intercumules+inter # addition de tous les intérêts perçus chaque année
    return intercumules



