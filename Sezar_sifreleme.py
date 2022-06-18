   # ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#sifre = input("şifrelenecek metni giriniz")
sifre = "rjwmfgf%rfmrzy"
metin = "" # metne dönüştürülmesi için değişken tanımlandı
for k in sifre:
#    print(ord(k)) # ASCII kodlarını verir decimal olarak
    print(k, "=>", chr(ord(k) - 4))
    metin = metin + chr(ord(k) - 4)
print(sifre, " = >", metin)
print(sifre, " = >", metin)
# ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#metin = input("şifrelenecek metni giriniz")
metin = "Python"
sifre = ""
for k in metin:
    print(ord(k)) # ASCII kodlarını verir decimal olarak
    print(k, "=>", chr(ord(k) + 4))
    sifre = sifre + chr(ord(k) + 4)
    print(sifre)
print(metin, " = >", sifre)
from sezar_sifreleme import sifreleme_fonk as sfr
metin = input("şifrelenecek metni giriniz")
sfr.sifrele(metin)
sifre = input("şifresi çözümlenecek metni giriniz")
sfr.sifrecoz(sifre)
def sifrele(metin):
    # ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#    metin = input("şifrelenecek metni giriniz")
    # metin = "Python"
    sifre = ""
    for k in metin:
        #    print(ord(k)) # ASCII kodlarını verir decimal olarak
        print(k, "=>", chr(ord(k) + 4))
        sifre = sifre + chr(ord(k) + 4)
    print(metin, " = >", sifre)
def sifrecoz(sifre): # şifresi çözülecek şifre fonksiyona parametre olarak geliyor
    # ord() => ASCII olarak değeri verme chr() içerisinde ki değere göre karakter üretiyor
#    sifre = input("şifrelenecek metni giriniz")
    # sifre = "Python"
    metin = "" # metne dönüştürülmesi için değişken tanımlandı
    for k in sifre:
        #    print(ord(k)) # ASCII kodlarını verir decimal olarak
        print(k, "=>", chr(ord(k) - 4))
        metin = metin + chr(ord(k) - 4)
    print(sifre, " = >", metin)
