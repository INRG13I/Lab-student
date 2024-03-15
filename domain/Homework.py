from domain.entity import Entity


class Homework(Entity):
    def __init__(self, idLab, idStudent, grade):
        Entity.__init__(self, idLab)
        self.__idStudent = idStudent
        self.__grade = grade

    def get_idStudent(self):
        return self.__idStudent

    def get_grade(self):
        return self.__grade

    def set_idStudent(self, idStudent):
        self.__idStudent = idStudent

    def set_grade(self, grade):
        self.__grade = grade

    def file_format(self):
        e = self.__str__()
        e = e.replace("[36m|  [0m", "")
        e = e.replace("Lab: ", "")
        e = e.replace("Student: ", "")
        e = e.replace("Nota:  ", "")
        e = e.replace("\n", "")
        return e

    def __str__(self):
        return f"\033[92m|  \033[0mLab: {self.get_id_entity()} \n" \
               f"\033[92m|  \033[0mStudent: {self.__idStudent} \n" \
               f"\033[92m|  \033[0mNota:  {self.__grade}\n"