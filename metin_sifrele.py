from tkinter import filedialog
from PIL import Image
from tkinter import messagebox


def ikilik(n):
    liste = []
    for i in range(8):
        x = (n >> i) & 1
        liste.append(x)
    return liste


def duzeltme(my_bit, y):
    if y == 255:
        y = 254

    if my_bit % 2 == 1:
        if y % 2 == 0:
            return y + 1
        else:
            return y
    else:
        if y % 2 == 0:
            return y
        else:
            return y + 1


class MetinSifrele:
    def __init__(self):
        self.path = ""
        self.resim_onay = 0
        self.text = ""
        self.kayit_yeri = ""

    def kayit(self):
        messagebox.showinfo("sifreleme programı", "Kaydetmek istediğiniz yeri seçiniz")
        self.kayit_yeri = filedialog.askdirectory()

    def open_file(self):
        self.path = filedialog.askopenfilename(title="Resim Seçiniz",
                                               filetypes=(("image files", "*.png"), ("all files", "*.*")))

    def donustur(self, harf):
        kucuk = harf.islower()
        if not harf.isalpha():
            return harf
        harf = harf.lower()

        if kucuk:
            if harf == "ş":
                return "s"
            elif harf == "ö":
                return "o"
            elif harf == "ı":
                return "i"
            elif harf == "ç":
                return "c"
            elif harf == "ğ":
                return "g"
            elif harf == "ü":
                return "u"
        else:
            if harf == "ş":
                return "S"
            elif harf == "ö":
                return "O"
            elif harf == "i":
                return "I"
            elif harf == "ç":
                return "C"
            elif harf == "ğ":
                return "G"
            elif harf == "ü":
                return "U"
        return harf

    def run(self):
        img_1 = Image.open(self.path)
        px_1 = img_1.convert("RGB")
        width_1, height_1 = img_1.size
        count = 0
        u = self.text
        uzunluk = len(u)
        temp = ""
        for t in range(4):

            if t < len(str(uzunluk)):
                temp += str(uzunluk)[t]
            else:
                temp = "0" + temp

        u = temp + u
        print(u)
        for i in u:
            ch_n = ord(self.donustur(i))

            for j in range(8):
                binary_liste = ikilik(ch_n)
                rgb = px_1.getpixel((count % width_1, count // width_1))
                r = rgb[0]
                r = duzeltme(binary_liste[j], r)
                print(r)
                img_1.putpixel((count % width_1, count // width_1), (r, rgb[1], rgb[2]))
                count += 1
        img_1.save(self.kayit_yeri + "/sifreli_metin.png")
        img_1.close()