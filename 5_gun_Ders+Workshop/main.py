#Sınıflar => class
#modules
#paket yönetimi
#nesne yönelimi programlar içerisinde fonskiyon tanımlayacağız. nesnelere atama yapacağız.
#self ---this demek 

class Human:
    name="halit"
    #Built-in
    #construct: nesne üretilirken yapıcı blok 
    #initialize
    def __init__(self,name):
        self.name = name
        print("bir human instance üretildi")#yapıcı blok çalıştı. 
    def __str__(self) -> str:
        return f"srt fonksiyonunda dönen değer: {self.name}"
    
    def talk(self, sentence): #ilgili fonksiyonun tanımlandığı nesne
        print(f"{self.name} :{sentence}") #parametre kullanmak istediğim fonksiyonda sentence örneğin o zaman yukardaki sentence'e atadı merhaba'yı. self rezerve çünkü doluu.
#self.name dersen sen bu clas içerisindeki alandaki name kullan. name yazarsan kendi bloğunda def'e kadar ki kısmı arar.
    def walk(self):#class içinde fonksiyon varsa self kullnıp ilk elemanını rezerve ediyorsun
        print(f"{self.name} is walking")

#instance örnek. kalıbımız hazır ama ürün üretelim.

human1 = Human("enes") #alana kalıbı attım. aşağıdaki gi yapmak yerine
#human1.name="enes"
human1.talk("merhaba")
human1.walk()
print(human1)

human2 = Human() #alana kalıbı attım
human2.talk("selam")
human2.walk()
print(human2)

Human().talk("Merhaba")
