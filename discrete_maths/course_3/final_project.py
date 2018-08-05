# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def stableMatching(n, menPreferences, womenPreferences):
# Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n                      
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n                      
    # Each man made 0 proposals, which means that 
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n                       
    
    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he=unmarriedMen[0]
#        print('he is',he)          
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]
#        print('his prefer',hisPreferences)
        # Find a woman to propose to
        for i in hisPreferences:
            she = i
#            print('she is',she)
        # Store her ranking in this variable for convenience
            herPreferences = womenPreferences[she]
#            print('her prefer',herPreferences)
        # Find the present husband of the selected woman (it might be None)
            currentHusband = womanSpouse[she]
#            print('her husban',currentHusband)
            if womanSpouse[she]==None or herPreferences.index(he)<herPreferences.index(currentHusband):
                manSpouse[he]=she
                womanSpouse[she]=he
                del unmarriedMen[unmarriedMen.index(he)]
#                print('husbands',womanSpouse)
                if currentHusband!=None:
                    unmarriedMen.insert(0,currentHusband)
                    manSpouse[currentHusband]=None
#                print(manSpouse,unmarriedMen)
                break
#                print(unmarriedMen)

                
        # Write your code here
        
        # Now "he" proposes to "she". 
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice
            
    # Note that if you don't update the unmarriedMen list, 
    # then this algorithm will run forever. 
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse
    
# You might want to test your implementation on the following two tests:
# assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
# assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])
print(stableMatching(1,[[0]],[[0]]))
print()
print(stableMatching(2,[[0,1],[1,0]],[[0,1],[1,0]]))
print()
print(stableMatching(2,[[0,1],[0,1]],[[1,0],[0,1]]))
print()
print(stableMatching(4,[[0,1,3,2],[0,2,3,1],[1,0,2,3],[0,3,1,2]],[[3,1,2,0],[3,1,0,2],[0,3,1,2],[1,0,3,2]]))







