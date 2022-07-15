from slack import send_slack_message
from email_gmail import send_email
import requests
import time
import datetime
import os
import sys
import logging

import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)  # reset color after each print statement

## Location ID of the Los Angeles Global Entry Service Center
LOCATION_ID = 5180

# create log folder if doesnt exists
# get executable parent folder
if getattr(sys, 'frozen', False):
    # get executable parent folder when run as .exe
    script_dir = os.path.dirname(sys.executable)
else:
    # get executable parent folder when run as .py
    script_dir = os.path.dirname(__file__)

log_folder_path = f"{script_dir}/logs"

if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)

now = datetime.datetime.now()
log_filename = f"logs/{now:%Y-%m-%d}.log"

logging.basicConfig(level=logging.INFO, filename=log_filename, filemode="a", format="%(message)s")

url = "https://ttp.cbp.dhs.gov/schedulerapi/slots"

params = {
    "orderBy": "soonest",
    "limit": "1",
    "locationId": LOCATION_ID
}

current_appt = datetime.date(2022, 8, 1)
appt_emailed = None
next_appt_printed = None
check_interval = 10

while True:
    try:
        r = requests.get(url, params=params)
    except requests.exceptions.RequestException as e:
        logging.exception(e)
        print(e)

    json = r.json()
    # print(json)

    # check for empty list if no appointments are available, wait 10 seconds and skip rest of the code
    if not json:
        print(".", end="")
        time.sleep(check_interval)
        continue

    next_appt_iso8601_datetime = json[0]["startTimestamp"]
    next_available_appt_datetime = datetime.datetime.fromisoformat(next_appt_iso8601_datetime)
    next_available_appt_date = next_available_appt_datetime.date()
    date_diff_delta = next_available_appt_date - current_appt

    now = datetime.datetime.now()

    if next_appt_printed != next_available_appt_datetime:
        appt_avail_message = f"[{now:%b %d, %Y %I:%M:%S %p}] Next Available Appointment: {next_available_appt_datetime:%a %b %d, %Y %I:%M:%S %p}"
        print(f"\n{appt_avail_message}")
        logging.info(appt_avail_message)
        next_appt_printed = next_available_appt_datetime
    else:
        print(".", end="")

    if next_available_appt_date < current_appt and appt_emailed != next_available_appt_date:
        appt_found_message = f"Earlier Appointment Available on {next_available_appt_datetime:%a %b %d, %Y %I:%M:%S %p}"
        message_body = f"{appt_found_message}\nGo to https://ttp.cbp.dhs.gov/"
        print(f"{Back.MAGENTA} {appt_found_message}")
        logging.info(f"***** {appt_found_message} *****")

        send_email(subject=appt_found_message, content=message_body)
        send_slack_message(message_body)
        appt_emailed = next_available_appt_date

    time.sleep(check_interval)
