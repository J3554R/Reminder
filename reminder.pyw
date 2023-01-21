"""
win10toast==0.9 and Python 3.8.5 used.

Set a new variable with the time you want to be reminded, and replace it with the integer used in the last if statement (line 60).

Save this file as a ".pyw" file, create a shortcut of it, and place the shortcut in your startups folder so that you don't have to manually start it everytime you start your computer. 

When you run this reminder and get the "How do you want to open this file?" window, select Python and check the "Always use this app to open .pyw files". Now click OK.

To make this reminder stop, hit the CTRL+LSHIFT+ESC keys, scroll down in Task Manager, find Python, right-click it, and terminate it.

Or type "taskkill /f /im python.exe" in your command prompt to kill all python processes.  "taskkill /f /im pythonw.exe" for pythonw processes.
"""
# Path to startups folder: C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

from datetime import datetime as dt
import os, sys
from win10toast import ToastNotifier as tn

t = tn()

# Get the current time
current_time = dt.now()

title = "<TITLE OF REMINDER>" # Set the title/subject of your reminder here.
reminder = "<MESSAGE OF REMINDER>" # Set your reminder message here

# Use these variables to set the time of the reminder in the last if statement. It is currently set to 10, which means you'll get your reminder every 10 seconds while this program is open.
one_second = 1
one_minute = 60
one_hour = 60 * 60
one_day = one_hour * 24
two_days = one_day * 2

while True:
    current_time = dt.now()
    try:
        os.mkdir("date")
    except:
        pass
    dtls = os.listdir("date")
    if "date.txt" not in dtls:
        # If date.txt does not exist, create it and write the current time to it
        date = open("date/date.txt", "w")
        date.write(str(current_time))
        date.flush()
    else:
        # If date.txt exists, read the time from it
        date_read = open("date/date.txt", "r")
        date_read = date_read.read()

        # Convert the time in the file to a datetime object
        time_in_file = dt.strptime(date_read, '%Y-%m-%d %H:%M:%S.%f')


        # Calculate the difference between the current time and the time in the file
        time_difference = current_time - time_in_file

        # Check if the difference is greater
        if time_difference.total_seconds() > 10: # If it is, execute the reminder
            try:
                notis = t.show_toast(title, reminder, duration=None) # If you want to add an icon, add this variable with the path of your icon: t.icon_path = "path/to/icon.ico". Then include it in the notification: notis = t.show_toast(title, reminder, duration=None, icon_path=t.icon_path)
            except TypeError as e:
                print("Notification sent")
            date = open("date/date.txt", "w") # File is created again so that the process loops
            date.write(str(current_time))
            date.flush()
