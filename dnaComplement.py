import unittest

def DNA_strand(dna):
    dnaList = list(dna)
    complementList = []
    for d in dnaList:
        if d == 'A':
            complementList.append('T')
        if d == 'T':
            complementList.append('A')
        elif d != 'A' and d != 'T':
            if d == 'C':
                complementList.append('G')
            if d == 'G':
                complementList.append('C')
        complement = ''.join(complementList)
    return complement


case1 = DNA_strand("AAAA")
case2 = DNA_strand("ATTCG")
case3 = DNA_strand("GTAT")
case4 = DNA_strand("AGAGAGCGTGA")

print (case1, case2, case3, case4)

def test_DNA_strand():
    assert DNA_strand("AAA") == "TTT"
    assert DNA_strand("ATTCG") == "TAAGC"
    assert DNA_strand("GTAT") == "CATA"
    assert DNA_strand("AGAGAGCGTGA") == "TCTCTCGCACT"

test_DNA_strand()





