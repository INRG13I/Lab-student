from domain.Homework import Homework
from domain.Lab import Laborator
from domain.Student import Student
from repository.repository import Repository


class Service:
    def __init__(self, entity_repository: Repository):
        """
        constructor for service
        :param entity_repository: Repository Object
        """
        self.__entity_repository = entity_repository

    def file_input(self):
        return self.__entity_repository.file_input()

    def file_add(self, entity):
        """
        Adds entity to repository
        :param entity:
        :return:
        """
        self.__entity_repository.file_add(entity)

    def get_all_entities(self):
        """
        returns a dictionary of all entities
        :return: dict
        """
        return self.__entity_repository.get_all()

    def get_entity_by_id(self, id_entity):
        """
        returns entity of specified id
        :param id_entity: int
        :return:
        """
        return self.__entity_repository.get_by_id(id_entity)

    def add_entity(self, entity):
        """
        adds entity to repository
        :param entity: Object
        :return:
        """
        self.__entity_repository.add(entity)

    def update_entity(self, entity):
        """
        updates and entity
        :param entity: Object
        :return:
        """
        self.__entity_repository.modify(entity)

    def delete_entity(self, id_entity):
        """
        deletes an entity
        :param id_entity: int
        :return:
        """
        self.__entity_repository.delete(id_entity)

class StudentService(Service):

    def create_student(self, id_client, name, group):
        """
        Crates a Client Class object and returns it
        :param id_client: int
        :param name: str
        :param group: int
        :return: Student Class Object
        """
        entity = Student(id_client, name, group)
        return entity

    def student_file_input(self):
        """
        Adds entities
        :return:
        """
        for e in Service.file_input(self):
            e = e.split(" ")
            entity = self.create_student(int(e[0]), e[1], int(e[2]))
            Service.file_add(self, entity)

class LaboratorService(Service):

    def create_lab(self, id_Lab, idProblem, description, deadline_day, deadline_month, deadline_year):
        """
        Creates a Book Class object and returns it
        :param id_Lab: int
        :param idProblem: int
        :param description: str
        :param deadline_day: int
        :param deadline_month: int
        :param deadline_year: int
        :return: Laborator Class Object
        """
        entity = Laborator(id_Lab, idProblem, description, deadline_day, deadline_month, deadline_year)
        return entity

    def lab_file_input(self):
        """
        Adds entities
        :return:
        """
        for e in Service.file_input(self):
            e = e.split(" ")
            print(e)
            entity = self.create_lab(int(e[0]), int(e[1]), e[2], int(e[3]), int(e[4]), int(e[5]))
            Service.file_add(self, entity)

class HomeworkService(Service):
    def __init__(self, homework_repository: Repository, *args):
        """
        Constructor For service
            Needs to be initialized with:
                ->Homework_Repo
                ->Student_Repo
        :param Homework_repository: Repository Object
        :param args:
        """
        Service.__init__(self, homework_repository)
        self.__student_repository = args[0]

    def homework_file_input(self):
        """
        Adds entities
        :return:
        """
        for e in Service.file_input(self):
            e = e.split(" ")
            entity = self.create_homework(int(e[0]), int(e[1]), int(e[2]))
            Service.file_add(self, entity)

    def create_homework(self, id_lab, id_student,grade):
        """
        Crates a Rent Class Object and returns it
        :param id_lab: int
        :param id_student: int
        :param grade: int
        :return: Homework Class Object
        """
        entity = Homework(id_lab, id_student, grade)
        return entity

    def get_student_and_names(self):
        """
        Makes a list of dicts
        :return: List
        """
        new_list = []
        for e in self.__student_repository.get_all():
            new_list.append({'id_student': e.get_id_entity(), 'name': e.get_name()})
        return new_list

    def sort_students_by_name(self, client_list):
        """
        Sorts list by name key
        :param client_list: list of dicts
        :return: list of dicts
        """
        return sorted(client_list, key=lambda d: d['name'])


    def getAllHomework(self):
        return self.__homeworkRepository.getAll()

    def getHomeworkById(self, idLab):
        return self.__homeworkRepository.getById(idLab)

    def addHomework(self, idLab, idStudent):
        homework = Homework(idLab, idStudent,0)
        self.__homeworkRepository.add(homework,idLab,idStudent)

    def updateHomework(self, idLab, idStudent, grade):
        homework = Homework(idLab, idStudent, grade)
        self.__homeworkRepository.modify(homework)

    def deleteHomework(self, idLab):
        self.__homeworkRepository.delete(idLab)