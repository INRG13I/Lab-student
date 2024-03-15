import sys

from exceptions.exceptions import DuplicateIdError
from service.service import StudentService, LaboratorService, HomeworkService


class Console:
    def __init__(self, studentService: StudentService, laboratorService: LaboratorService, homeworkService: HomeworkService):
        self.__studentService = studentService
        self.__laboratorService = laboratorService
        self.__homeworkService = homeworkService

    def print_options(self):
        print('\033[92m' + "1.Adaugare" + '\033[0m \n')
        print('\033[92m' + "2.Stergere" + '\033[0m \n')
        print('\033[92m' + "3.Modificari" + '\033[0m \n')
        print('\033[92m' + "4.Cautari" + '\033[0m \n')
        print('\033[92m' + "5.Asignare lab unui student" + '\033[0m \n')
        print('\033[92m' + "6.Notare laborator student" + '\033[0m \n')
        print('\033[92m' + "7.Afisari" + '\033[0m')
        # print('\033[92m' + "8.Statistici" + '\033[0m')
        # print("  11.Lista studenti si notele lor la un laborator dat.\n"
        #       # todo(cere id lab apoi daca se doreste ordonarea dupa note sau dupa nume)
        #       "  12.Toti studentii cu media laborator mai mica decat 5.\n"
        #       # todo(afiseaza numele student si media sa)
        #       )
        print("\033[91m  x.Iesire\033[0m\n")

    def file_input_submenu(self):
        try:
            options = {"1": self.file_input_students(),
                       "2": self.file_input_labs(),
                       "3": self.file_input_homeworks()}

            print("\n\u001b[36m1.\033[0m    Incarca Date din repo Studenti\n"
                  "\u001b[36m2.\033[0m    Incarca Date din repo Labs\n"
                  "\u001b[36m3.\033[0m    Incarca Date din repo Homeworks")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[31mOptiunea aleasa nu exista !!!")

    def file_input_labs(self):
        try:
            self.__laboratorService.lab_file_input()
        except ValueError:
            print("\u001b[31m Ooops nu am reusit sa obtinem valorile din repo!!!")

    def file_input_students(self):
        try:
            self.__studentService.student_file_input()
        except ValueError:
            print("\u001b[31m Ooops nu am reusit sa obtinem valorile din repo!!!")

    def file_input_homeworks(self):
        try:
            self.__homeworkService.homework_file_input()
        except ValueError:
            print("\u001b[31m Ooops nu am reusit sa obtinem valorile din repo!!!")

    def addSubMenu(self):
        try:
            options = {"1": self.addStudent, "2": self.addLaborator}
            print("\u001b[36m1.\033[0m  Adauga student\n"  # (cere id,nume,grupa nou student)
                  "\u001b[36m2.\033[0m  Adauga lab")  # (cere idlab,idproblema,descriere,deadline)
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[31mOptiunea aleasa nu exista !!!")

    def addStudent(self):
        idStudent = int(input("Insereaza id-ul studentului: "))
        name = input("Numele studentului: ")
        group = int(input("Grupa din care face parte studentul:"))
        print()
        try:
            self.__studentService.add_entity(self.__studentService.create_student(idStudent, name, group))
            print("\033[93mStudent adaugat.\033[0m\n")
        except ValueError:
            print("\033[93m")
            print("Id-ul si grupa trebuie sa fie formate doar din cifre !!!")
            print("\033[0m\n")
        except DuplicateIdError as die:
            print(die)

    def addLaborator(self):
        idLab = int(input("Insereaza id-ul laboratorului: "))
        idProblem = int(input("Insereaza id-ul problemei: "))
        description = input("Descrierea problemei: ")
        date = input("Deadline de forma zi.luna.an : ")
        print()
        date = date.strip()
        date = date.split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        try:
            self.__laboratorService.add_entity(self.__laboratorService.create_lab(idLab, idProblem, description, day, month, year))
            print("\033[93mLaborator adaugat.\033[0m\n")
        except KeyError:
            print("\033[93m")
            print("Id-ul trebuie sa fie format doar din cifre !!!")
            print("\033[0m\n")
        except DuplicateIdError as die:
            print(die)

    def delete_sub_menu(self):
        try:
            options = {"1": self.deleteStudent, "2": self.deleteLaborator}
            print("\n\u001b[36m1.\033[0m  Sterge student\n"
                  "\u001b[36m2.\033[0m  Sterge lab")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[31mOptiunea aleasa nu exista !!!")

    def deleteStudent(self):
        idStudent = int(input("Insereaza id-ul studentului: "))
        print()
        try:
            self.__studentService.delete_entity(idStudent)
            print("\033[93mStudent sters.\033[0m\n")
        except KeyError:
            print("\033[93m")
            print("Optiunea aleasa nu exista !!!")
            print("\033[0m\n")

    def deleteLaborator(self):
        idLaborator = int(input("Insereaza id-ul laboratorului: "))
        print()
        try:
            self.__laboratorService.delete_entity(idLaborator)
            print("\033[93mLaborator sters.\033[0m\n")
        except KeyError:
            print("\033[93m")
            print("Id-ul trebuie sa fie format doar din cifre !!!")
            print("\033[0m\n")

    def modify_sub_menu(self):
        try:
            options = {"1": self.modifyStudent, "2": self.modifyLab}
            print("\n\u001b[36m1.\033[0m  Modifica student\n"
                  "\u001b[36m2.\033[0m  Modifica lab")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[31mOptiunea aleasa nu exista !!!")

    def modifyStudent(self):
        idStudent = int(input("Insereaza id-ul studentului: "))
        newName = input("Numele studentului: ")
        newgroup = int(input("Grupa studentului: "))
        print()
        try:
            self.__studentService.add_entity(self.__studentService.create_student(idStudent, newName, newgroup))
            print("\033[93mStudent modificat.\033[0m\n")
        except KeyError:
            print("\033[93m")
            print("Id-ul trebuie sa fie format doar din cifre !!!")
            print("\033[0m\n")

    def modifyLab(self):
        idLab = int(input("Insereaza id-ul laboratorului: "))
        newidProblem = input("Insereaza id-ul problemei: ")
        newdescription = input("Descrierea problemei: ")
        date = input("Data de forma zi.luna.an : ")
        print()
        date = date.strip()
        date = date.split('.')
        newday = int(date[0])
        newmonth = int(date[1])
        newyear = int(date[2])
        try:
            self.__laboratorService.update_entity(self.__laboratorService.create_lab(idLab, newidProblem, newdescription, newday, newmonth, newyear))
            print("\033[93mLaborator modificat.\033[0m\n")
        except ValueError:
            print("\033[93m")
            print("Id-ul trebuie sa fie format doar din cifre !!!")
            print("\033[0m\n")
        except KeyError as ke:
            print(ke)

    def lookup_sub_menu(self):
        try:
            options = {"1": self.lookupStudent, "2": self.lookupLab}
            print("\n\u001b[36m1.\033[0m  Cauta student\n"
                  "\u001b[36m2.\033[0m  Cauta lab")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[31mOptiunea aleasa nu exista !!!")

    def lookupStudent(self):
        idStudent = int(input("Inserati id studentului: "))
        try:
            print(self.__studentService.get_entity_by_id(idStudent))
        except KeyError as ke:
            print("\033[93m")
            print(ke)
            print("\033[0m\n")
        except ValueError:
            print("\033[93m")
            print("\u001b[31m Id-ul trebuie sa fie format doar din cifre !!!")
            print("\033[0m\n")

    def lookupLab(self):
        idLab = int(input("Inserati id laboratorului: "))
        try:
            print(self.__laboratorService.get_entity_by_id(idLab))
        except KeyError as ke:
            print("\033[93m")
            print(ke)
            print("\033[0m\n")
        except ValueError:
            print("\033[93m")
            print("\u001b[31m Id-ul trebuie sa fie format doar din cifre !!!")
            print("\033[0m\n")

    def assignstudent(self):
        idLab = int(input("Insereaza id laboratorului: "))
        idStudent = int(input("Insereaza id student: "))
        print()
        try:
            self.__homeworkService.addHomework(idLab, idStudent)
            print("\033[93mAsignare cu succes.\033[0m\n")
        except KeyError as ke:
            print("\033[93m")
            print(ke)
            print("\033[0m\n")

    def gradestudent(self):
        idLab = int(input("Insereaza id laborator: "))
        idStudent = int(input("Insereaza id student: "))
        grade=int(input("Insereaza nota: "))
        print()
        try:
            self.__homeworkService.updateHomework(idLab, idStudent,grade)
            print("\033[93mNotare cu succes.\033[0m\n")
        except KeyError as ke:
            print("\033[93m")
            print(ke)
            print("\033[0m\n")

    def lab_grade_menu(self):
        options = {"1": self.lab_grade_ase, "2": self.lab_grade_des}
        print("\u001b[36m1.\033[0m  Ordonare crescatoare\n"
              "\u001b[36m2.\033[0m  Ordonare descrescatoare")
        option = input("Optiunea aleasa: ")
        id_lab=input("Id laborator")
        options[option](id_lab)

    def lab_grade_ase(self,id_lab):
        pass

    def lab_grade_des(self,id_lab):
        pass

    def print_all_sub_menu(self):
        try:
            options = {"1": self.printAllStudents, "2": self.printAllLabs()}
            print("\n\u001b[36m1.\033[0m  Afiseaza studenti \n"
                  "\u001b[36m2.\033[0m  Afiseaza labs")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[31mOptiunea aleasa nu exista !!!")

    def printAllStudents(self):
        for entity in self.__studentService.get_all_entities():
            print(entity)

    def printAllLabs(self):
        for entity in self.__laboratorService.get_all_entities():
            print(entity)

    def exit(self):
        sys.exit("\033[93mVa multumim ca ati ales sa folositi aceasta aplicatie !!!")

    def menu(self):
        options = {"1": self.addSubMenu,
                   "2": self.delete_sub_menu,
                   "3": self.modify_sub_menu,
                   "4": self.lookup_sub_menu,
                   "5": self.assignstudent,
                   "6": self.gradestudent,
                   "7": self.print_all_sub_menu(),
                   #"8": self.statistics_submenu,
                   "x": self.exit
                   }
        while True:
            self.print_options()
            opt = input("Optiunea: ")
            try:
                options[opt]()
            except KeyError as ke:
                print("Optiune inexistenta", ke)
