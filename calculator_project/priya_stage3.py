name = input("Enter student name: ")

def get_valid_mark(subject):
    while True:
        try:
            mark = int(input(f"Enter mark for {subject}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid mark! Enter between 0 and 100.")
        except:
            print("Please enter a valid number.")

mark_1 = get_valid_mark("Subject 1")
mark_2 = get_valid_mark("Subject 2")
mark_3 = get_valid_mark("Subject 3")

total = mark_1 + mark_2 + mark_3
percentage = round((total / 300) * 100, 2)

print("\nStudent Name:", name)
print(f"Total: {total}/300")
print(f"Percentage: {percentage}%")

if percentage >= 75:
    print("Grade A")
elif percentage >= 60:
    print("Grade B")
elif percentage >= 40:
    print("Grade C")
else:
    print("Grade F")
