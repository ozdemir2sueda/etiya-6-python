# İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturun. Örnek: [ 1, 1, 2, 3, 5, 8, 13, 21, 34..... ]
# Fibonacci Serisi : Serideki her bir sayı kendisinden önceki iki sayının toplamına eşittir.


#  Bir sayının kendi hariç tüm bölenlerinin toplamı eğer kendisine eşitse bu Mükemmel Sayıdır. Örnek: 1 + 2 + 3 = 6
# Kullanıcıdan aldığı sayıyının mükemmel olup olmadığını söyleyen bir program yazın. 

fibnc=[]

a1=1
a2=1
a3=a1+a2

while a3< 20:

 a1=a2
 a2=a3
 fibnc.append(a3)

print(fibnc)


# for ilkeleman in range(20):
#     ilkeleman=1
    



# a = 0
# b = 1
# c = 0
# print("Bir değer giriniz : ", end="")
# n = int(input())
# print("\nFibonacci Serisi :", a, b, end=" ")
# c = a+b
# n = n-2
# while n>0:
#     print(c, end=" ")
#     a = b
#     b = c
#     c = a+b
#     n = n-1



#1 1 2 3 5 8 13
#Fibonacci dizisini n nci terime kadar görüntüleyen program, burada n kullanıcı tarafından sağlanır


# farklı bir sonuç için bu değeri değiştirin
nterms = 20

# eğer terimi kullanıcının belirlemesini isterseniz alttaki satırın başındaki # işareti kaldırın
#nterms = int(input("Kaç terime kadar? "))

# İlk iki terim
n1 = 0
n2 = 1
count = 0
toplam =0

# Buraa girilen terimin geçerli olupğ oladığını kontrol ediyoruz.
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       if(n1%2==0):
           toplam =toplam + n1
       nth = n1 + n2
       # değeri güncelliyoruz
       n1 = n2
       n2 = nth
       count += 1

print("toplam . " ,toplam)



list = [] 
a = 1
b = 0
c = 0
while len(list)<20: 
    c = a+b
    a = b
    b = c
    list.append(b) 
print(list)

#  Bir sayının kendi hariç tüm bölenlerinin toplamı eğer kendisine eşitse bu Mükemmel Sayıdır. Örnek: 1 + 2 + 3 = 6
# Kullanıcıdan aldığı sayıyının mükemmel olup olmadığını söyleyen bir program yazın. 

sayi = int(input("Bir Sayı Giriniz:"))
toplam=0
for i in range(1,sayi): 
    if(sayi%i == 0): 
        toplam +=i 
        
if(sayi == toplam): 
    print(sayi,"-> Mükemmel Sayıdır.") 
else:
    print(sayi,"-> Mükemmel Sayı Degildir")