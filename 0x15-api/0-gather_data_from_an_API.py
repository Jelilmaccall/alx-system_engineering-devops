#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos'
    users_url = f'{base_url}/users/{employee_id}'

    try:
        # Fetch employee name
        response = requests.get(users_url)
        response.raise_for_status()
        employee = response.json()
        employee_name = employee['name']

        # Fetch employee todos
        response = requests.get(todos_url, params={'userId': employee_id})
        response.raise_for_status()
        todos = response.json()

        # Filter completed todos
        completed_todos = [todo for todo in todos if todo['completed']]
        completed_task_count = len(completed_todos)
        total_task_count = len(todos)

        # Display progress
        print(f'Employee {employee_name} is done with tasks({completed_task_count}/{total_task_count}):')
        for todo in completed_todos:
            print(f'\t{todo["title"]}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)

