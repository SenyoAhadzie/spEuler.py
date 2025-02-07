import re
import numpy as np
from collections import OrderedDict

def find_last(lst, sought_elt):
    for r_idx, elt in enumerate(reversed(lst)):
        if elt == sought_elt:
            return len(lst) - 1 - r_idx
        
catLabels = ['a', 'b', 'c', 'd']
cats = ['a', 'b', 'c', 'd', \
        'ab', 'ac', 'bc', 'ad', 'bd', 'cd', \
        'abc', 'abd', 'acd', 'bcd', \
        'abcd']

def spEulerRankBasedDualConstruction(catLabels, cats):
    S = max([len(cat) for cat in cats])
    cats_S = [' '+ ' '.join([''.join(sorted(cat)) for cat in cats if len(cat)==s])+' ' for s in range(1,S+1)]
    cats_S_R = [[[''] for x in range(len(catLabels))]]
    cats_S_R_groupMappings = [[], []]
    for cat_S in cats_S:
        thisCats_R = [''] * len(catLabels)
        thisCats_R_flattened = []
        for j in range(len(catLabels)):
            if j==0:
                try:
                    thisCats_R[j] = [x.strip() for x in re.findall('(?<=\s)['+''.join(catLabels[:j+1])+']+\s+', cat_S)]
                    thisCats_R_flattened.extend(thisCats_R[j])
                except:
                    pass #thisCats_R[j] = ['']
            else:
                try:
                    thisCats_R[j]= [x.strip() for x in re.findall('(?<=\s)['+''.join(catLabels[:j+1])+']+\s+', cat_S) if x.strip() not in thisCats_R_flattened]
                    thisCats_R_flattened.extend(thisCats_R[j])
                except:
                    pass #thisCats_R[j] = ['']
            cats_S_R_groupMappings[0] = cats_S_R_groupMappings[0] + thisCats_R[j]
            cats_S_R_groupMappings[1] = cats_S_R_groupMappings[1] + ([j] * len(thisCats_R[j]))
        cats_S_R.append(thisCats_R)
    catLabelsExtended = catLabels + [catLabels[0]]
    cats_S_R_groupDict = dict(zip(cats_S_R_groupMappings[0], cats_S_R_groupMappings[1]))
    cats_ordered = []
    cats_ordered_withDuplicatedEndpoints = []
    cats_ordered_flattened = []
    for s in range(S+1):
        cats_ordered_S = []
        cats_ordered_S_flattened = []
        cats_ordered_S_withDuplicatedEndpoints = []
        if s==0 or s==1:
            for r in range(len(catLabels)):
                cats_ordered_S_flattened.extend(cats_S_R[s][r])
                cats_ordered_withDuplicatedEndpoints.extend(cats_S_R[s][r])
            cats_ordered_S.extend(cats_S_R[0])
            cats_ordered_S_withDuplicatedEndpoints.extend(cats_S_R[0])
        else:
            leftBoundaryWords = [''.join(sorted(set(cats_ordered_flattened[s-1][i]+cats_ordered_flattened[s-1][(i+1)%len(cats_ordered_flattened[s-1])]))) for i in range(len(cats_ordered_flattened[s-1]))] #[''.join(sorted(set(cats_ordered_S_flattened[s][i]+cats_ordered_S[s][i%len(cats_ordered_S_flattened[s])]))) for i in range(len(cats_ordered_S_flattened[s]))]
            leftBoundaryWordsExistIndices = [ind for (ind, lBW) in enumerate(leftBoundaryWords) if lBW in cats]
            leftBoundaryWordsExistGroupIndices = [cats_S_R_groupDict[leftBoundaryWords[ind]] for ind in leftBoundaryWordsExistIndices]
            for r in set(leftBoundaryWordsExistGroupIndices): 
                if leftBoundaryWordsExistGroupIndices.count(r)==1:
                    leftBoundaryWordsExistListPrefix = [leftBoundaryWords[leftBoundaryWordsExistIndices[leftBoundaryWordsExistGroupIndices.index(r)]]]
                    cats_ordered_S.append(list(OrderedDict.fromkeys(leftBoundaryWordsExistListPrefix + [cat_s_r for cat_s_r in cats_S_R[s][r] if cat_s_r not in leftBoundaryWordsExistListPrefix])))
                    cats_ordered_S_flattened.extend(cats_ordered_S[-1])
                elif leftBoundaryWordsExistGroupIndices.count(r)>1:
                    endGrouprVal = find_last(leftBoundaryWordsExistGroupIndices, r)
                    if endGrouprVal!=len(leftBoundaryWordsExistGroupIndices)-1:
                        leftBoundaryWordsExistListPrefix = [leftBoundaryWords[ind] for ind in leftBoundaryWordsExistIndices[leftBoundaryWordsExistGroupIndices.index(r):find_last(leftBoundaryWordsExistGroupIndices, r)+1]]
                        cats_ordered_S.append(list(OrderedDict.fromkeys(leftBoundaryWordsExistListPrefix + [cat_s_r for cat_s_r in cats_S_R[s][r] if cat_s_r not in leftBoundaryWordsExistListPrefix])))
                        cats_ordered_S_flattened.extend(cats_ordered_S[-1])
                    else:
                        leftBoundaryWordsExistListPrefix = [leftBoundaryWords[ind] for ind in leftBoundaryWordsExistIndices[leftBoundaryWordsExistGroupIndices.index(r):find_last(leftBoundaryWordsExistGroupIndices, r)]]
                        cats_ordered_S.append(list(OrderedDict.fromkeys(leftBoundaryWordsExistListPrefix + [cat_s_r for cat_s_r in cats_S_R[s][r] if cat_s_r not in leftBoundaryWordsExistListPrefix+[leftBoundaryWords[endGrouprVal]]]+[leftBoundaryWords[endGrouprVal]])))
                        cats_ordered_S_flattened.extend(cats_ordered_S[-1])
        cats_ordered.append(cats_ordered_S)
        cats_ordered_flattened.append(cats_ordered_S_flattened)
    cats_ordered_flattened[0] = ['']

    return cats_ordered_flattened

sampleCase_Fig3b = spEulerRankBasedDualConstruction(catLabels, cats)
