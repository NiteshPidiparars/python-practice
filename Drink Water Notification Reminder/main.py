'''
This application will track time and show you notification after a brief period of time to remind you to drink water. 
We are going to use plyer  module to show the notification and the time module to run the module after a fixed period of time. 
You can install plyer by typing “pip install plyer” on the terminal/cmd.  For better understanding watch the complete video. 
'''
import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon="C:\\Users\\hp\\Desktop\\MY\\Python Tutorials\\PracticePrograms\\Drink Water Notification Reminder\\icon.ico",
            timeout=12
        )
        # time.sleep(6)
        time.sleep(60*60)
