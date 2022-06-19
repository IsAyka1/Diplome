from Libraries import *
from showPrediction import from_img

class MainWindow:
    def __init__(self, root, model):
        self.root = root
        self.root.geometry('1000x870')
        self.root.title("Загрузка изображения")
        self.root.iconbitmap('icon.ico')
        self.model = model
        self.panel = None
        self.button_next = None

    def draw_widgets(self):
        self.file_dir = StringVar()
        self.button_file = Button(self.root, text="Выбрать файл", background="#08f", foreground="#ccc",
                             padx="20", pady="8", font="16", command=partial(self.choose_file, self.file_dir))
        self.button_file.pack(side=TOP, padx=15, pady=30)
        self.text = StringVar()
        self.label = Label(self.root, textvariable=self.text, font=("Time New Roman", 14))
        self.label.pack(side=TOP, padx=15, pady=10)


    def delete_widgets(self):
        self.label.destroy()
        self.button_file.destroy()
        self.button_next.destroy()

    def choose_file(self, file_dir):
        self.filetypes = (("Изображение", "*.jpg *.gif *.png"),)
        filename = askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=self.filetypes, multiple=False)
        if filename:
            print(filename)
            file_dir.set(filename)
            img = Image.open(file_dir.get())
            x, y = img.size
            self.x, self.y = self.get_size(x, y)
            self.show_img(img, is_result=False)
            self.text.set("")
        else:
            tkinter.messagebox.showerror("Ошибка", "Невозможно открыть файл")

    def show_img(self, img, is_result):
        if self.panel:
            self.panel.destroy()
        self.canvas = Canvas(self.root)

        img = img.resize((self.x, self.y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel = Label(self.root, image=img)
        self.panel.image = img
        self.panel.pack(side=TOP, padx=15, pady=15)

        self.draw_button(is_result)

    def get_size(self, x, y):
        while x > 550 or y > 550:
            x = x // 2
            y = y // 2
        while x < 550 and y < 550:
            x += 50
            y += 50
        return x, y

    def draw_button(self, is_result):
        if self.button_next:
            self.button_next.destroy()
        if is_result:
            self.button_next = Button(self.root, text="Сохранить", background="#07f", foreground="#ccc",
                                      padx="35", pady="15", font="20", command=self.save_result)
            self.button_next.pack(side=BOTTOM, padx=15, pady=25)
        else:
            self.button_next = Button(self.root, text="Распознать", background="#07f", foreground="#ccc",
                                      padx="35", pady="15", font="20", command=partial(self.get_result, self.file_dir))
            self.button_next.pack(side=BOTTOM, padx=15, pady=25)


    def get_result(self, file_dir):
        prediction_text = []
        try:
            self.result, prediction_text = from_img(self.model, self.file_dir.get(), self.x, self.y)
            self.show_img(self.result, is_result=True)
        except:
            tkinter.messagebox.showerror("Ошибка в имени файла", "Невозможно выполнить распознавание, используйте латиницу в пути файла")
        if not len(prediction_text):
            self.text.set("Лица не найдены")
        else:
            self.text.set("Найденные эмоции: " + ", ".join(str(x) for x in prediction_text))

    def save_result(self):
        new_filename = asksaveasfilename(title="Сохранить файл", defaultextension=".jpg",
                                    filetypes=(self.filetypes))
        self.result.save(new_filename, "png")