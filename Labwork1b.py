marks = {}
students = []
courses = []
def input_number_of_student():
    n = int(input("Input number of students in a class:"))
    return n
def input_student_info():
    id = str(input("ID:"))
    name = str(input("Name:"))
    DoB = str(input("DOB:"))
    student = {
    "id": id,
    "name": name,
    "dob": DoB
}
    students.append(student)
    return students
def input_number_of_courses():
    c = int(input("Input number of courses:"))
    return c
def input_courses_info():
    c_id = str(input("Course ID:")) 
    course_name = str(input("Course Name:"))
    course = {
        "id": c_id,
        "name": course_name
    }
    courses.append(course)
    return courses
def select_courses_input_mark():
    course_id = input("Enter course ID: ")
    marks[course_id] = {}
    for student in students:
        mark = float(input(f"enter mark for{student['name']}:"))
        marks[course_id][student['id']] = mark

def list_course():
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")
def list_strudents():
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")
def show_marks():
    course_id = input("enter courses id to view mark:")
    if course_id in marks:
        for student in students:
            student_mark = marks[course_id].get(student['id'], "no mark")
            print(f"{student['name']} {student_mark}")
    else:
        print("no mark dound in this course.")

   