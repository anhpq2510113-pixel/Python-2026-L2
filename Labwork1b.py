marks = {}
students = []
courses = []

def input_number_of_student():
    return int(input("Input number of students in a class: "))

def input_student_info():
    n = input_number_of_student()
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        s_id = str(input("ID: "))
        name = str(input("Name: "))
        dob = str(input("DOB: "))
        student = {
            "id": s_id,
            "name": name,
            "dob": dob
        }
        students.append(student)

def input_number_of_courses():
    return int(input("Input number of courses: "))

def input_courses_info():
    c = input_number_of_courses()
    for i in range(c):
        print(f"\n--- Course {i+1} ---")
        c_id = str(input("Course ID: ")) 
        course_name = str(input("Course Name: "))
        course = {
            "id": c_id,
            "name": course_name
        }
        courses.append(course)

def select_courses_input_mark():
    course_id = input("Enter course ID to input marks: ")
    # Kiểm tra khóa học có tồn tại không
    course_exists = any(c['id'] == course_id for c in courses)
    if not course_exists:
        print("Course ID does not exist!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark

def list_courses():
    if not courses:
        print("No courses available.")
        return
    print("\n--- Course List ---")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    if not students:
        print("No students available.")
        return
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_marks():
    course_id = input("Enter course ID to view marks: ")
    if course_id in marks:
        print(f"\n--- Marks for Course {course_id} ---")
        for student in students:
            student_mark = marks[course_id].get(student['id'], "No mark")
            print(f"{student['name']} (ID: {student['id']}): {student_mark}")
    else:
        print("No marks found for this course.")

def main():
    while True:
        print("\n================ MENU ================")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Select Course & Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks")
        print("0. Exit")
        
        choice = input("Select an option (0-6): ")
        
        if choice == '1':
            input_student_info()
        elif choice == '2':
            input_courses_info()
        elif choice == '3':
            select_courses_input_mark()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_marks()
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

   