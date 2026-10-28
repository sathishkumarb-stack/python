
import numpy as np

# 1. Create a NumPy array (4 students x 3 subjects)
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

# Print array properties
print("Marks:\n", marks)
print("Shape:", marks.shape)
print("Data type:", marks.dtype)
print("Size:", marks.size)

# 2. Slice first two students and last subject
print("\nFirst two students, last subject:")
print(marks[:2, -1])

# 3. Calculate averages
student_avg = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)

print("\nStudent averages:", np.round(student_avg, 2))
print("Subject averages:", subject_avg)

# 4. Broadcasting: add 5 grace marks
grace_marks = marks + 5

print("\nMarks after adding 5 grace marks:")
print(grace_marks)

# 5. Weighted scores using matrix multiplication
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = marks @ weights

print("\nWeighted scores:", np.round(weighted_scores, 2))

# 6. Reshape numbers from 0 to 11 into a 3x4 array
arr = np.arange(12).reshape(3, 4)

print("\nReshaped array:")
print(arr)
