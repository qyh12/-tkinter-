import json

class StudentsDB:
    # 学生信息管理系统数据模型
    def __init__(self):
        self.students = []
        # 加载本地文件中的数据
        self._load_students_data()

    def insert(self, student):
        self.students.append(student)

    def all(self):
        # 返回所有数据
        return self.students

    def search_by_name(self, name):
        # 查询列表中的数据
        for student in self.students:
            if student['name'] == name:
                return student
        return None  # If not found

    def modify_by_name(self, modified_student):
        # 修改列表中的数据
        for i, student in enumerate(self.students):
            if student['name'] == modified_student['name']:
                self.students[i] = modified_student
                break

    def delete_by_name(self, name):
        # 删除列表中的数据
        for i, student in enumerate(self.students):
            if student['name'] == name:
                del self.students[i]
                break

    def _load_students_data(self):
        try:
            with open('students.json', 'r') as file:
                self.students = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty list
            self.students = []

    def save_data(self):
        with open('students.json', 'w') as file:
            json.dump(self.students, file)

db=StudentsDB()

