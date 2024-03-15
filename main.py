from repository.repository import Repository
from service.service import StudentService, LaboratorService, HomeworkService
from ui.console import Console

if __name__ == '__main__':
    studentRepository =Repository('student_saved_file')
    laboratorRepository =Repository('lab_saved_file')
    homeworkRepository = Repository('homework_saved_file')
    studentService = StudentService(studentRepository)
    laboratorService = LaboratorService(laboratorRepository)
    homeworkService = HomeworkService(homeworkRepository, studentRepository)
    console = Console(studentService, laboratorService, homeworkService)
    console.menu()