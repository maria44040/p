class Course:
    course_id = 1000
    course_level = ["A", "B", "C"]

    def __init__(self, course_name, course_level):
        self.id = Course.course_id
        Course.course_id += 1
        self.name = course_name
        self.level = course_level


class Student:
    student_id = 2023000

    def __init__(self, student_name, student_level):
        self.stid = Student.student_id
        Student.student_id += 1
        self.name = student_name
        self.level = student_level
        self.courses =[]

    def add_course(self, new_course):
        if new_course.level == self.level:
            self.courses.append(new_course)
            return f"Added {new_course.name} successfully."
        else:
            return f"Failed to add {new_course.name}. The course level does not match the student's level."

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.stid}")
        print(f"Student Level: {self.level}")

        if len(self.courses) > 0:
            print("Courses Enrolled:")
            for course in self.courses:
                print(f"- {course.name} (Level: {course.level})")
        else:
            print("No courses enrolled.")


class SchoolSystem:
    students = []
    courses = []

    @classmethod
    def add_student(cls):
        name = input("Enter student name: ")

        while True:
            level = input("Enter student level (A/B/C): ")

            if level in Course.course_level:
                break

            print("Invalid level. Please select A, B, or C.")

        student = Student(name, level)
        cls.students.append(student)

        print("Student saved successfully.")

    @classmethod
    def remove_student(cls):
        student_id = int(input("Enter student ID: "))

        for student in cls.students:
            if student.stid == student_id:
                cls.students.remove(student)
                print("Delete done successfully.")
                return

        print("User does not exist.")

    @classmethod
    def edit_student(cls):
        student_id = int(input("Enter student ID: "))

        for student in cls.students:
            if student.stid == student_id:
                new_name = input("Enter new name: ")

                while True:
                    new_level = input("Enter new level (A/B/C): ")

                    if new_level in Course.course_level:
                        break

                    print("Invalid level. Please select A, B, or C.")

                student.name = new_name
                student.level = new_level

                print("Student details updated successfully.")
                return

        print("User does not exist.")

    @classmethod
    def display_students(cls):
        if len(cls.students) > 0:
            for student in cls.students:
                print("*" * 20)
                student.display_details()
        else:
            print("No students found.")

    @classmethod
    def create_course(cls):
        course_name = input("Enter course name: ")

        while True:
            course_level = input("Enter course level (A/B/C): ")

            if course_level in Course.course_level:
                break

            print("Invalid level. Please select A, B, or C.")

        course = Course(course_name, course_level)
        cls.courses.append(course)

        print(f"Course '{course.name}' created successfully.")

    @classmethod
    def add_course_to_student(cls):
        stid = int(input("Enter student ID: "))

        for student in cls.students:
            if student.stid == stid:
                course_id = int(input("Enter course ID: "))

                for course in cls.courses:
                    if course.id == course_id:
                        result = student.add_course(course)
                        print(result)
                        return

                print("Course does not exist.")
                return

        print("Student does not exist.")


# Example usage:

while True:
    print("\n--- School System Menu ---")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display All Students")
    print("5. Create New Course")
    print("6. Add Course to Student")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        SchoolSystem.add_student()
    elif choice == "2":
        SchoolSystem.remove_student()
    elif choice == "3":
        SchoolSystem.edit_student()
    elif choice == "4":
        SchoolSystem.display_students()
    elif choice == "5":
        SchoolSystem.create_course()
    elif choice == "6":
        SchoolSystem.add_course_to_student()
#   p  
 