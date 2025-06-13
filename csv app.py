import csv

Toplampuan = 0
Toplamyas = 0
sayi = 0
sayi2 = 0
with open("test.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for isim, yas, sehir, puan in reader:
        if puan:
            sayi += 1
            Toplampuan += int(puan)
        if yas:
            sayi2 +=1
            Toplamyas += int(yas)
Ortalamapuan = Toplampuan / sayi
Ortalamayas = Toplamyas / sayi2
print(f"Ortalama yas {Ortalamayas:.0f}")
print(f"Ortalama puan {Ortalamapuan:.2f}")
