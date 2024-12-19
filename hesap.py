import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Hesap makinası - FAHRİ ")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_373=tk.Entry(root)
        GLineEdit_373["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_373["font"] = ft
        GLineEdit_373["fg"] = "#333333"
        GLineEdit_373["justify"] = "center"
        GLineEdit_373["text"] = "1.sayıyı gir"
        GLineEdit_373.place(x=70,y=70,width=70,height=25)

        GLineEdit_850=tk.Entry(root)
        GLineEdit_850["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_850["font"] = ft
        GLineEdit_850["fg"] = "#333333"
        GLineEdit_850["justify"] = "center"
        GLineEdit_850["text"] = "2.sayıyı gir"
        GLineEdit_850.place(x=150,y=70,width=70,height=25)

        GButton_648=tk.Button(root)
        GButton_648["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_648["font"] = ft
        GButton_648["fg"] = "#000000"
        GButton_648["justify"] = "center"
        GButton_648["text"] = "+"
        GButton_648.place(x=70,y=140,width=70,height=25)
        GButton_648["command"] = self.GButton_648_command

        GButton_2=tk.Button(root)
        GButton_2["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_2["font"] = ft
        GButton_2["fg"] = "#000000"
        GButton_2["justify"] = "center"
        GButton_2["text"] = "-"
        GButton_2.place(x=150,y=140,width=70,height=25)
        GButton_2["command"] = self.GButton_2_command

        GLabel_728=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_728["font"] = ft
        GLabel_728["fg"] = "#333333"
        GLabel_728["justify"] = "center"
        GLabel_728["text"] = "sonuc"
        GLabel_728.place(x=240,y=70,width=70,height=25)

        GLineEdit_477=tk.Entry(root)
        GLineEdit_477["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_477["font"] = ft
        GLineEdit_477["fg"] = "#333333"
        GLineEdit_477["justify"] = "center"
        GLineEdit_477["text"] = "sonuc"
        GLineEdit_477.place(x=310,y=70,width=70,height=25)

    def GButton_648_command(self):
        print("command")


    def GButton_2_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textBoxYazilanlar1 = tk.StringVar()
    textBoxYazilanlar2 = tk.StringVar()
    textBoxYazilanlar3 = tk.StringVar()

    root.mainloop()
