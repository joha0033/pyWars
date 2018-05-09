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
        print (complement)
    return complement

DNA_strand(dna = "AAAA")
DNA_strand("ATTCG")
DNA_strand("GTAT")
DNA_strand("AGAGAGCGTGA")