#değişkenler

haber="haberiniz olsun"
print(haber)

x="haberiniz olsun"
print(x)

baslik= "haberiniz olsun"
vade=12 #int
faizoranı1= 1.47 #float
faizoranı2= 1.44 #float


print(baslik)
print(type(baslik))
print(type(faizoranı1))

mesaj="hoşgeldin"

kullanıcıAdı = "süeda"

kullanıcısoyadı = "özdemir"

print(mesaj+""+kullanıcıAdı+kullanıcısoyadı) #2str yan yana topladı

sonucmesajı=(mesaj+""+kullanıcıAdı+kullanıcısoyadı) #2str yan yana topladı

print(sonucmesajı)

sayı1= 10
sayı2= 20

print(sayı1+sayı2)

print(sonucmesajı)

#LİSTELER

krediler=["hızlı kredi","maaşını halkbank'tan alanlar","mutlu emekli ihtiyaç kredisi"]
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])


print(len(krediler)) #length
krediler[0]="çabuk kredi"
print(krediler)
#print(krediler[5])




#ŞARTBLOKLARI

dolarDun=19.03
dolarBugun=19.03
if dolarDun>dolarBugun:
  print("azalış oku")
  print("bitti")
elif dolarDun<dolarBugun:
  print("artış oku")
  
else:
  print("eşittir oku")
  print("bitti")
  
  
#if dolarDun<dolarBugun:
  #print("artış oku")
#if dolarDun==dolarBugun:
  
  #print("eşittir oku")
  



#DÖNGÜLER


dolarDun=19.03
dolarBugun=19.03
if dolarDun>dolarBugun:
  print("azalış oku")
  print("bitti")
elif dolarDun<dolarBugun:
  print("artış oku")
  
else:
  print("eşittir oku")
  print("bitti")
  
  
#if dolarDun<dolarBugun:
  #print("artış oku")
#if dolarDun==dolarBugun:
  
  #print("eşittir oku")
  



#FONKSİYONLAR

#print("İlk Sayfa")

#krediler=["hızlı kredi","maaşını halkbank'tan alanlar","mutlu emekli ihtiyaç kredisi"]
#for kredi in krediler:
  #print("<option>"+kredi+"<option>")

#print("İkinci Sayfa")

#krediler=["hızlı kredi","maaşını halkbank'tan alanlar","mutlu emekli ihtiyaç kredisi"]
#for kredi in krediler:
  #print("<option>"+kredi+"<option>")


#print("Üçüncü Sayfa")

#krediler=["hızlı kredi","maaşını halkbank'tan alanlar","mutlu emekli ihtiyaç kredisi"]
#for kredi in krediler:
  #print("<option>"+kredi+"<option>")


#fonksiyon oluşturmak için def kullanırız;
def kredilerilistele():


  krediler=["hızlı kredi","maaşını halkbank'tan alanlar","mutlu emekli ihtiyaç kredisi"]
  for kredi in krediler:
    print("<option>"+kredi+"<option>")

kredilerilistele()
