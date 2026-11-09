branslar = ("Yazılım" , "Tasarım" , "Pazarlama")
tum_ogrenciler =[]
tum_ogrenciler.append(["Aynur".strip(), ["Yazılım"]])
tum_ogrenciler.append(["Irmak".strip(), ["Tasarım"]])
tum_ogrenciler.append(["Ayşe".strip(), ["Pazarlama"]])
tum_ogrenciler.insert(0,["Çağla Başkan".strip(), ["Yazılım", "Tasarım", "Pazarlama"]])

print(f"Toplam kayıtlı öğrenci sayısı:{len(tum_ogrenciler)}")
for ogrenci in tum_ogrenciler:
  if (ogrenci[0])== "Ayşe":
    tum_ogrenciler.remove(ogrenci)
    break 

cikan_ogrenci = tum_ogrenciler.pop()
print(f"Sistemden en son çıkan öğrenci:{cikan_ogrenci[0]}")

tum_ogrenciler.append(["Deniz kök".strip(), ["Yazılım"]])

sirali_kopya = sorted(tum_ogrenciler)
print("Sıralanmış Kopya:", sirali_kopya)
print("Orijinal Liste (Değişmedi):", tum_ogrenciler)

tum_ogrenciler.sort()
print("Kalıcı olarak sıralanmış ana liste:", tum_ogrenciler)
