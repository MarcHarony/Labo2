import re
def verif(regexLignes, regexColonnes, solutions) :
    assert (len(regexLignes) == len(solutions))
    n=0
    m=0
    o=0
    q=0
    r=0
    correct = True
    while n<len(solutions) :
        p = re.compile(regexLignes[n])
        if p.match(solutions[n]) is None :
            return False
        n+=1
    solutionColonne = []
    nbrColonnes = len(solutions[0])
    while q<nbrColonnes :
        solutionColonne.append('') #crée une liste avec le nombre de colonnes
        q+=1
    while m<len(solutions[0]) :
        for solution in solutions : #pour chaque ligne
            solutionColonne[m]+=solution[m] #ajouter l element d indice m a la colonne m
        m+=1
    while r<len(solutionColonne) :
        p = re.compile(regexColonnes[r])
        if p.match(solutionColonne[r]) is None :
            return False
        r+=1
    return True
print(verif (['[1-9][a-z][a-z]','[a-z][1-9][0-9]'],['[0-9][a-z]|[a-z][0-9]','[0-9][a-z]|[a-z][0-9]','[0-9][a-z]|[a-z][0-9]'],['5ab', 'b98']))
print(verif (['[0-9]','[a-z]'],['[0-9][0-9]'],['5','a']))
