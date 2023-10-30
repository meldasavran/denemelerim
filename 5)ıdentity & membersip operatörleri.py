""""identity" ve "membership" operatörleri, nesnelerin tanımlanmasını (identity) ve bir
 koleksiyonun içindeki bir elemanın varlığını kontrol etmeyi (membership) sağlayan operatörlerdir."""

"""Identity Operatörleri:
is: "is" operatörü, iki nesnenin aynı bellek konumunu işaret edip 
etmediğini kontrol eder. Yani, iki nesne aynı nesneyi mi temsil ediyor yoksa farklı nesneler mi? """

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
""""
Membership Operatörleri:in: "in" operatörü, bir elemanın bir koleksiyonun
 (liste, demet, dize, vb.) içinde olup olmadığını kontrol eder.
"""
my_list = [1, 2, 3, 4, 5]
x = 3

if x in my_list:
    print("x, my_list içinde")#true
else:
    print("x, my_list içinde değil")
