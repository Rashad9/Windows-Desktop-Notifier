from plyer import notification
import time

# Absolute path to the icon file (ensure the path is correct)
icon_path = r"C:\Users\rasha\Downloads\heart.ico"

# Notification content
title = 'Reminder !'
message = 'This is a reminder to go to the gym at 1pm today!'

try:
    # Show notification
    notification.notify(
        title=title,
        message=message,
        app_icon=icon_path,  # Use None if no icon is needed
        timeout=15,
        toast=False
    )

    # Wait for 1 hour (or handle any interruption gracefully)
    time.sleep(60*60)
except Exception as e:
    print(f"An error occurred: {e}")
