
dongu=1
while dongu==1:
    print("1-İkilik tabandan onluk tabana cevirme")
    print("2-Onluk tabandan ikilik tabana cevirme")
    print("3-Çıkış yap")
    secim=int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if secim==1:
        sayi=input("Sayi giriniz:")

        for i in sayi:
            if i != "0" and i != "1":
                durum = 0
                print("Girdiginiz sayi ikilik tabana uygun degil!!")
                uygun=True
                break
            durum = 1
        if durum==1:
            count=0
            for k in sayi:
                count+=1
            us=0
            kalan=0
            sum=0
            while us<count:
                sayi = int(sayi)
                kalan=(sayi%10)
                sum=kalan*(2**us)+sum
                us+=1
                sayi=sayi-kalan
                sayi=sayi//10
            print("ONLUK TABANA CEVRILMIS SAYI= ",sum)

    elif secim==2:
        cevir = " "  #ikilik tabana cevirmek icin bos bir karakter dizisi tanimladik
        sayi = int(input("Sayi giriniz:"))
        while sayi!=0:
            cevir = str(sayi % 2) + cevir
            sayi=sayi//2
        print("IKILIK TABANA CEVRILMIS SAYI=",cevir)
    else:
        dongu=0
        print("ÇIKIŞ YAPTINIZ!")