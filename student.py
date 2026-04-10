class Person:
    def __init__(self, name):
        self.__name = name  # sale and package:privaate property

    @property
    def name(self):
        return self.__name
    
class Student(Person):
    def __init__(self, student_id, name, score):
        super().__init__(name)
        self.__student_id = student_id
        self.__score = score # seal and package
    @property
    def student_id(self):
        return self.__student_id

    @property
    def score(self):
        return self.__score

    def __str__(self):
        return f"Student number：{self.__student_id}，NAME：{self.name}，MARK：{self.__score}"
