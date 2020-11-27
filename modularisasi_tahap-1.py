"""
Program perhitungan luas segitiga
"""
print('Menghitung luas segitiga 1')
alas  = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 6
print(f'Menghitung luas segitiga dengan fungsi hasilnya = {hitung_luas_segitiga(alas, tinggi)}') #bisa kaya gini
print(f'Menghitung luas segitiga dengan fungsi hasilnya = {hitung_luas_segitiga(20,2)}') #atau kaya gini
