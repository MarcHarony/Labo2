import re
def verif(regexLignes, regexColonnes, solutions) :
    assert (len(regexLignes) == len(solutions))
    n=0
    m=0
    correct = True
    while n<len(solutions) :
        p = re.compile(regexLignes[n])
        if p.match(solutions[n]) is None :
            correct = False
        n+=1
    print(correct)
    solutionColonne = ['']
    while m<len(solutions)-1 :
        for solution in solutions :
            solutionColonne[m] += solution[m]
        m+=1
    for truc in solutionColonne :
        print(solutionColonne)
verif (['[1-9][a-z]','[a-z][1-9]'],['\d','\d'],['5a', 'b9'])

