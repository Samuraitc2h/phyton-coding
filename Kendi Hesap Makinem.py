sayi1=int(input("İlk Sayını Gir Gardaş: "))
sayi2=int(input("İkinci Sayını Gir Gardaş: "))  
secim=input("*,/,+,- Bunlardan Birini Seç Çabuk!")

if secim=="+":
 sonuc=sayi1+sayi2
 print(sonuc)
elif secim=="*":
 sonuc=sayi1*sayi2
 print(sonuc)
elif secim=="-":
  sonuc=sayi1-sayi2
  print(sonuc)
elif secim=="/":
 sonuc=sayi1/sayi2
 print(sonuc)