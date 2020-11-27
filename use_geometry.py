# Cara pertama impor fungsi
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga
# kalo ga ditulis aliasnya, yang kepake nanti yang terakhir yaitu info persegi panjang
from geometri.persegi_panjang import hitung_luas_persegi_panjang, info as info_persegi_panjang
print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_luas_segitiga(10,6)}')

# Cara kedua
    # import geometri.segitiga # ini bisa disingkat
    # print(f'hitung_luas_segitiga {geometri.segitiga.hitung_luas_segitiga(10,6)}') # supaya ga panjang kaya gini
    # import geometri.segitiga as gs
    # print(f'hitung_luas_segitiga {gs.hitung_luas_segitiga(10,6)}') # bisa jadi pendek kaya gini

# Persegi panjang
print(info_persegi_panjang())
print(f'hitung_luas_segitiga {hitung_luas_persegi_panjang(10,6)}') # habis diimpor fungsinya muncul di atas, ya tinggal dipindah aja