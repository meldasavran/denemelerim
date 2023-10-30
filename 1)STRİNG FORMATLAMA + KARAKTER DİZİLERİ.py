
# STRİNG FORMATLAMA + KARAKTER DİZİLERİ
ad='melda' 
soyad="savran"
yas=11 
meslek="test"
print ("my name is {} mesleğim {}".format(ad,meslek))#değişkenleri ekrana formatlı şekilde yazdırır
print(f"my name is {ad} surname {soyad} ")#değişkenleri ekrana formatlı yazdırmanın kolay yolu
print ("my name is {1} {0}".format(ad,meslek)) #index belirterek değişkenlerin yerini değiştirme
print("my name is {m} mesleğim {a}".format(m=meslek,a=ad))#değişken tanımlayarak değişkenlerin yerini değiştirme

a=5 #döngü çalışması
b=4
if (a>b):
    print("{}sayısı büyüktür {} sayısından".format(a,b))
else:
    print("{}sayısı küçüktür {} sayısından".format(a,b))

#float sonucu formatlama
sonuc=200/700
print("{}".format(sonuc))#sonuc 0.28571428...
print("{f:1.3}".format(f=sonuc))# f adından değişken tanımlandı, 
#{f:1.3} kısmında 3 virgülden sonra kaç basamak olacağını belirtir 1 tam kısımda ne kadar boşluk


website="http://www.meldasavran.com"
course="Python kursu baştan sona python programlama"

# soru1:course içinde kaç karakter var
say=len(course)
print(say)

#soru2 website içinde www karakterlerini al
c=website[7:10] #indeks numaraları belirlerek veri çekildi
print(c)

#soru 3 website içinden com karakterlerini alın
d=website[23:26]
print(d)

#soru 4 website içinden ilk 15 karakter ve son 15 karakter
e=website[:15]
f=website[-15:]
print(e,f)

#soru 5 course ifadesindeki karakterleri tersten yazdır
degisken=course[::-1]
print (degisken)

# 5 karakter de 1 al 5 kere yazdır
s="12345"*5
print(s[::5])

# soru 6 hello world ifadesindeki w W ile değiştir
s="hello world"
s=s.replace("w","W")
print(s)