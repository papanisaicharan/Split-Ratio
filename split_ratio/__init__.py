import math

# Version of split_ratio package
__version__ = "1.0.0"


def info(D):
    categories = set(D)
    freqofcategories = dict()
    for i in D:
        if i not in freqofcategories:
            freqofcategories[i] = 0
        freqofcategories[i] = freqofcategories[i] +1
    sum = 0.0
    for x in freqofcategories:
        interm = (freqofcategories[x]/len(D))
        sum = sum-(interm*math.log(interm,2))
    return(float(sum))


def infoofDA(freqofcategoriesDina,total):
    sum = 0.0
    for i in freqofcategoriesDina:
        if i > 0:
            interm = (i/total)
            sum = sum-(interm*  math.log(interm,2))
    return(float(sum))


def infoA(a,D):
    categoriesD = list(set(D))
    categories = set(a)
    freqofcategoriesDwitha = dict()
    for i in categories:
        freqofcategoriesDwitha[i] = [0]*len(categoriesD)
    freqofcategories = dict()
    count = 0
    for i in a:
        if i not in freqofcategories:
            freqofcategories[i] = 0
        freqofcategories[i] = freqofcategories[i] + 1
        freqofcategoriesDwitha[i][categoriesD.index(D[count])] +=1
        count = count+1
    sum = 0.0
    for x in freqofcategories:
        interm = (freqofcategories[x]/len(D))
        sum = sum+(interm*infoofDA(freqofcategoriesDwitha[x],freqofcategories[x]))
    return(float(sum))
    
def info_gain(A,D):
    return(info(D)-infoA(A,D))


def split_infoA(a):
    categories = list(set(a))
    freqofcategories = dict()
    for i in a:
        if i not in freqofcategories:
            freqofcategories[i] = 0
        freqofcategories[i] = freqofcategories[i] + 1
    # print(freqofcategories)
    sum = 0
    for x in freqofcategories:
        interm = (freqofcategories[x]/len(a))
        # print(freqofcategories[x],len(a))
        sum = sum-((interm)*math.log(interm,2))
    return(float(sum))


def gain_ratio(a,D):
    p=float(info(D) - infoA(a,D))
    if p == float(0) and split_infoA(a) != float(0.0):
        return 0.0
    elif p == float(0) and split_infoA(a) == float(0.0):
        return("indeterminate form(0/0)")
    else:
        return p/split_infoA(a)
    
    