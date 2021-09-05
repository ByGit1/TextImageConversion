if __name__ == "__main__":
    def Middle(x=600, y=300):
        try:
            import win32api
            import win32con
        except FileNotFoundError:
            return '%dx%d' % (x, y)
        import tkinter.messagebox
        if (win32api.GetSystemMetrics(win32con.SM_CXSCREEN) < x) or (
                win32api.GetSystemMetrics(win32con.SM_CYSCREEN) < y + 50):
            tkinter.messagebox.showinfo(Title, '屏幕分辨率过小，\n请调大屏幕分辨率！')
            raise Exception
        else:
            XA = int((win32api.GetSystemMetrics(win32con.SM_CXSCREEN) - x) / 2) - 7
            YA = int((win32api.GetSystemMetrics(win32con.SM_CYSCREEN) - y) / 2) - 30
            return '%dx%d+%d+%d' % (x, y, XA, YA)


    def RootA_Bmp():
        global choiceA
        choiceA = 1
        RootA_Des()


    def RootA_Txt():
        global choiceA
        choiceA = 2
        RootA_Des()


    def RootB_A(event=0):
        try:
            with open(FileT.get(), encoding='utf8') as f:
                all_text = f.read()
                str_len = len(all_text)
                width = math.ceil(str_len ** 0.5)
                im = PIL.Image.new("RGB", (width, width), 0x0)

                x, y = 0, 0
                for i in all_text:
                    index = ord(i)
                    rgb = (0, (index & 0xFF00) >> 8, index & 0xFF)
                    im.putpixel((x, y), rgb)
                    if x == width - 1:
                        x = 0
                        y += 1
                    else:
                        x += 1
                im.save(FileT.get().split('.')[0] + ".bmp")
        except UnicodeDecodeError:
            messagebox.showerror(Title, '编码错误!\n请转成UTF-8编码!')
        except FileNotFoundError:
            messagebox.showerror(Title, '找不到文件!\n请确定在程序目录下!')
        else:
            messagebox.showinfo(Title, '转换成功!\n文件名为：' + (FileT.get().split('.')[0] + ".bmp"))
        rootB.destroy()


    def RootC_A(event=0):
        try:
            im, lst = PIL.Image.open(FileRT.get(), 'r'), []
            width, height = im.size
            for y in range(height):
                for x in range(width):
                    red, green, blue = im.getpixel((x, y))
                    if (blue | green | red) == 0:
                        break
                    index = (green << 8) + blue
                    lst.append(chr(index))
            all_text = ''.join(lst)
            with open(FileWT.get(), 'w', encoding="utf8") as f:
                f.write(all_text)
        except PIL.UnidentifiedImageError:
            messagebox.showerror(Title, '编码错误!\n请转成UTF-8编码!')
        except (FileNotFoundError, AttributeError):
            messagebox.showerror(Title, '找不到文件!\n请确定在程序目录下!')
        else:
            messagebox.showinfo(Title, '转换成功!\n内容文件名为：' + FileWT.get())
        rootC.destroy()


    import PIL.Image
    from tkinter import *
    import math
    from tkinter import messagebox
    while 1:
        rootA, Title, choiceA, RootA_Des = Tk(), '', 0, lambda: rootA.destroy()
        rootA.title(Title)
        rootA.geometry(Middle())
        Label(rootA, text='请选择模式：', font='楷体 30').pack(pady=20)
        Button(rootA, text='变图片', width=40, font='楷体 18', command=RootA_Bmp, height=2).pack()
        Button(rootA, text='变文件', width=40, font='楷体 18', command=RootA_Txt, height=2).pack(pady=5)
        Button(rootA, text='退出', width=40, font='楷体 18', command=RootA_Des, height=2).pack()
        rootA.mainloop()
        if choiceA:
            if choiceA == 1:
                rootB, Title = Tk(), '文字转图片'
                rootB.title(Title)
                rootB.geometry(Middle())
                rootB_frameA, FileT = Frame(rootB), StringVar()
                Label(rootB_frameA, text='设置', font='楷体 25').pack(pady=40)
                Label(rootB_frameA, text='转化文件的文件名： ', font='楷体 20').pack(side=LEFT)
                Entry(rootB_frameA, font='楷体 18', textvariable=FileT).pack(side=LEFT)
                Button(rootB, text='确定', command=RootB_A, font='楷体 18', width=30).pack(side=BOTTOM)
                rootB_frameA.pack()
                rootB.bind('<Return>', RootB_A)
                rootB.mainloop()
            else:
                rootC, Title = Tk(), '图片转文字'
                rootC.title(Title)
                rootC.geometry(Middle())
                rootC_frameA, FileRT, rootC_frameB, FileWT = Frame(rootC), StringVar(), Frame(rootC), StringVar()
                Label(rootC_frameA, text='设置', font='楷体 25').pack(pady=40)
                Label(rootC_frameA, text='图片文件名： ', font='楷体 20').pack(side=LEFT)
                Entry(rootC_frameA, font='楷体 18', textvariable=FileRT).pack(side=LEFT)
                Label(rootC_frameB, text='内容文件名： ', font='楷体 20').pack(side=LEFT)
                Entry(rootC_frameB, font='楷体 18', textvariable=FileWT).pack(side=LEFT)
                Button(rootC, text='确定', command=RootC_A, font='楷体 18', width=30).pack(side=BOTTOM)
                rootC_frameA.pack()
                rootC_frameB.pack()
                rootC.bind('<Return>', RootC_A)
                rootC.mainloop()
        else:
            sys.exit()
