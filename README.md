# allocateResourcesScript
This Python script automates the process of allocating team members to project tasks based on predefined rules and constraints.
Features

Loads project tasks and team member data from CSV files
Defines resource allocation rules, such as maximum tasks per team member and skill requirements
Prioritizes tasks based on their priority
Assigns tasks to the available team member with the lowest current task count
Identifies and tracks unassigned tasks due to skill gaps
Generates CSV files for the resource allocation and unassigned tasks

Usage

Ensure you have Python and the following libraries installed:

pandas


Update the CSV files project_tasks.csv and team_members.csv with your project data.

Run the script:
python scriptName.py
