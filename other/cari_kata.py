
def carikata():
    cari=''
    kata=''
    while(cari != 'exit'):
        kata = input("Masukan kalimat yang di inginkan : ")
        cari = input("Masukan kata yang dicari didalam kalimat :")
    
        cari=cari.lower()
        kata=kata.lower()
        
        if (cari=='exit'):
            print('good bye :)')
        else:
            if cari in kata:
                print('ada')
            else:
                print("tidak ada")
            print("ketik exit pada cari untuk keluar dari perulangan\n")
    
        
        
carikata()
