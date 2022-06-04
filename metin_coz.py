from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


class MetinCoz:

    def __init__(self):
        self.filepath = ""
        self.sifrelenecek_onay = 0
        self.buton = 0

    def open_file(self):
        messagebox.showinfo("sifreleme programı", "Açmak istediğiniz dosyayı seçiniz")

        if self.buton == 0:
            filepath = filedialog.askopenfilename(title="Resim Seçiniz",
                                                  filetypes=(("image files", "*.png"), ("all files", "*.*")))
            self.filepath = filepath
            return self.run()

    def run(self):
        img_1 = Image.open(self.filepath)
        px_1 = img_1.convert("RGB")
        width, height = img_1.size
        sayac = 0
        sayi = 0
        uz = ""
        metin = ""

        for i in range(4):
            for j in range(8):
                rgb = px_1.getpixel((sayac % width, sayac // width))
                r = rgb[0] % 2
                sayi += (2 ** j) * r
                sayac += 1
            uz = chr(sayi) + uz

            sayi = 0

        uz = uz[::-1]

        for i in range(int(uz)):
            for j in range(8):
                rgb = px_1.getpixel((sayac % width, sayac // width))
                r = rgb[0] % 2
                sayi += (2 ** j) * r
                sayac += 1

            metin = metin + chr(sayi)
            sayi = 0
        img_1.close()
        return metin
