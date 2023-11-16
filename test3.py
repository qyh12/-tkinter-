#增删改查页面
# import tkinter
import tkinter
from tkinter import ttk
import tkinter as tk
from IPython.terminal.pt_inputhooks import tk

from db import db


class InsertFrame(tkinter.Frame):
    #继承
    def __init__(self,root):
        super().__init__(master=root)
        self.studentid = tkinter.StringVar()
        self.name = tkinter.StringVar()
        self.math = tkinter.StringVar()
        self.chinese = tkinter.StringVar()
        self.english = tkinter.StringVar()
        self.physics = tkinter.StringVar()
        self.chemistry = tkinter.StringVar()
        self.biology = tkinter.StringVar()
        self.status = tkinter.StringVar()

        self.create_page()

    def create_page(self):
        #设置空白格，将布局更美观
        tkinter.Label(self,width=10,height=1).grid(row=0,column=0,padx=6,pady=6)
        tkinter.Label(self,text='学号:',bg='lightblue').grid(row=1,column=0,padx=6,pady=6)
        tkinter.Entry(self,textvariable=self.studentid,bg='lightblue').grid(row=1,column=1,padx=6,pady=6)
        tkinter.Label(self,text='姓名:',bg='lightblue').grid(row=2,column=0,padx=6,pady=6)
        tkinter.Entry(self,textvariable=self.name,bg='lightblue').grid(row=2,column=1,padx=6,pady=6)
        tkinter.Label(self, text='数学:',bg='lightblue').grid(row=3, column=0,padx=6,pady=6)
        tkinter.Entry(self, textvariable=self.math,bg='lightblue').grid(row=3, column=1,padx=6,pady=6)
        tkinter.Label(self, text='语文:',bg='lightblue').grid(row=4, column=0,padx=6,pady=6)
        tkinter.Entry(self, textvariable=self.chinese,bg='lightblue').grid(row=4, column=1,padx=6,pady=6)
        tkinter.Label(self, text='英语:',bg='lightblue').grid(row=5, column=0,padx=6,pady=6)
        tkinter.Entry(self, textvariable=self.english,bg='lightblue').grid(row=5, column=1,padx=6,pady=6)
        tkinter.Label(self, text='物理:',bg='lightblue').grid(row=6, column=0,padx=6,pady=6)
        tkinter.Entry(self, textvariable=self.physics,bg='lightblue').grid(row=6, column=1,padx=6,pady=6)
        tkinter.Label(self, text='化学:',bg='lightblue').grid(row=7, column=0,padx=6,pady=6)
        tkinter.Entry(self, textvariable=self.chemistry,bg='lightblue').grid(row=7, column=1,padx=6,pady=6)
        tkinter.Label(self, text='生物:',bg='lightblue').grid(row=8, column=0,padx=6,pady=6)
        tkinter.Entry(self, textvariable=self.biology,bg='lightblue').grid(row=8, column=1,padx=6,pady=6)

        tkinter.Button(self, text='录入', command=self.recode,bg='lightblue').grid(row=9, column=1)
        tkinter.Label(self, textvariable=self.status).grid(row=10, column=1)

    def recode(self):
        print('触发记录数据事件')

        stu={
            "studentid": self.studentid.get(),
             "name": self.name.get(),
             "math": self.math.get(),
             "chinese": self.chinese.get(),
             "english": self.english.get(),
             "physics": self.physics.get(),
             "chemistry": self.chemistry.get(),
             "biology": self.biology.get()
        }
        db.insert(stu)
        self.status.set('数据插入成功')
        print(db.all())

class SearchFrame(tkinter.Frame):
    #继承
    def __init__(self,root):
        super().__init__(master=root)
        tkinter.Label(self, text='查询页面内容').pack()
        tkinter.Label(self, text='查询页面内容').pack()
        tkinter.Label(self, text='查询页面内容').pack()
        tkinter.Label(self, text='查询页面内容').pack()

class ModifyFrame(tkinter.Frame):
    #继承
    def __init__(self,root):
        super().__init__(master=root)
        tkinter.Label(self, text='修改页面内容').pack()
        tkinter.Label(self, text='修改页面内容').pack()
        tkinter.Label(self, text='修改页面内容').pack()
        tkinter.Label(self, text='修改页面内容').pack()

class DeleteFrame(tkinter.Frame):
    #继承
    def __init__(self,root):
        super().__init__(master=root)
        tkinter.Label(self, text='删除页面内容').pack()
        tkinter.Label(self, text='删除页面内容').pack()
        tkinter.Label(self, text='删除页面内容').pack()
        tkinter.Label(self, text='删除页面内容').pack()

class QueryFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root=master
        self.itemName=tkinter.StringVar()

        self.table_frame=tkinter.Frame(self)
        self.table_frame.pack()
        self.row=1

        self.create_page()

    def create_page(self):
        self.create_tree_view()
        self.show_data_frame()
        tkinter.Button(self, text='刷新数据', command=self.show_data_frame).pack(anchor=tkinter.E, pady=5)

    def show_data_frame(self):
        # 删除原节点
        for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass
        students = db.all()
        for index, stu in enumerate(students):
            print(stu)
            self.tree_view.insert('', index + 1,
                                  values=(str(stu['studentid']), stu['name'], str(stu['math']),
                                          str(stu['chinese']), str(stu['english']), str(stu['physics']),
                                          str(stu['chemistry']), str(stu['biology'])))

    def create_tree_view(self):
        # 表格
        columns = ("studentid", "name", "math", "chinese", "english", "physics", "chemistry", "biology")
        columns_value = ('学号', '姓名', '数学', '语文', '英语', '物理', '化学', '生物')
        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        self.tree_view.column('studentid', width=80, anchor='center')
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('math', width=80, anchor='center')
        self.tree_view.column('chinese', width=80, anchor='center')
        self.tree_view.column('english', width=80, anchor='center')
        self.tree_view.column('physics', width=80, anchor='center')
        self.tree_view.column('chemistry', width=80, anchor='center')
        self.tree_view.column('biology', width=80, anchor='center')
        self.tree_view.heading('studentid', text='学号')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('math', text='数学')
        self.tree_view.heading('chinese', text='语文')
        self.tree_view.heading('english', text='英语')
        self.tree_view.heading('physics', text='物理')
        self.tree_view.heading('chemistry', text='化学')
        self.tree_view.heading('biology', text='生物')
        self.tree_view.pack(fill=tkinter.BOTH, expand=True)


