import pandas as pd
import numpy as np

# -------------------------------
# Configurations
# -------------------------------
num_tasks = 5000  # total tasks in dataset
task_types = ['Customer Support', 'Billing', 'Technical', 'HR']
assigned_options = ['Human', 'AI']
urgency_levels = ['Low', 'Medium', 'High']

# -------------------------------
# Generate Dataset
# -------------------------------
data = pd.DataFrame({
    'task_id': np.arange(1, num_tasks + 1),
    'task_type': np.random.choice(task_types, num_tasks),
    'complexity': np.random.randint(1, 6, num_tasks),  # 1=low, 5=high
    'assigned_to': np.random.choice(assigned_options, num_tasks),
    'duration_minutes': np.random.randint(5, 61, num_tasks),  # 5–60 mins
    'resolved': np.random.choice(['Yes', 'No'], num_tasks, p=[0.9, 0.1]),
    'user_feedback': np.random.randint(1, 6, num_tasks),  # 1–5 rating
    'previous_attempts': np.random.randint(0, 4, num_tasks),
    'urgency': np.random.choice(urgency_levels, num_tasks)
})

# -------------------------------
# Optional: Derived Columns
# -------------------------------
# Automation potential (simplified rule)
data['automation_possible'] = np.where(
    (data['complexity'] <= 2) & (data['duration_minutes'] <= 20),
    'Yes',
    'No'
)

# Efficiency index (user feedback / duration)
data['efficiency_index'] = round(data['user_feedback'] / data['duration_minutes'], 3)

# -------------------------------
# Save Dataset to CSV
# -------------------------------
data.to_csv('simulated_workflow_data.csv', index=False)
print("✅ Simulated dataset generated successfully! Saved as 'simulated_workflow_data.csv'")
