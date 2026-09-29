#intialising dictionary
student_marks = {}

#function to calculate letter grade based on marks
def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

#function for adding students's information
def info(name, marks):
    if 0 <= marks <= 100:
        grade = get_grade(marks)
        student_marks[name] = {"marks": marks, "grade": grade}
        print(f"added{name} with {marks}/100 (Grade: {grade})")
    else:
        print("enter marks between 0 and 100")

#function for upadating information
def update(name, marks):
    if name in student_marks:
        if 0 <= marks <= 100:
            grade = get_grade(marks)
            student_marks[name] = {"marks": marks, "grade": grade}
            print(f"{name} with marks are updated {marks} (Grade: {grade}) ")
        else:
            print("enter marks between 0 and 100")
    else:
        print(f"{name} not found")

#function for deleting 
def delete(name):
    if name in student_marks:
        del student_marks[name]
        print(f"{name} has been deleted")
    else:
        print(f"{name} not found")

#function for viewing all students
def displayall():
    if student_marks:
        for name, data in student_marks.items():
            print(f"{name} : {data['marks']}/100 | Grade: {data['grade']}")

    else:
        print(f"no student found")

#function to view grade of a specific student
def view_grade(name):
    if name in student_marks:
        data = student_marks[name]
        print(f"{name}'s Marks: {data['marks']}/100 | Grade: {data['grade']}")
    else:
        print(f"{name} not found")

#function for calculating class average
def calculate_average():
    if student_marks:
        total = sum(data["marks"] for data in student_marks.values())
        avg = total / len(student_marks)
        avg_grade = get_grade(avg)
        print(f"class average Marks: {avg:.2f}/100 | average grade: {avg_grade}")
    else:
        print("no student found to calculate average")


def main():
    while True:
        print('\n STUDENT MARKS MANAGEMENT SYSTEM')
        print("Press 1 to add information")
        print("Press 2 to upadate information")
        print("Press 3 to delete information")
        print("Press 4 to view information")
        print("Press 5 to view a student's assigned grade")
        print("Press 6 to calculate class average")
        print("Press 7 t0 exit")

        choice = int(input("Enter your choice"))
        if choice == 1:
            name = input("Enter student name :")
            marks = float(input("Enter student marks out of 100 :"))
            info(name, marks)

        elif choice == 2:
             name = input("Enter student name :")
             marks = float(input("Enter student marks out of 100 :"))
             update(name, marks)

        elif choice == 3:
            name = input("Enter student name :")
            delete(name)

        elif choice == 4:
            displayall()

        elif choice == 5:
            name = input("Enter student name :")
            view_grade(name)

            

        elif choice == 6:
            calculate_average()

        elif choice == 7:
            print("CLOSING PROGRAM")
            break

        else:
            print("Invalid Choice")

if __name__=='__main__':
       main()
