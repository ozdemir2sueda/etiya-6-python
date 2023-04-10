# #ödev çözüm notları
# #senin yaptığın

sayilar=[]
for i in range(10):
    i=int(input("sayi giriniz:"))
    sayilar.append(i)

print(sayilar)
enbuyukdegisken=max(sayilar)
print(enbuyukdegisken)


# #kulanıcıdan 10 adet sayı alalım ✅ #Döngü kullanman gerekiyor. 1 kod bloğu birden fazla kez çalıştırmak için kullanılır. konsola 10 kere tekrarlandı for kullan
# #ve bu sayılar arasından en büyük 2. olanı kullanıcıya gösterelim ✅
# #döngüler-loops
# #for loop
# # i=0 , i = i + 1
# # 0,1,2,3,4,5,6,7,8,9  < 10

# sayilar = []
# # 0 dan başlat, 10'dan küçük olana kadar döngüyü çalıştır, 
# # döngü her çalıştığında i değerini 1 artır
# for i in range(3):
#     sayilar.append(int(input(f"{i+1}. sayıyı giriniz: "))) #25
# sayilar.sort(reverse=True)
# enBuyukN = int(input("Sayılar arasından en büyük kaçıncı elemanı istiyorsun? "))
# print(sayilar[enBuyukN - 1])


# ## end
# #sayilar.sort(reverse=true) bu bizim listemizi sıralar. içine reverse=true dersek tam tersi kücüktan büyüge sıralar
# #enbyksayı=int(input(kaçıncı eleman istiyorsuzn?))
# #print(sayilar[enbyksayı -1])
# #biggestvalue=0
# #for i in range(10); range fonksiyonu 0dan başla 10dan küçük olana kadar çalış
# #sayı= int(input(f"{i+1}.sayı giriniz:"))
# # if sayi> biggestvalue:
# #biggestvalue=sayi
# #print(f"sayı gir:{biggestvalue}"")

#https://github.com/halit-kalayci-instruction/etiya-6-python


# # for ciftSayi in range(0, ustlimit, 2): 
# #   print(ciftSayi)

# # altlimit= int(input("alt limit giriniz"))

# # for ciftSayi in range(altlimit,ustlimit):
# #    if ciftSayi%2==0:
# #     print(ciftSayi)


#     # kullanıcı bir üst limit belirleyip 0 a kadar sayıp çift sayıları yazdıracağım
#     #döngü kullanacağız

#     forRange


# kullanıcın vereceği üst limit ile
# 0dan üst limite kadar olan tüm çift sayıları yazdıralım
#forRange = int(input("Üst limit belirleyiniz: "))
# for i in range(forRange+1):
#     if i % 2 == 0:
#         print(i)
#start => döngü kaç sayısından başlasından
#stop => döngü kaç sayısında son bulsun
#step => döngü kaç kaç artırılsın
#for i in range(0,forRange+1,2):
    #print(i)
## end


## 3. ister => 2. isterdeki alt limit kullanıcı belirlemelidir
forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))
for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print(i)
##end
