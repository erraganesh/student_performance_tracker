from students import add_student, get_top_performers
from courses import add_course, course_average
from marks import record_marks, calculate_gpa, generate_report_card
from attendance import record_attendance, attendance_summary

def main():
    while True:
        print("\n" + "="*50)
        print("      STUDENT PERFORMANCE TRACKER")
        print("="*50)
        print("""
        1. Add New Student
        2. Add New Course
        3. Record Marks
        4. Record Attendance
        5. Calculate GPA
        6. Generate Report Card
        7. View Top Performers
        8. View Course-Wise Averages
        9. View Attendance Summary
        10. Exit
        """)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(
                input("Student ID: "),
                input("Student Name: "),
                input("Grade: ")
            )

        elif choice == "2":
            add_course(
                input("Course ID: "),
                input("Course Name: "),
                input("Instructor: ")
            )

        elif choice == "3":
            record_marks(
                input("Student ID: "),
                input("Course ID: "),
                int(input("Marks (0-100): "))
            )

        elif choice == "4":
            record_attendance(
                input("Student ID: "),
                input("Course ID: "),
                input("Present? (yes/no): ").lower() == "yes"
            )

        elif choice == "5":
            calculate_gpa(input("Student ID: "))

        elif choice == "6":
            generate_report_card(input("Student ID: "))

        elif choice == "7":
            grade = input("Enter Grade (e.g., 9, 10): ")
            count = int(input("Number of top performers to view: "))
            get_top_performers(grade, count)

        elif choice == "8":
            course_average(input("Enter Course ID: "))

        elif choice == "9":
            attendance_summary(input("Enter Student ID: "))

        elif choice == "10":
            print("Thank you for using Student Performance Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()
