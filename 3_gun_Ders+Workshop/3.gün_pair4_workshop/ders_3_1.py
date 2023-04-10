#döngüler

i=0
i<10 ==True
#iteration itereetmek üzerinde gezinmek
for i in range(0,10):
    print(i)

ogrenciler=["volkan","süeda","zühal","selen","ümit"]
#length

print(len(ogrenciler))

for i in range(len(ogrenciler)):
    print(f"{i+1}.öğrenci: {ogrenciler[i]}")
    

#break iligili alanı kırıyor.

for i in range(len(ogrenciler)):
    if i==3:
        break
    print(f"{i+1}.öğrenci: {ogrenciler[i]}")

#pass işleme sahip değil if yazdım ama içini boş burakmak isitiyorum pass ile hata almadan boş döngü dönüyor


#continue = o an döndü ne var ise onu atlayıp bir sonrakine geçiyor

for i in ogrenciler:
    if i=="volkan":
        continue
    print(f"öğrenci:{i}")


    #while infinite loop booleandeger 

while True: #control+c terminali durduruyor. sonsuza kadar merhaba yazabilir
        print("merhaba")


i=0

while i<10:
 if i==3:
    continue
    print("merhabalar")

i=0

while i<10:
 
 i=i+1
 if i==3:
    break
    print(f"while içerisindeki i değeri: {i}")
    
#döngüler end












# döngüler - loops -start

# i=0
# i<10 == True

# iterate etmek, iteration

for i in range(0,10):
    print(i)

ogrenciler = ["Volkan","Süeda","Zühal","Selen","Ümit"]
#length
print(len(ogrenciler))
# 5
# 0, 1, 2, 3, 4

#break => ilgili döngünün o anda kırılmasını (bitirilmesini) sağlar

for i in range(len(ogrenciler)):
    if i==3:
        break
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#pass => ilgili alanın bodysini boş bırakabilmemize olanak sağlar
for i in range(0,10):
    pass

#continue => iterasyondaki current değeri atla, bir sonraki değer ile devam et
for i in ogrenciler:
    if i=="Volkan":
        continue
    print(f"Öğrenci: {i}")


# while booleanDeger
#infinite loop - sonsuz döngü
# ctrl+c => terminali durduran manual işlem
i = 0
while i < 10:
    i = i + 1
    if i==3:
        break
    print(f"While içerisindeki i değeri: {i}")
    

# döngüler - loops -end