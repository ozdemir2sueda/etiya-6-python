
def kredilerilistele(): #tanım yaptım birbiri ile ilişkili clas oluşturduğunda bunu çağırıyorsun
 krediler =["hizli kredi","maasini halkbanktan alanlara özel","mutlu emekli ihtiyaç kredisi"]
#veri kaynağından geliyor veri kaynağından sonra biz bu işlemleri yapıyoruz. ilişkilendirmeler

#alias
for kredi in krediler:
 print (kredi)
 kredilerilistele()
 