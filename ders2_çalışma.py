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