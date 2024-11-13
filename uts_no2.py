def is_leap_year(year):
    # Memeriksa apakah tahun tersebut adalah tahun kabisat
    if (year % 400 == 0):
        return True
    elif (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# Input dari pengguna
try:
    year = int(input("Masukkan tahun: "))
    if is_leap_year(year):
        print(f"{year} adalah tahun kabisat.")
    else:
        print(f"{year} bukan tahun kabisat.")
except ValueError:
    print("Silakan masukkan angka yang valid.")