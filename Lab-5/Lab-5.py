total_marks = 80
marks = [55, 67, 65, 45]
students = ["Sahil", "Om", "Juveriya", "Sanvade"]
n = len(marks)

def calculate_percentage(marks_obtained):
    percentage = (marks_obtained / total_marks) * 100
    return percentage

for i in range(n):
    result = calculate_percentage(marks[i])
    print(f"{students[i]} scored {result} % in exam.")
