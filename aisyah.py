print("============== MENU ==============")
print("1. Konversi Suhu")
print("2. Bangun Ruang")
pilih = input("Silahkan pilih menu dibawah 1/2 : ")
if(pilih == "1"):
    celcius = int(input("Silahkan masukkan suhu Celcius : "))
    fahrenheit = (5/9)*celcius +32
    kelvin = celcius+273
    print("Hasil Konversi Suhu :")
    print("Fahrenheit : ", fahrenheit, "F")
    print("kelvin : ", kelvin, "k")
elif(pilih == "2"):
    sisi = int(input("Silahkan masukkan panjang sisi : "))
    luasKubus = sisi*sisi*sisi
    print("Luas Kubus = ", luasKubus)
else:
    print("Menu yang dipilih tidak tersedia")