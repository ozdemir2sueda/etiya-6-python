#diziler-listeler-start

sayi1=1
sayi2=2 #şeklinde tanımlamıyorum liste yapıyorum


sayilar = [100,200,300,400,500, "merhabalar", 15.5,True] #listedeki veri tipi aynı olmak zorunda değil
print(sayilar)
#program saymaya 0dan başlar
#index indisi => 0

print(sayilar[1])
print(sayilar[5]) #merhaba yazmak için


#pembe cube fonksiyon, anahtar klas, proportyler klas içerisindeki değişkendir.
sayilar.append(100) #listemin sonuna 100 ekledi
sayilar.append(600)
#append fonksiyonu listenin sonuna eleman ekliyor
print(sayilar)
sayilar.pop() #index vermediğin durumda yani içine bir şey yazmazsan son satırı alıp siliyor son index dediğimiz -1 demektir. son elemanı işaret eder. listenin boyunu bilmiyoruz 
sayilar.pop(0) #ilk elemanı siliyor aralık veremiyoruz
print(sayilar)
sayilar.remove(100)#bulduğu ilk değeri siler. birden fazla kez 100 tekrar ediyor listemde en baştakini siliyor
sayilar.extend([700,800,900]) #liste halinde alıyor. 2 listeyi birleştiriyor. append de tek bir eleman eklerken bu listeyi ekliyor
print(sayilar)
sayilar.clear() #dizinin içini boşaltan fonksiyon

#diziler-listeler-end

#string interpolation-start

hello = "Merhabalar"
userName = "süeda"
print(hello + userName)
print(hello + " " +  userName) #yapmak yerine total text ile ekleyebilirsin
totalText = hello + " " +  userName
print(totalText)

totalText= "{message} Sayın {name}".format(message=hello, name=userName)

#f-string- en kolayı string interpolation

totalText= f"hoşgeldiniz {userName}"
print(totalText)

#string interpolation-end

#karar yapıları-start

ortalamaNot = input ("Lütfen ortalamanızı giriniz")
#yukardaki string yapıyı numerik olması gerekiyor. Stringden integer'a çevireceğiz.
#numerik => int,double

ortalamaNotAsInterger= int(ortalamaNot)

#if else blokları

#4 satır => 1 tab/indent

#1 indent içeriye alırsan o bloğa bağlı olduğu anlamına gelir girmezsen bloga girmez. kodu 
if ortalamaNot > 50:
    print("geçtiniz")
    if ortalamaNot > 80:
        print("başarili")
else:
    print("kaldiniz")

print("if blogundan bağımsız kısım")

#else if -> elif birden fazla kararı bağlama
if ortalamaNot > 80:
    print("bravo")

elif ortalamaNotAsInterger >60:
    print("ortalama")

studentCount = 40

if studentCount> 20:

    print("öğrenciler derse hazır")

vize= int(input("vize"))
final=int(input("final"))
ortalama =(vize*0.4) + (final*0.6)

if final < 40:
    print("kaldiniz")
    
elif ortalama < 50:
    print("kaldi")
elif vize == 2*final:

    print("kaldi")
else: 
    print("geçtiniz")

    
    

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.



