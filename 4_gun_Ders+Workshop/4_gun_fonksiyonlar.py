# def kredilerilistele():
#     krediler=["hızlı kredi", "maaşını halbanktan alanlara özel", "mutlu emeklilik"]
#     for kredi in krediler:
#         print("<option>"+ kredi +"<option>" )
# kredilerilistele()


# sayilar=[]

# for i in range(10):
#     i=int(input("sayi giriniz:"))
#     sayilar.append(i)
    
#     print(sayilar)
    
    
# enbuyukdegisken=max(sayilar)

# print(enbuyukdegisken)

# def fibonacci():

#     a=1
#     b=0
#     toplam=0 
#     for i in range(20):
#         toplam=a+b
#         a=b
#         b=toplam
#     print(toplam)
# fibonacci()

# def mükemmelsayı():
#    toplam=0
#    sayi = int(input("Bir Sayı Giriniz:"))
#     for i in range(1,sayi): 
#         if(sayi%i == 0): 
#             toplam +=i 
        
#     if(sayi == toplam): 
#         print(sayi,"-> Mükemmel Sayıdır.") 
#     else:
#          print(sayi,"-> Mükemmel Sayı Degildir")
# mükemmelsayı()


# def ciftsayı():
   
#     ustlimit= int(input("üst limit giriniz"))

#     for ciftSayi in range(0, ustlimit, 2): 
#         print(ciftSayi)

#     altlimit= int(input("alt limit giriniz"))

#     for ciftSayi in range(altlimit,ustlimit):
#         if ciftSayi%2==0:
#             print(ciftSayi)
# ciftsayı()



# def sayı():
#     sayilar = []

#     for i in range(10):
#         sayilar.append(int(input(f"{i+1}. sayıyı giriniz: "))) #25
#         sayilar.sort(reverse=True)
#         enBuyukN = int(input("Sayılar arasından en büyük kaçıncı elemanı istiyorsun? "))
#         print(sayilar[enBuyukN - 1])

# sayı()



   
def sayilar():
    ustlimit=int(input("Üst Limit Giriniz: "))
    altlimit=int(input("Alt Limit Giriniz: "))


    for ciftSayi in range(altlimit,ustlimit):
        if ciftSayi%2==0:
            print("Çift Sayilar : ", ciftSayi)
sayilar()

def buyukKucukSayi():
    sayilar = []

    for i in range(10):
        i= int(input(f"{i+1}. sayıyı giriniz: "))
        sayilar.append(i)


    print(sayilar)
    enBuyuk = max(sayilar)
    enKucuk = min(sayilar)
    print("Listedeki En Büyük Sayı : ", enBuyuk, "\nListedeki En Küçük Sayı : ", enKucuk)
buyukKucukSayi()


def fibonacciFonksiyon():

    fibonacciList = []
    birinciSayi = 0
    ikinciSayi = 1

    fibonacciList.append(birinciSayi)
    fibonacciList.append(ikinciSayi)

    alinanSayi=int(input("Merhaba 20 veya 20'den büyük bir sayi giriniz: "))

    if(alinanSayi<20):
        print("Yanlış değer girdiniz !! Lütfen 20 veya 20'den büyük bir sayı giriniz.")

    else:
        for i in range(alinanSayi):

            ucuncuSayi = birinciSayi + ikinciSayi
            birinciSayi = ikinciSayi
            ikinciSayi = ucuncuSayi

            fibonacciList.append(ucuncuSayi)
        print(fibonacciList)

fibonacciFonksiyon()


def mukemmelfonksiyon():

    sayi=int(input("Sayı Giriniz: "))
    toplam=0
    for i in range(1,sayi):
        if sayi%i==0:
            toplam+=i

    if toplam==sayi:
        print("Bu mükemmel sayıdır")
    else:
        print("Mükemmel sayı değildir")

mukemmelfonksiyon()