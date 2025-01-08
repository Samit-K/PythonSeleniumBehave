from datetime import datetime


def get_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%H_%M_%S_%m_%Y")
    return "Tester.testing" + str(time_stamp) + "@test.com"
