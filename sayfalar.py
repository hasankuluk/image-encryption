from tkinter import *
from tkinter import messagebox
from metin_coz import MetinCoz
from metin_sifrele import MetinSifrele
from sifre_coz import SifreCoz
from sifrele import Sifre
import tkinter.font as font


class Sayfa:
    def __init__(self):
        self.girdi = None
        self.ana_cerceve = Tk()
        self.ana_cerceve.geometry("500x250")
        self.ana_cerceve.title('Şifreleme programı')
        self.pencere = Frame(self.ana_cerceve).pack()
        self.sfr = Sifre()
        self.coz = SifreCoz()
        self.myFont = font.Font(family='Helvetica', size=20, weight='bold')
        self.metin_sifrele = MetinSifrele()
        self.onay1 = 0
        self.ana_onay = 0
        self.hedef_onay = 0
        self.metin_cozucu = MetinCoz()



    def clear_pencere(self):
        for widgets in self.ana_cerceve.winfo_children():
            widgets.destroy()

    def ana_sayfa(self):
        Label(self.pencere, font="myFont", text="Yapmak istediğiniz işlemi seçiniz").place(x=100, y=40)
        button1 = Button(self.pencere, font="myFont", text="ŞİFRELE",
                         command=self.sayfa_sifrele)  # command=self.sfr.open_file
        button1.place(x=75, y=100)
        button2 = Button(self.pencere, font="myFont", text="ŞİFRE ÇÖZ", command=self.sayfa_coz)
        button2.place(x=300, y=100)


    def metin_sayfa(self):
        self.clear_pencere()
        Label(self.pencere, font="myFont", text="Şifrelenecek metni giriniz").place(x=30, y=15)
        self.girdi = Entry(self.pencere, width=30, font=('Arial 14'))
        self.girdi.place(x=30, y=55)
        button1 = Button(self.pencere, font="myFont", text="RESİM SEÇİNİZ", command=self.metin_sifrele_resim)
        button1.place(x=30, y=105)
        button = Button(self.pencere, font="myFont", text="KAYDET", command=self.metin_sifrele_kayit)
        button.place(x=215, y=160)

    def sayfa_sifrele(self):
        self.clear_pencere()
        Label(self.pencere, font="myFont", text="Hangi tür şifreleme yapılacağını seçiniz").place(x=75, y=40)
        button1 = Button(self.pencere, font="myFont", text="METİN ŞİFRELE", command=self.metin_sayfa)
        button1.place(x=50, y=100)
        button2 = Button(self.pencere, font="myFont", text="RESİM ŞİFRELE", command=self.sayfa_sifrele_resim)
        button2.place(x=275, y=100)

    def sayfa_coz(self):
        self.clear_pencere()
        Label(self.pencere, font="myFont", text="Hangi tür şifre çözme yapılacağını seçiniz").place(x=65, y=40)
        button1 = Button(self.pencere, font="myFont", text="METİN ÇÖZ",
                         command=self.coz_metin_buton)  # command=self.sfr.open_file
        button1.place(x=70, y=100)
        button2 = Button(self.pencere, font="myFont", text="RESİM ÇÖZ", command=self.coz_buton)
        button2.place(x=275, y=100)

    def sayfa_sifrele_resim(self):
        self.clear_pencere()
        Label(self.pencere, font="myFont", text="Şifrelenecek resim ana resmin sekizde biri boyutta\n olacak şekilde "
                                                "dosyalarınızı seçiniz.").place(x=20, y=10)
        button1 = Button(self.pencere, font="myFont", text="ANA RESMİ SEÇİNİZ", command=self.ana_buton)
        button1.place(x=144, y=80)
        button2 = Button(self.pencere, font="myFont", text="ŞİFRELENECEK RESMİ SEÇİNİZ", command=self.sifre_buton)
        button2.place(x=90, y=130)
        button3 = Button(self.pencere, font="myFont", text="KAYDET", command=self.kaydet_buton)
        button3.place(x=200, y=185)

    def ana_buton(self):
        self.ana_onay = 1
        self.sfr.buton = 0
        self.sfr.open_file()

    def sifre_buton(self):
        self.hedef_onay = 1
        self.sfr.buton = 1
        self.sfr.open_file()

    def kapat(self):
        self.ana_cerceve.destroy()

    def basarisiz_sayfa(self):
        self.clear_pencere()
        Label(self.pencere, font="myFont", text="İşleminiz başarısız olmuştur").place(x=110, y=70)
        button = Button(self.pencere, font="myFont", text="TAMAM", command=self.kapat)
        button.place(x=215, y=180)

    def son_sayfa(self):
        self.clear_pencere()
        Label(self.pencere, font="myFont", text="İşleminiz başarıyla gerçekleşti").place(x=110, y=70)
        button = Button(self.pencere, font="myFont", text="TAMAM", command=self.kapat)
        button.place(x=215, y=180)

    def kaydet_buton(self):

        if self.ana_onay == 1 and self.hedef_onay == 1:
            self.sfr.buton = 2
            self.sfr.open_file()
            if self.sfr.red == 1:
                self.basarisiz_sayfa()
            else:
                self.son_sayfa()
        else:
            messagebox.showinfo("sifreleme programı", "Önce dosyaları seçiniz")

    def coz_buton(self):
        self.coz.open_file()
        self.son_sayfa()

    def metin_sifrele_resim(self):
        self.metin_sifrele.open_file()
        self.onay1 = 1

    def metin_sifrele_kayit(self):
        text = self.girdi.get()
        self.metin_sifrele.text = text
        if self.onay1 == 1:
            self.metin_sifrele.kayit()
            self.metin_sifrele.run()
            self.son_sayfa()
        else:
            messagebox.showinfo("sifreleme programı", "Önce dosyayı seçiniz")

    def metin_desifre(self, secret_metin):
        self.clear_pencere()
        Label(self.pencere, font="myFont", text="Gizli mesaj:").place(x=20, y=20)
        output = Text(self.pencere, height=7, width=45, bg="light cyan")
        output.insert(END, secret_metin)
        output.place(x=20, y=55)

        button = Button(self.pencere, font="myFont", text="TAMAM", command=self.kapat)
        button.place(x=215, y=180)

    def coz_metin_buton(self):
        cozulmus_metin = self.metin_cozucu.open_file()
        self.metin_desifre(cozulmus_metin)

