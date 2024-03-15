from domain.entity import Entity


class Student(Entity):
    def __init__(self, idStudent, name, group, ):
        Entity.__init__(self, idStudent)
        self.__name = name
        self.__group = group

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_name(self, name):
        self.__name = name

    def set_group(self, group):
        self.__group = group

    def file_format(self):
        e = self.__str__()
        e = e.replace("[36m|  [0m", "")
        e = e.replace("ID: ", "")
        e = e.replace("Nume:  ", "")
        e = e.replace("Grupa:", "")
        e = e.replace("\n", "")
        return e

    def __str__(self):
        return f"\033[92m|  \033[0mID: {Entity.get_id_entity(self)} \n" \
               f"\033[92m|  \033[0mName:  {self.__name}\n" \
               f"\033[92m|  \033[0mGrupa: {self.__group}\n"
