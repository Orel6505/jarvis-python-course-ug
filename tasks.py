import requests
import os
import contextlib
from typing import List, Dict, Optional
from utils import talk   # Import the #talk function
import pywhatkit
import datetime
import threading

class tasks:
    def __init__(self, access_token: str):
        """
        Initialize the Microsoft To Do client with an access token.
        """
        self.access_token = access_token
        self.base_url = "https://graph.microsoft.com/v1.0"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    
    def get_all_tasks(self, todo_list_id: str) -> List[Dict]:
        """
        Fetch all tasks from a specific To Do list.
        """
        url = f"{self.base_url}/me/todo/lists/{todo_list_id}/tasks"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data.get('value', [])
        except requests.exceptions.RequestException as e:
            #talk(f"Error fetching tasks: {e}")
            return []
    
    def add_task(self, todo_list_id: str, title: str, body: str = "", due_date: str = None, importance: str = None) -> Dict:
        """
        Add a new task to a specific To Do list.
        """
        url = f"{self.base_url}/me/todo/lists/{todo_list_id}/tasks"
        task_data = {"title": title}
        if body:
            task_data["body"] = {"content": body, "contentType": "text"}
        if due_date:
            task_data["dueDateTime"] = {"dateTime": due_date, "timeZone": "UTC"}
        if importance:
            task_data["importance"] = importance
        try:
            response = requests.post(url, headers=self.headers, json=task_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            #talk(f"Error adding task: {e}")
            return {}
    
    def complete_task(self, todo_list_id: str, task_id: str) -> bool:
        """
        Mark a task as completed.
        """
        url = f"{self.base_url}/me/todo/lists/{todo_list_id}/tasks/{task_id}"
        update_data = {"status": "completed"}
        try:
            response = requests.patch(url, headers=self.headers, json=update_data)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            #talk(f"Error completing task: {e}")
            return False
    
    def update_task(self, todo_list_id: str, task_id: str, title: str = None, 
                   body: str = None, due_date: str = None, importance: str = None) -> Dict:
        """
        Update an existing task.
        """
        url = f"{self.base_url}/me/todo/lists/{todo_list_id}/tasks/{task_id}"
        update_data = {}
        if title:
            update_data["title"] = title
        if body is not None:
            update_data["body"] = {"content": body, "contentType": "text"}
        if due_date:
            update_data["dueDateTime"] = {"dateTime": due_date, "timeZone": "UTC"}
        if importance:
            update_data["importance"] = importance
        try:
            response = requests.patch(url, headers=self.headers, json=update_data)
            response.raise_for_status()
            # Return the JSON object but do not print it.
            return response.json()
        except requests.exceptions.RequestException as e:
            #talk(f"Error updating task: {e}")
            return {}
    
    def print_tasks(self, tasks: List[Dict], filter_status: Optional[str] = None, return_filtered: bool = False) -> Optional[List[Dict]]:
        """
        Helper function to speak tasks in a readable format with consecutive numbering,
        with uncompleted tasks shown before completed ones.
        """
        if not tasks:
            print("No tasks found.")
            return [] if return_filtered else None

        # Filter tasks if needed.
        if filter_status:
            filtered_tasks = []
            for task in tasks:
                if (filter_status == 'completed' and task.get('status') == 'completed') or \
                   (filter_status == 'uncompleted' and task.get('status') != 'completed'):
                    filtered_tasks.append(task)
            display_tasks = filtered_tasks
        else:
            display_tasks = tasks

        # Sort tasks: uncompleted tasks first.
        sorted_tasks = sorted(display_tasks, key=lambda task: task.get('status') == 'completed')

        # Speak tasks with consecutive numbering.
        for idx, task in enumerate(sorted_tasks, start=1):
            status = "✓" if task.get('status') == 'completed' else "○"
            title = task.get('title', 'No title')
            print(f"{idx}. {status} {title}")

        if return_filtered:
            return sorted_tasks
        
    def send_task_reminder(self, task: Dict, minutes_from_now: int, phone_number: str) -> None:
        """
        Uses pywhatkit to send a WhatsApp reminder after x minutes for the specified task.
        The reminder message follows the same printed format.
        The WhatsApp message is sent in a separate (daemon) thread so that it doesn't interfere
        with the CMD. If the computed time exceeds today's remaining time, it adjusts the target to 23:59 today.
        """
        wait_time = 10  # seconds for WhatsApp Web to load
        # Convert minutes to seconds.
        seconds_from_now = minutes_from_now * 60
        now = datetime.datetime.now()
        proposed_target_time = now + datetime.timedelta(seconds=seconds_from_now)
        
        # Ensure target time is at least (wait_time + 5) seconds in the future.
        min_target_time = now + datetime.timedelta(seconds=wait_time + 5)
        if proposed_target_time < min_target_time:
            proposed_target_time = min_target_time
            talk(f"Delay too short. Adjusting target time to {proposed_target_time.strftime('%H:%M')}.")
        
        # If the computed target time falls on tomorrow, adjust to today at 23:59.
        if proposed_target_time.date() != now.date():
            adjusted_target = datetime.datetime(now.year, now.month, now.day, 23, 59)
            # Only adjust if 23:59 is still in the future; otherwise use minimum delay.
            if adjusted_target > now:
                proposed_target_time = adjusted_target
                talk("Delay exceeds today's remaining time. Adjusting target time to 23:59 today.")
            else:
                proposed_target_time = min_target_time
                talk("Not enough time left today; using the minimal allowed delay.")
        
        target_hour = proposed_target_time.hour
        target_minute = proposed_target_time.minute

        title = task.get('title', 'No title')
        status = "✓" if task.get('status') == 'completed' else "○"
        message = f"Reminder: {status} {title} - please complete this task."
        
        def send_msg():
            # Suppress output from pywhatkit by redirecting stdout
            with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
                pywhatkit.sendwhatmsg(phone_number, message, target_hour, target_minute, wait_time=wait_time)
        
        try:
            talk(f"Reminder set for task '{title}' at {target_hour}:{target_minute:02d} on WhatsApp.")
            reminder_thread = threading.Thread(target=send_msg)
            reminder_thread.daemon = True  # daemon thread so it doesn't block CMD
            reminder_thread.start()
        except Exception as e:
            talk(f"Failed to set reminder: {e}")