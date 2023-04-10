ustlimit= int(input("üst limit giriniz"))

for ciftSayi in range(0, ustlimit, 2): 
  print(ciftSayi)

altlimit= int(input("alt limit giriniz"))

for ciftSayi in range(altlimit,ustlimit):
   if ciftSayi%2==0:
    print(ciftSayi)


   # fibonacci

fibonacciList=[]
a=1
b=0
toplam=0 
for i in range(20):
    toplam=a+b
    a=b
    b=toplam
    fibonacciList.append(toplam)
print(fibonacciList)


# mükemmel sayi

sayi=int(input("Sayı Giriniz: "))
toplam=0
for i in range(1,sayi):
    if sayi%i==0:
        toplam+=i

if toplam==sayi:
    print("Bu mükemmel sayıdır")
else:
    print("Mükemmel sayı değildir")