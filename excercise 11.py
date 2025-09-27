
# import time

# def reminder():
#     print("Drink Water Reminder...\nStay Hydreted...)")
#     time.sleep(40)
#     print("Drink Water Reminder...\nStay Hydreted...)")

# reminder()




# import time

# def water_reminder():
#     while True:
#         print("💧 Time to drink water! Stay hydrated. 💧")
#         # Sleep for 2 hours (7200 seconds)
#         time.sleep(2 * 60 * 60)

# water_reminder()




import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title="💧 Water Reminder",
            message="💧 Time to drink water! Stay hydrated. 💧 \nIt's time to drink a glass of water!",
            timeout=10  # notification stays for 10 seconds
        )
        # Wait for 2 hours
        time.sleep(1 * 60 * 60)

water_reminder()
