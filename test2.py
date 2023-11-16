#主页面
import tkinter
from test3 import InsertFrame, SearchFrame,ModifyFrame,DeleteFrame,QueryFrame


class Mainpage:
    def __init__(self,root2):
        self.root=root2
        self.root.title('学生信息管理系统 V1')
        self.root.geometry('600x550')
        self.create_page()

        #自定义组件
        self.insert_frame=InsertFrame(self.root)
        self.insert_frame.pack()

        self.search_frame = QueryFrame(self.root)
        # self.search_frame.pack()

        self.modify_frame = ModifyFrame(self.root)
        # self.modify_frame.pack()

        self.delete_frame = DeleteFrame(self.root)
        # self.delete_frame.pack()



    def create_page(self):
        menu_ba=tkinter.Menu(self.root)

        menu_ba.add_command(label='插入', command=self.show_insert_frame)
        menu_ba.add_command(label='查询', command=self.show_search_frame)
        menu_ba.add_command(label='修改', command=self.show_modify_frame)
        menu_ba.add_command(label='删除', command=self.show_delete_frame)

        self.root['menu']=menu_ba #设置菜单栏

    def show_insert_frame(self):
        self.insert_frame.pack()
        self.search_frame.forget()
        self.modify_frame.forget()
        self.delete_frame.forget()

    def show_search_frame(self):
        self.insert_frame.forget()
        self.search_frame.pack()
        self.modify_frame.forget()
        self.delete_frame.forget()

    def show_modify_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.modify_frame.pack()
        self.delete_frame.forget()

    def show_delete_frame(self):
        self.insert_frame.forget()
        self.search_frame.forget()
        self.modify_frame.forget()
        self.delete_frame.pack()


# root=tkinter.Tk()
#
# Mainpage(root)
#
# root.mainloop()