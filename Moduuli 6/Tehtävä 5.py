def karsi_parilliset(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 ==0:
            parilliset.append(luku)
    return parilliset

def alkuperäiset():
    alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    karsittu_lista = karsi_parilliset(alkuperäinen_lista)
    print ("Alkkuperäinen lista:", alkuperäinen_lista)
    print("Karsittu lista:", karsittu_lista)

