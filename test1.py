#解释test2
import tkinter

#定义窗口对象
root = tkinter.Tk()

#登录页
login_frame=tkinter.Frame(root)
login_frame.grid()

#设置标题
root.title('学生信息管理系统 V1')
#设置窗体大小
root.geometry('400x200')

username=tkinter.StringVar()
password=tkinter.StringVar()

#设置空白格，将布局更美观
tkinter.Label(login_frame,width=25,height=3).grid(row=0,column=0)

tkinter.Label(login_frame,text='账号:').grid(row=1,column=0)
tkinter.Entry(login_frame,textvariable=username).grid(row=1,column=1)

tkinter.Label(login_frame,text='密码:').grid(row=2,column=0)
tkinter.Entry(login_frame,textvariable=password,show='*').grid(row=2,column=1)

tkinter.Label(login_frame).grid(row=3,column=0)

#登录检测参数
def check_login():
    print('检查登录')
    print('账号名：',username.get())
    print('密码：',password.get())
    #数据是否存在
    if username.get()=='qyh' and password.get()=='123':
        print('登录成功')
        #换页
        login_frame.destroy()
    else:
        print('登录失败')

tkinter.Button(login_frame,text='登录',command=check_login).grid(row=4,column=0)
tkinter.Button(login_frame,text='退出',command=quit).grid(row=4,column=2)

#换页

#显示窗口对象
root.mainloop()