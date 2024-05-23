import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define the number of students
num_students = 100

# Generating random data
student_ids = [f'S{str(i).zfill(3)}' for i in range(1, num_students + 1)]
ages = np.random.choice([18, 19, 20,21, 22, 23], num_students)
genders = np.random.choice(['Male', 'Female'], num_students)
programme_types = np.random.choice(['Undergraduate',], num_students)
programmes = np.random.choice(['Computer Science', 'Mathematics', 'Statistics', 'Information Technology'], num_students)

cgpas = np.random.choice([1.4,1.6,1.8,1.5,1.9,2.0,2.6,3.8,2.8], num_students)

# Created DataFrame
students_df = pd.DataFrame({
    'Student ID': student_ids,
    'Age': ages,
    'Gender': genders,
    'Programme Type': programme_types,
    'Programme': programmes,
    'CGPA': cgpas
})

# Save to Excel
students_df.to_excel('Students.xlsx', index=False)
print("Students.xlsx created successfully!")
