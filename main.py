#登录页面
import tkinter
from test2 import Mainpage

class LoginPage:
    def __init__(self,root2):
        #初始化
        #root 相当于本子
        # 定义窗口对象
        self.root = root2


        #登录页 一页纸
        self.login_frame=tkinter.Frame(self.root)
        self.login_frame.grid()

        #设置标题
        self.root.title('学生信息管理系统 V1')
        #设置窗体大小
        self.root.geometry('400x200')


        self.username=tkinter.StringVar()
        self.password=tkinter.StringVar()
        self.create_page()
        self.root.mainloop()

    def create_page(self):
        #设置空白格，将布局更美观
        tkinter.Label(self.login_frame,width=25,height=3).grid(row=0,column=0)
        tkinter.Label(self.login_frame,text='账号:',bg='lightblue').grid(row=1,column=0)
        tkinter.Entry(self.login_frame,textvariable=self.username,bg='lightblue').grid(row=1,column=1)

        tkinter.Label(self.login_frame,text='密码:',bg='lightblue').grid(row=2,column=0)
        tkinter.Entry(self.login_frame,textvariable=self.password,show='*',bg='lightblue').grid(row=2,column=1)

        tkinter.Label(self.login_frame).grid(row=3,column=0)

        tkinter.Button(self.login_frame, text='登录', command=self.check_login,bg='lightblue').grid(row=4, column=0)
        tkinter.Button(self.login_frame, text='退出', command=self.root.quit,bg='lightblue').grid(row=4, column=2)

    #登录检测参数
    def check_login(self):
        print('检查登录')
        print('账号名：',self.username.get())
        print('密码：',self.password.get())
        #数据是否存在
        if self.username.get()=='qyh' and self.password.get()=='123':
            print('登录成功')
            #换页
            self.login_frame.destroy()
            #登录成功 切换页面
            Mainpage(self.root)
        else:
            print('登录失败')

root=tkinter.Tk()

LoginPage(root)

root.mainloop()