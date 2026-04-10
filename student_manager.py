class StudentManager:
    # list
    def __init__(self):
        self.__student_list = []

    def add_student(self, student):
        for s in self.__student_list:
            if s.student_id == student.student_id:
                raise ValueError("The student ID is exist")
        self.__student_list.append(student)

    def delete_by_id(self, student_id):
        for s in self.__student_list:
            if s.student_id == student_id:
                self.__student_list.remove(s)
                return True
        raise ValueError("The student ID is not exist")

    def get_all(self):
        return self.__student_list.copy()

    def sort_students(self, strategy):
        # 多态调用
        return strategy.sort(self.__student_list)
