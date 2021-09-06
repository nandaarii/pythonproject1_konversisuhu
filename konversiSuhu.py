# Tampilkan menu
print()
print("--Program Konveksi Suhu--")
print("1. Celcius \t=> Fahrenheit")
print("2.  Celcius \t=> Kelvin")
print("3.  fahrenheit \t=> Celcius")
print("4.  kelvin \t=> Kelvin")
print("5.  Kelvin \t=> Celcius")
print("6.  Kelvin \t=> Fahrenheit")
print()

# Terima pilihan user
pilihan = input("silakan pilih menu diatas: ")

# Buat kondisi berdasarkan pilihan user
if pilihan == "1":
    formatAwal = " C"
    formatAkhir = " F"
    nilaiAwal = int(input("masukkan nilai celcius: "))
    nilaiAkhir = (nilaiAwal * 9/5) + 32
elif pilihan == "2":
    formatAwal = " C"
    formatAkhir = " K"
    nilaiAwal = int(input("masukkan nilai celcius: "))
    nilaiAkhir = nilaiAwal + 273.15
elif pilihan == "3":
    formatAwal = " F"
    formatAkhir = " C"
    nilaiAwal = int(input("masukkan nilai fahrenheit: "))
    nilaiAkhir = (nilaiAwal - 32) * 5/9
elif pilihan == "4":
    formatAwal = " F"
    formatAkhir = " K"
    nilaiAwal = int(input("masukkan nilai fahrenheit: "))
    nilaiAkhir = (nilaiAwal - 32) * 5/9
elif pilihan == "5":
    formatAwal = " K"
    formatAkhir = " C"
    nilaiAwal = int(input("masukkan nilai kelvin: "))
    nilaiAkhir = nilaiAwal - 273.15
elif pilihan == "6":
    formatAwal = " K"
    formatAkhir = " F"
    nilaiAwal = int(input("masukkan nilai kelvin: "))
    nilaiAkhir = (nilaiAwal - 273.15) * 9/5 +32

# Tampilkan hasil
print(str(nilaiAwal) + formatAwal +" = " + str(nilaiAkhir) + formatAkhir)





