#!/usr/bin/env python3
import PIL.Image, PIL.ImageDraw, PIL.ImageFont
from tkinter import *
import tkinter.filedialog, tkinter.messagebox

def mktga(fontname, fontsize, aa, ft):
    d=dict()
    if ft:
        f = open("characters.txt", encoding="U8")
        for line in f:
            line=line.strip()
            if line:
                fs=line.split("\t")
                d[fs[0]]=fs[1].split()[0]

    font = PIL.ImageFont.truetype(fontname, fontsize, 0)
    fontnum = 94
    fontw = 12 if fontsize <= 12 else 20
    image = PIL.Image.new("RGBA", (fontw * fontnum, fontw * fontnum))
    draw = PIL.ImageDraw.Draw(image)
    if aa == 0: draw.fontmode = "1"

    for i in range(fontnum):
        for j in range(fontnum):
            c = chr(j+0x21) if i == 9 else bytes((i+0xa1, j+0xa1)).decode("gb2312", "ignore")
            if c:
                draw.text((j*fontw, i*fontw), d.get(c, c), font=font, fill= (255,255,255))

    filename = "宋体 标准 12x12.tga" if fontsize <= 12 else "黑体 伪粗 20x20(16).tga"
    image.save(filename)
    return filename

apptitle="龙之崛起字体制作工具"
class Application(Frame):
    """图形界面"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):        
        self.fontsize = IntVar(self)
        self.aa = IntVar(self)
        self.ft = IntVar(self)
        
        OptionMenu(self, self.fontsize, *range(9,21)).pack(side=LEFT)
        Checkbutton(self, text = "平滑", variable=self.aa).pack(side=LEFT) 
        Checkbutton(self, text = "繁體", variable=self.ft).pack(side=LEFT)
        Button(self, text = "选择字体并转换", command = self.selectfont).pack(side=LEFT)
        
        self.fontsize.set(16) # 默认值
        self.aa.set(1)
        self.ft.set(0)
        
    def selectfont(self):
        f = tkinter.filedialog.askopenfile(parent=self, title="字体", 
                    defaultextension=".ttf", filetypes = [('字体文件', '.tt*')])
        if f:
            filename = mktga(f.name, self.fontsize.get(),self.aa.get(), self.ft.get())
            tkinter.messagebox.showinfo(parent=self, title=apptitle, message="“%s”已生成， \n请复制到游戏的LG_Data目录，覆盖同名文件！" % filename)

root = tkinter.Tk()
root.title(apptitle)
Application(master=root).mainloop()
