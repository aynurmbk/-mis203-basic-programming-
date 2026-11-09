#Hafta 03

Kullanılan Yapay Zeka Aracı: ChatGPT/ Gemini

Kullanılan komut: "Ödevin ekran görüntülerini sağladım ve mantığı açıklamalarla birlikte Python koduna dönüştürmenizi istedim."

Ne değiştirdiniz?: Dize cinsinden yaş girişlerinde çökmeyi önlemek için tamsayı girişleri için try-except ile giriş doğrulama işlemi eklendi.

Testler:

1.Girdi: Kutu, Yaş: 5, Hafta Sonu -> Sonuç: Kutu: 0.00 DENEME (Ücretsiz)
2.Girdi: Aynur, Yaş: 20, Hafta içi, Öğrenci: evet -> Sonuç: Aynur: 140.00 TL (Öğrenci)
3.Girdi: Irmak, Yaş: 65, Hafta içi -> Sonuç: Irmak: 100.00 TRY (Senior)
Kuralların sırası neden önemlidir?: Sıra önemlidir çünkü if-elif ifadeleri yukarıdan aşağıya doğru çalışır ve ilk eşleşen koşulda durur.
Eğer öğrenci indirimleri gibi daha geniş koşullar yaş sınırlarından (örneğin, 6 yaş altı) önce kontrol edilirse, 5 yaşındaki bir öğrenci yanlışlıkla ücretsiz olmak yerine %30 indirim alabilir.
