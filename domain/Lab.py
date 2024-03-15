from domain.entity import Entity


class Laborator(Entity):
    def __init__(self, id_Lab, idProblem, description, deadline_day, deadline_month, deadline_year):
        Entity.__init__(self, id_Lab)
        self.__idProblem = idProblem
        self.__description = description
        self.__deadline_day = deadline_day
        self.__deadline_month = deadline_month
        self.__deadline_year = deadline_year

    def get_idProblem(self):
        return self.__idProblem

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline_day, self.__deadline_month, self.__deadline_year

    def set_idProblem(self, idProblem):
        self.__idProblem = idProblem

    def set_description(self, description):
        self.__description = description

    def set_deadline(self, deadline_day, deadline_month, deadline_year):
        self.__deadline_day = deadline_day
        self.__deadline_month = deadline_month
        self.__deadline_year = deadline_year

    def file_format(self):
        e = self.__str__()
        e = e.replace("[36m|  [0m", "")
        e = e.replace("ID: ", "")
        e = e.replace("Problema:  ", "")
        e = e.replace("Descriere:", "")
        e = e.replace("Deadline: ", "")
        e = e.replace("\n", "")
        return e

    def __str__(self):
        return f"\033[92m|  \033[0mLab: {Entity.get_id_entity(self)} \n" \
               f"\033[92m|  \033[0mProblema: {self.__idProblem} \n" \
               f"\033[92m|  \033[0mDescriere: {self.__description} \n" \
               f"\033[92m|  \033[0mDeadline:  {self.__deadline_day}.{self.__deadline_month}.{self.__deadline_year}\n"