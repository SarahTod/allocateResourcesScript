# allocateResourcesScript

This Python script automates the process of allocating team members to project tasks based on predefined rules and constraints.

## Features

- Loads project tasks and team member data from CSV files
- Defines resource allocation rules, such as maximum tasks per team member and skill requirements
- Prioritizes tasks based on their priority
- Assigns tasks to the available team member with the lowest current task count
- Identifies and tracks unassigned tasks due to skill gaps
- Generates CSV files for the resource allocation and unassigned tasks

## Usage

1. Ensure you have Python and the following libraries installed:
   - pandas

2. Update the CSV files `project_tasks.csv` and `team_members.csv` with your project data.

### PROJECT TASKS CSV FILE

- **Header row:** Include column headers that clearly identify the information you want to store for each team member. Common headers might include:
  - `team_member_id` (unique identifier for each member)
  - `name`
  - `email`
  - `role`
  - `department`
  - `availability` (e.g., full-time, part-time, contract)
- **Data rows:** Each row should represent a single team member, with values for each column corresponding to that member's information.
- **Data types:** Ensure that data types are consistent within each column (e.g., all `team_member_id` values should be numbers).

### TEAM MEMBERS CSV FILE

- **Header row:** Include column headers that clearly identify the information you want to store for each project task. Common headers might include:
  - `task_id` (unique identifier for each task)
  - `project_id` (if applicable)
  - `task_name`
  - `description`
  - `due_date`
  - `priority`
  - `status` (e.g., not started, in progress, completed)
  - `assigned_to` (referencing the `team_member_id` from the team members file)
- **Data rows:** Each row should represent a single project task, with values for each column corresponding to that task's information.
- **Data types:** Ensure that data types are consistent within each column (e.g., all `due_date` values should be dates).

3. Run the script:
   ```
   python scriptName.py
   ```

Would you like me to explain or break down any part of this reformatted content?
