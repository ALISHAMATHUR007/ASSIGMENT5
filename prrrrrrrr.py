
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}

# # Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display the marks, or show a message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")

    # -----------------task2----------------
numbers = list(range(1, 11))
print("Original list :",numbers)
# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_five = first_five[::-1]

# Step 4: Print both lists
print(" extract First five elements:", first_five)
print("Reversed extract elements:", reversed_five)
