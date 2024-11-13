def hitung_total_belanja():
    total_belanja = 0
    try:
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        
        for i in range(jumlah_barang):
            harga_barang = float(input(f"Masukkan harga barang ke-{i + 1}: "))
            total_belanja += harga_barang
            
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka yang benar.")
        return None

    return total_belanja

# Menjalankan program
total = hitung_total_belanja()
if total is not None:
    print(f"Total belanja Anda adalah: {total:.2f}")