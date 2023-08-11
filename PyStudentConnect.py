import csv

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def edit_student(self, student_id, new_name, new_age, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.name = new_name
                student.age = new_age
                student.grade = new_grade
                print("Student information updated successfully!")
                return
        print("Student not found.")

    def view_students(self):
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student_by_name(self, name):
        matching_students = [student for student in self.students if name.lower() in student.name.lower()]
        if matching_students:
            print(f"Students matching '{name}':")
            for student in matching_students:
                print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
        else:
            print("No students found with that name.")

    def generate_student_report(self):
        with open("student_report.txt", "w") as f:
            f.write("Student Report\n\n")
            for student in self.students:
                f.write(f"ID: {student.student_id}\n")
                f.write(f"Name: {student.name}\n")
                f.write(f"Age: {student.age}\n")
                f.write(f"Grade: {student.grade}\n")
                f.write("\n")

    def save_to_csv(self):
        with open("students.csv", "w", newline="") as csvfile:
            fieldnames = ["ID", "Name", "Age", "Grade"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow({"ID": student.student_id, "Name": student.name, "Age": student.age, "Grade": student.grade})

    def load_from_csv(self):
        try:
            with open("students.csv", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student = Student(row["ID"], row["Name"], row["Age"], row["Grade"])
                    self.students.append(student)
        except FileNotFoundError:
            print("No student data found.")

def main():
    student_system = StudentManagementSystem()
    student_system.load_from_csv()

    while True:
        print("\nPyStudentConnect - Student Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Edit Student Information")
        print("4. View Students")
        print("5. Search Students by Name")
        print("6. Generate Student Report")
        print("7. Save to CSV")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Student Grade: ")
            student = Student(student_id, name, age, grade)
            student_system.add_student(student)
            print("Student added successfully!")

        elif choice == "2":
            student_id = input("Enter Student ID to remove: ")
            student_system.remove_student(student_id)
            print("Student removed successfully!")

        elif choice == "3":
            student_id = input("Enter Student ID to edit: ")
            new_name = input("Enter new Name: ")
            new_age = input("Enter new Age: ")
            new_grade = input("Enter new Grade: ")
            student_system.edit_student(student_id, new_name, new_age, new_grade)

        elif choice == "4":
            print("\nList of Students:")
            student_system.view_students()

        elif choice == "5":
            search_name = input("Enter the name to search: ")
            student_system.search_student_by_name(search_name)

        elif choice == "6":
            student_system.generate_student_report()
            print("Student report generated.")

        elif choice == "7":
            student_system.save_to_csv()
            print("Data saved to CSV.")

        elif choice == "8":
            print("Exiting PyStudentConnect. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
