# Python Reminder

## Description
This program sets reminders at a specified time duration in seconds. You can customize the message and title of the reminder. Make sure the file has a ".pyw" extension to avoid a command prompt window. Use Python to open the file. It will repeat by creating a new file and adding the set time duration you gave it.

## Installing
```
git clone https://github.com/J3554R/Python-reminder.git
```
Next, ```pip install -r requirements.txt``` to get the necessary dependencies to run this reminder.

## Icon
To add an icon:
```
t.icon_path = "path/to/icon.ico"
```
Then include it in the notification variable below the last if statement:
```
notis = t.show_toast(title, reminder, duration=None, icon_path=t.icon_path)
```

## Startup folder
Create a shortcut for the ".pyw" file and place it in the startup folder for automatic execution on computer startup.
<br>The startup folder is located at:
```
C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

## Convert to seconds
You can use <a href="https://unitconverter.io/minutes/seconds/1">this</a> website to convert days, minutes and hours to seconds, then replace the variable/integer in the last if statement with your number. For example, in the first label select 1. In the second label select "hours". In the third label select "seconds", then hit the convert button.
