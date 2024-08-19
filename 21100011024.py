
# 21100011024/BATUHAN/AYDOGDU

def baslangic():
    global nerde
    global a
    with open("21100011024.txt", "r+") as file:
        veri = file.read()
    liste = veri.split(" ")
    don = len(liste)//6
    int(don)
    for j in range(don):
        for i in range(1):
            id = str(liste[a])
            ogrencidict[id] = {}
            ogrencidict[id]["id"] = str(liste[a])
            ogrencidict[id]["ad"] = liste[a + 1]
            ogrencidict[id]["soyad"] = liste[a + 2]
            ogrencidict[id]["bolum"] = liste[a + 3]
            ogrencidict[id]["izin"] = liste[a + 4]
            ogrencidict[id]["borc"] = liste[a + 5]
            a += 6
    with open("21100011024.txt", "a") as lan:
        nerde = lan.tell()

def ekle():
    global a
    print("-----------------------------------------------------------------------------------------------")
    idm = input("Eklenecek ogrencinin id'sini giriniz.Lutfen daha once kayitli olan id'leri girmeyiniz -->")
    ad = input("Eklenecek ogrencinin adini giriniz -->")
    soyad = input("Eklenecek ogrencinin soyadini giriniz -->")
    bolum = input("Eklenecek ogrencinin bolumunu buyuk harflerle giriniz. -->")
    izin = input("Eklenecek ogrencinin izin gunu sayisini giriniz -->")
    borc = input("Eklenecek ogrencinin borc miktarını giriniz -->")
    kagit = " " + idm + " " + ad + " " + soyad + " " + bolum + " " + izin + " " + borc
    uzun = len(kagit)
    orda = uzun + nerde
    with open("21100011024.txt", "a") as dos:
        dos.writelines(kagit)
        dos.seek(orda)
    with open("21100011024.txt", "r+") as s:
        yeniveri = s.read()
def sil():
    print("--------------------------------------------------------------------------------")
    silinecek = str(input("Silinecek ogrencinin id'sini giriniz"))
    global ogrencidict
    ogrencidict.pop(silinecek)
    silveri = ""
    bos = ""
    with open("21100011024.txt","w") as sil:
        for i in ogrencidict:
            silveri=ogrencidict[i]["id"] + " " + ogrencidict[i]["ad"] + " " + ogrencidict[i]["soyad"] + " " + ogrencidict[i]["bolum"] + " " + ogrencidict[i]["izin"] + " " + ogrencidict[i]["borc"]+" "
            silveri=bos+silveri
            sil.writelines(silveri)

def guncelle():
    print("--------------------------------------------------------------------------------")
    guncel=str(input("Guncellemek istediginiz ogrencinin ID'sini giriniz -->"))
    silveri = ""
    bos = ""
    id = input("Guncel ID degerini giriniz -->")
    ad = input("Guncel ogrenci adini giriniz -->")
    soyad = input("Guncel ogrenci soyadini giriniz -->")
    bolum = input("Guncel ogrenci bolumunu buyuk harflerle giriniz. -->")
    izin = input("Guncel ogrenci izin gunu sayisini giriniz -->")
    borc = input("Guncelogrencinin borc miktarını giriniz -->")
    global ogrencidict
    ogrencidict[guncel] = {"id":id,"ad":ad,"soyad":soyad,"bolum":bolum,"izin":izin,"borc":borc}
    with open("21100011024.txt","w") as sil:
        for i in ogrencidict:
            silveri = ogrencidict[i]["id"] + " " + ogrencidict[i]["ad"] + " " + ogrencidict[i]["soyad"] + " " + ogrencidict[i]["bolum"] + " " + ogrencidict[i]["izin"] + " " + ogrencidict[i]["borc"]+" "
            sil.writelines(silveri)

def ara():
    print("--------------------------------------------------------------------------------")
    aranacak = str(input("Aramak istediginiz ogrencinin ID degerini giriniz -->"))
    for i in ogrencidict:
        if i is aranacak:
            print("Ogrenci ID -->{}".format(ogrencidict[i]["id"]))
            print("Ogrenci AD -->{}".format(ogrencidict[i]["ad"]))
            print("Ogrenci SOYAD -->{}".format(ogrencidict[i]["soyad"]))
            print("Ogrenci BOLUM -->{}".format(ogrencidict[i]["bolum"]))
            print("Ogrenci KALAN IZIN -->{}".format(ogrencidict[i]["izin"]))
            print("Ogrenci BORC -->{}".format(ogrencidict[i]["borc"]))


def yurt_yonetim():
    def kapasite():
        global ogrencisayi
        for i in ogrencidict:
            ogrencisayi += 1
        toplamoda = 20
        odasayisi = ogrencisayi / 4
        bosoda = toplamoda - odasayisi
        kapas = int(input("YURDUN MAKSIMUM KAPASITESI ICIN 1'i\n"
                          "YURTTAKI DOLU ODA SAYISINI OGRENMEK ICIN 2'yi\n"
                          "YURTTAKI BOS ODA SAYISINI OGRENMEK ICIN 3'ü tuslayiniz --->"))
        if kapas == 1:
            print("YURDUN MAKSIMUM KAPASITESI --> {}".format(toplamoda*4))
        elif kapas == 2:
            print("YURTAKI DOLU ODA SAYISI --> {}".format(odasayisi))
        elif kapas == 3:
            print("YURTTAKI BOS ODA SAYISI --> {}".format(bosoda))

        else:
            print("YANLIS TUSLAMA YAPTINIZ.KAPASITE BOLUMUNE YONLENDIRILIYORSUNUZ !!!")
            kapasite()

    global borc
    global ogrencisayi
    for i in ogrencidict:
        borc = borc+int(ogrencidict[i]["borc"])

    bolumler = set()
    for i in ogrencidict:
        bolumler.add(ogrencidict[i]["bolum"])
    print("-----------------------------------------------------------------")
    print("Ogrencilerin toplam borc miktari -->{}".format(borc))
    print("-----------------------------------------------------------------")
    print("Yurttaki ogrencilerin kayitli oldugu bolumler --> {}".format(bolumler))
    print("-----------------------------------------------------------------")
    ogr = int(input("Yurdun kapasite verilerine ulasmak icin 1'i tuslayiniz -->\n"
                  "Menuye donmek icin 2'ye basiniz -->\n"))
    if ogr==1:
        kapasite()
    else:
        print("VERI SISTEMINDEN CIKILIYOR")

def izin():
    global ogrencidict
    izinveri = ""
    izinid = input("İZİN ALACAK OLAN OGRENCİNİN İD'SİNİ GİRİNİZ -->")
    alinacakgun = int(input("Kac gun izin almak istiyorsunuz? -->"))
    for i in ogrencidict:
        if i is izinid:
            kalandict = int(ogrencidict[izinid]["izin"])
            if kalandict >= alinacakgun:
                ogrencidict[izinid]["izin"]=str(kalandict-alinacakgun)
            else:
                izinsecim = input("Yeterli izin hakkiniz bulunmamaktadir.İzin alma bölümüne dönmek icin 1'i Ana menüye dönmek icin 2'yi tuslayiniz -->")
                if izinsecim == 1:
                    izin()
                elif izinsecim == 2:
                    exit()
    with open("21100011024.txt","w") as ac:
        for i in ogrencidict:
            izinveri = ogrencidict[i]["id"] + " " + ogrencidict[i]["ad"] + " " + ogrencidict[i]["soyad"] + " " + ogrencidict[i]["bolum"] + " " + ogrencidict[i]["izin"] + " " + ogrencidict[i]["borc"]+" "
            ac.writelines(izinveri)


ogrencidict = {}
a = 0
nerde = 0
borc = 0
ogrencisayi = 0

while True:
    print("--------------------------------------------------------------------------------")
    print("* ** *** **** ***** BatuYurT OTOMASYON SISTEMINE HOSGELDINIZ ***** **** *** ** *")
    anasecim = int(input("OGRENCI EKLEYEREK ISLEM YAPMAK ICIN 1'i -->\n"
                         "SISTEMDE BULUNAN OGRENCILER ILE ISLEM YAPMAK ICIN 2'yi TUSLAYINIZ -->"))

    if anasecim == 1:
        print("-------------------------------------------------")
        kac = int(input("Kac ogrenci eklemek istiyorsunuz? -->"))
        for i in range(kac):
            ekle()
        baslangic()
        while True:
            print("-------------------------------------------------")
            secim = int(input("SİL FONSKSİYONU ICIN 2\n"
                              "GUNCELLE FONKSIYONU ICIN 3\n"
                              "ARAMA FONKSIYONU ICIN 4u tuslayınız\n"
                              "OGRENCILERE AIT VERILERI GORMEK ICIN 5'i\n"
                              "IZIN ALMAK ICIN 6'YI TUSLAYINIZ\n"
                              "CIKIS YAPMAK ICIN 7'YI TUSLAYINIZ -->"))

            if secim == 2:
                sil()
            elif secim == 3:
                guncelle()
            elif secim == 4:
                ara()
            elif secim == 5:
                yurt_yonetim()
            elif secim == 6:
                izin()
            elif secim == 7:
                exit()

    elif anasecim == 2:
        baslangic()
        #print(ogrencidict)
        while True:
            print("-------------------------------------------------")
            secim = int(input("SİL FONSKSİYONU ICIN 2\n"
                              "GUNCELLE FONKSIYONU ICIN 3\n"
                              "ARAMA FONKSIYONU ICIN 4\n"
                              "OGRENCILERE AIT VERILERI GORMEK ICIN 5'i\n"
                              "IZIN ALMAK ICIN 6'YI\n"
                              "CIKIS YAPMAK ICIN 7'YI TUSLAYINIZ -->"))
            if secim == 2:
                sil()
            elif secim == 3:
                guncelle()
            elif secim == 4:
                ara()
            elif secim == 5:
                yurt_yonetim()
            elif secim == 6:
                izin()
            elif secim == 7:
                exit()

    else:
        print("--------------------------------------------------------------------------------")
        print("Yanlıs tuslama yaptiniz.Ana menuye yonlendiriliyorsunuz.")
        print("*****\n"
              " *** \n"
              "  *  \n"
              " *** \n"
              "*****  ")
        print("--------------------------------------------------------------------------------")








