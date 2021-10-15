tahun = int(input('Masukkan tahun :'))
def apakah_kabisat(tahun):
habis_400 = tahun % 400 == 0
habis_100 = tahun % 100 == 0
habis_4 = tahun % 4 == 0

if habis_400 or habis_4 and not habis_100:
    print(f'{tahun} tahun kabisat')
else:
    print(f'{tahun} bukan tahun kabisat')
