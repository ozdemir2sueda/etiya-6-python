
#1. ders
print("Merhaba Etiya")
print("hoş geldiniz")
#yorum satırı

# değişkenler-start lifecycle boyunca değişebilecektir.

#metinsel,numerk,objei
#programa text diye bir alan tanımladım. tanımladığım nıktadan itibaren kullanılır
text="merhaba"

print(text)

text="selam"

#text'in artık içinde tuttuğu ifade selam

studentCount="45"#string metinsel ifade
print(studentCount)
studentCount=45#int,integer tam sayı
print(studentCount+ 5)
averagePoint=25.5 #double, decimal, float ondalık sayı

isVerified=True #bool,boolean true veay false alıyor

print(isVerified)

print(type(averagePoint)) #hangi tipte yazdığını unuttun bu fonksiyon ile 
 
#değişkenler end
#operatörler

number=10 #matematiksel operatörler-mantıksal 

print(10+10)

print(number+number)

print(number -5)

print(number / 2) #bölüm işlemlerinde her zaman tam sayı olmayacağından float dönüyor. geriye

print(number * 5)

#mod operatörü sol taraftaki değerin sağa bölümünden kalanı veriyor

print(number % 3)

print(number + (10- number) * (5/10))
#operatörler-end

#mantıksal operatörler- karşılaştırma operatörleri bir değerin diğer değer ile eşit olduğı vs.

print(number == 10) #true gelir

print(number != 10)

print(10 != 10) #bu durum false döner iki taradın eşit olmamasını istiyor operatör o yuden false

print(11 != 10) #true değerini alırsın

print(number > 10) #false

print(number <= 10) #true

