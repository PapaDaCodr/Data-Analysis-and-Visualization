import pandas as pd
import numpy as np

# Load the Students dataset
students_df = pd.read_excel('Students.xlsx')

# Define the number of students with clashes
num_clashes = 35

# Randomly select students for clashes
clash_students = np.random.choice(students_df['Student ID'], num_clashes, replace=False)

# Randomly assign clashes during Main Class or Tutorial Class
clash_periods = np.random.choice(['Main Class', 'Tutorial Class (Current)'], num_clashes)

# Create DataFrame for clashes
clashes_df = pd.DataFrame({
    'Student ID': clash_students,
    'Clash Period': clash_periods
})

# Save to Excel
clashes_df.to_excel('Clashes.xlsx', index=False)

print("Clashes.xlsx created successfully!")
