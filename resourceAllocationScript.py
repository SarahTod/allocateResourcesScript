import pandas as pd

# Load the project tasks and team member data from CSV files
project_tasks = pd.read_csv('project_tasks.csv')
team_members = pd.read_csv('team_members.csv')

# Define the resource allocation rules and constraints
max_tasks_per_team_member = 3
skill_requirements = {
    'task1': ['skill1', 'skill2'],
    'task2': ['skill2', 'skill3'],
    # Add more task-skill mappings as needed
}

def allocate_resources():
    """
    Allocate team members to project tasks based on the defined rules and constraints.

    Returns:
        resource_allocation (dict): A dictionary mapping each task to the assigned team member (or 'Unassigned' if no suitable team member is found).
        unassigned_tasks (list): A list of tuples containing the name of each unassigned task and the reason (e.g., 'Skill gap').
    """
    # Initialize dictionaries and lists to store the resource allocation and unassigned tasks
    resource_allocation = {}
    unassigned_tasks = []

    # Sort the project tasks by priority
    project_tasks.sort_values('priority', inplace=True)

    # Iterate through the project tasks
    for _, task in project_tasks.iterrows():
        # Find available team members who meet the skill requirements and have not reached the maximum number of tasks
        available_team_members = team_members[(team_members['skills'].isin(skill_requirements[task['name']])) & (team_members['tasks_assigned'] < max_tasks_per_team_member)]

        # If there are available team members, assign the task to the one with the lowest current task count
        if not available_team_members.empty:
            available_team_members.sort_values('tasks_assigned', inplace=True)
            assigned_team_member = available_team_members.iloc[0]
            resource_allocation[task['name']] = assigned_team_member['name']
            team_members.at[assigned_team_member.name, 'tasks_assigned'] += 1
        # If no suitable team member is found, mark the task as 'Unassigned' and add it to the unassigned tasks list
        else:
            resource_allocation[task['name']] = 'Unassigned'
            unassigned_tasks.append((task['name'], 'Skill gap'))

    return resource_allocation, unassigned_tasks

# Call the resource allocation function
resource_allocation, unassigned_tasks = allocate_resources()

# Save the resource allocation to a CSV file
pd.DataFrame.from_dict(resource_allocation, orient='index', columns=['Assigned Team Member']).to_csv('resource_allocation.csv')

# Save the unassigned tasks to a separate CSV file
pd.DataFrame(unassigned_tasks, columns=['Task Name', 'Reason']).to_csv('unassigned_tasks.csv')