#soru1 girilen sayının 0-100 arasında olup olmadığını kontrol edin

"""degisken= int(input("sayı giriniz"))
if degisken>0 and degisken<=100:
    print("sayı 0 ile 100 arasındadır")
else:
    print("sayı 0 ile 100 arasında değildir")"""


 #soru2 girilen sayının pozitif çift sayı olup olmama durumunu kontrol edin

"""sayi1=int(input("sayı giriniz"))

if sayi1>0 and sayi1%2==0:
 print("girilen sayı pozitiftir ve çift sayıdır")
else:
 print ("girilen sayı pozitif veya çift değildir")"""


#soru3 girilen 3 sayıyı karşılaştırınız


sayi1=int(input("1.sayıyı giriniz"))
sayi2=int(input("2.sayıyı giriniz"))
sayi3=int(input("3.sayıyı giriniz"))

if sayi1>sayi2 and sayi1>sayi3:
    print(f"girilen sayılardan {sayi1} büyüktür ")
elif sayi2>sayi1 and sayi2>sayi3:
    print(f"girilen sayılardan {sayi2} büyüktür")
else:
    print(f"girilen sayılardan {sayi3} büyüktür")