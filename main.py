import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the Students dataset
students_df = pd.read_excel('Students.xlsx')

# Step 1: Stratify by Programme
# Calculate the proportion of students in each Programme
programme_counts = students_df['Programme'].value_counts(normalize=True)

# Create a column for group assignment
students_df['Group'] = None

for programme in programme_counts.index:
    # Get students in the current programme
    programme_df = students_df[students_df['Programme'] == programme]

    # Check if the group is too small to split
    if len(programme_df) < 2:
        # Randomly assign to control or experimental group
        students_df.loc[programme_df.index, 'Group'] = np.random.choice(['Control', 'Experimental'], size=len(programme_df))
    else:
        # Split into Control and Experimental groups
        control_group, experimental_group = train_test_split(
            programme_df, test_size=0.7, random_state=42
        )
        # Assign groups
        students_df.loc[control_group.index, 'Group'] = 'Control'
        students_df.loc[experimental_group.index, 'Group'] = 'Experimental'

# For small groups that couldn't be split, ensure they are assigned
unassigned_mask = students_df['Group'].isna()
students_df.loc[unassigned_mask, 'Group'] = np.random.choice(['Control', 'Experimental'], size=unassigned_mask.sum())

# Check the resulting groups
print(students_df['Group'].value_counts())
print(students_df.head())

# Save the new dataset
students_df.to_excel('Students_with_Groups.xlsx', index=False)
print("Students_with_Groups.xlsx created successfully!")
