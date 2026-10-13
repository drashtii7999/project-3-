students = []
all_subjects = set()

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")

        subjects = [s.strcdip() for s in subjects]
        student_info = {
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Grade": grade,
            "DOB": dob,
            "Subjects": subjects
        }

        student_info["ID_DOB"] = (student_id, dob)
        students.append(student_info)
        all_subjects.update(subjects)

        print("Student added successfully!")

    elif choice == "2":
        print("\n--- Display All Students ---")

        if not students:
            print("No student records found.")
        else:
            for student in students:
                print(
                    f"Student ID: {student['ID']} | "
                    f"Name: {student['Name']} | "
                    f"Age: {student['Age']} | "
                    f"Grade: {student['Grade']} | "
                    f"Subjects: {', '.join(student['Subjects'])}"
                )

    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        for student in students:
            if student["ID"] == student_id:
                print("1. Update Age")
                print("2. Update Subjects")
                update_choice = input("Enter your choice: ")

                if update_choice == "1":
                    student["Age"] = int(input("Enter new age: "))
                    print("Age updated successfully!")

                elif update_choice == "2":
                    new_subjects = input(
                        "Enter new subjects (comma-separated): "
                    ).split(",")

                    new_subjects = [s.strip() for s in new_subjects]
                    student["Subjects"] = new_subjects
                    all_subjects.update(new_subjects)

                    all_subjects.clear()
                    for s in students:
                        all_subjects.update(s["Subjects"])

                    print("Subjects updated successfully!")
                else:
                    print("Invalid update choice.")
                break
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

        all_subjects.clear()
        for student in students:
            all_subjects.update(student["Subjects"])

    elif choice == "5":
        print("\n--- Subjects Offered ---")

        if all_subjects:
            for subject in sorted(all_subjects):
                print(subject)
        else:
            print("No subjects available.")

    elif choice == "6":
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Please try again.")