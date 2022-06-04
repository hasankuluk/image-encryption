from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


class SifreCoz:

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
            self.run_2()

    def run_2(self):

        img_1 = Image.open(self.filepath)
        px_1 = img_1.convert("RGB")

        en = 0
        boy = 0
        for i in range(11):
            rgb = px_1.getpixel((i, 0))
            if rgb[0] % 2 == 1:
                en += 2 ** i
            if rgb[1] % 2 == 1:
                boy += 2 ** i

        print(en, "------------", boy)

        width, height = img_1.size
        hedef_height = boy
        hedef_width = en
        hedef_size = hedef_height * hedef_width

        r = [0] * 8
        g = [0] * 8
        b = [0] * 8

        for x in range(hedef_size):
            k = x * 8
            r_hedef = 0
            g_hedef = 0
            b_hedef = 0

            for i in range(8):
                rgb = px_1.getpixel(((k + i) % width, (k + i) // width + 1))
                r[i] = rgb[0] % 2
                g[i] = rgb[1] % 2
                b[i] = rgb[2] % 2

            for u in range(8):
                r_hedef += r[u] * 2 ** (7 - u)
                g_hedef += g[u] * 2 ** (7 - u)
                b_hedef += b[u] * 2 ** (7 - u)

            img_1.putpixel((x % hedef_width, x // hedef_width), (r_hedef, g_hedef, b_hedef))

        # img_1.show()
        crop = img_1.crop((0, 0, hedef_width, hedef_height))
        filepath = filedialog.askdirectory()
        filepath += "/secret.png"

        crop.save(filepath, "PNG")
        img_1.close()

        # crop.show()
