
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)



my_list = [2, 8, 4, 1, 7]

largest_number = None

for scores in student_scores:
    if largest_number is None or largest_number < scores:
        largest_number = scores

# ✅ get the largest number
print(f"The highest score in the class is: {largest_number}")  # 👉️ 8


