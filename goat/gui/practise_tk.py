from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text="泥嚎！有机会粗来玩嘛！！！")
        self.helloLabel.pack()

        # 添加Entry小部件供用户输入名字
        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.alertButton = Button(self, text="如果接受我的邀请，pick me!!!", command=self.hello)
        self.alertButton.pack()

    def hello(self):
        context = self.nameInput.get() or 'my pleasure~~'
        messagebox.showinfo("Message", "Hello " + context)


if __name__ == '__main__':
    app = Application()
    # 设置窗口标题
    app.master.title('一吱小fei鹅.gaga')
    # 主消息循环
    app.mainloop()
