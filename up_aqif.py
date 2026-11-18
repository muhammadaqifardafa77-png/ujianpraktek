print("PROGRAM KASIR KANTIN KAMPUS")

total_belanja = 0

while True:
    nama_makanan = input("\nMasukkan nama makanan: ")
    harga = int(input("Masukkan harga makanan (Rp): "))
    jumlah = int(input("Masukkan jumlah pembelian: "))

    subtotal = harga * jumlah
    total_belanja += subtotal
    print(f"Subtotal {nama_makanan}: Rp{subtotal:,.0f}")

    lanjut = input("Apakah ingin menambah makanan lain? (y/t): ").lower()
    if lanjut != 'y':
        break

if total_belanja > 100000:
    diskon = total_belanja * 0.10
else:
    diskon = 0.10

total_pembayaran = total_belanja - diskon

print("\n=== RINCIAN PEMBAYARAN ===")
print(f"Total Belanja    : Rp{total_belanja:,.0f}")
print(f"Diskon (10%)     : Rp{diskon:,.0f}")
print(f"Total Pembayaran : Rp{total_pembayaran:,.0f}")