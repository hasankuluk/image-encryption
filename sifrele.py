from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


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


class Sifre:

    def __init__(self):
        self.path1 = ""
        self.path2 = ""
        self.path3 = ""
        self.count = 0
        self.sifrelenecek_onay = 0
        self.red = 0
        self.buton = 0

    def open_file(self):

        filepath = ""
        if self.buton < 2:
            messagebox.showinfo("sifreleme programı", "Açmak istediğiniz dosyayı seçiniz")
            filepath = filedialog.askopenfilename(title="Resim Seçiniz",
                                                  filetypes=(("image files", "*.png"), ("all files", "*.*")))

        if self.buton == 0:
            self.path1 = filepath
        elif self.buton == 1:
            self.path2 = filepath
        elif self.buton == 2:
            messagebox.showinfo("sifreleme programı", "Kaydetmek istediğiniz yeri seçiniz")
            self.path3 = filedialog.askdirectory()
            self.run()

    def erken_cikis(self):
        return self.red

    def run(self):

        img_1 = Image.open(self.path1)  # Ana image
        img_2 = Image.open(self.path2)  # sifrelenecek image

        px_1 = img_1.convert("RGB")
        px_2 = img_2.convert("RGB")

        width_1, height_1 = img_1.size
        width_2, height_2 = img_2.size

        if img_1.size < img_2.size * 8 or width_1 < 30:
            messagebox.showinfo("sifreleme programı", "Sİfrelenecek boyut ana resmin en fazla 1/8 boyutunda olabilir.")
            self.red = 1
            print("erken çıkış ", self.red)
            return

        # t_1 = height_1 * width_1
        img2_pixel_sayisi = height_2 * width_2

        for x in range(img2_pixel_sayisi):
            rgb = px_2.getpixel((x % width_2, x // width_2))  # rgb degerlerini al
            r_2 = rgb[0]
            g_2 = rgb[1]
            b_2 = rgb[2]

            k = x * 8

            r_bit = [0] * 8
            g_bit = [0] * 8
            b_bit = [0] * 8

            for i in range(8):
                r_bit[7 - i] = (r_2 >> i) & 1  # rgb degerleri ikilik tabana cevrilir 24 -> 00001100
                g_bit[7 - i] = (g_2 >> i) & 1
                b_bit[7 - i] = (b_2 >> i) & 1
            for z in range(8):  # sifrelenecek resimdeki her bir piksel için 8 kez döner
                rgb = px_1.getpixel(((k + z) % width_1, (k + z) // width_1 + 1))

                r_1 = duzeltme(r_bit[z], rgb[0])  # ana resme ikilik tabandaki degere göre yerleştir
                g_1 = duzeltme(g_bit[z], rgb[1])
                b_1 = duzeltme(b_bit[z], rgb[2])

                img_1.putpixel(((k + z) % width_1, (k + z) // width_1 + 1), (r_1, g_1, b_1))

        # boyut bilgileri eklenir
        w = width_2
        h = height_2

        for i in range(10, -1, -1):
            a = (w >> i) & 1
            b = (h >> i) & 1

            rgb = px_1.getpixel((i, 0))

            r_1 = duzeltme(a, rgb[0])  # ana resme ikilik tabandaki degere göre yerleştir
            g_1 = duzeltme(b, rgb[1])
            b_1 = rgb[2]
            img_1.putpixel((i, 0), (r_1, g_1, b_1))

        img_1.save(self.path3 + "/sifreli_resim.png")
        img_1.close()
        img_2.close()