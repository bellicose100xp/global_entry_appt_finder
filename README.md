# Global Entry Appointment Finder
Finds earliest Global Entry appointment and notifies user via GMail and Slack.

## Configurations Needed

### Update `LOCATION_ID` in `app.py`
Set location ID to the Global Entry service center you want to track. You can find this by checking the requests made in the Network tab of the Chrome or Firefox Developer Tools when you click on the service center name in the Global Entry appointment scheduler.

Ex. this sets the location ID to Los Angeles service center.

```python
LOCATION_ID = 5180
```

## Create `cred_store_local.py` with the credentials needed to send Email and Slack notifications

```python
EMAIL_PASS = "gmail_password or gmail_app_password"
EMAIL_USERNAME = "gmail username"
EMAIL_SENDER = "gmail username"
EMAIL_RECEIVER = "email where you want to be notified"
SLACK_WEBHOOK = "slack webhook of the channel where you want to be notified"
```

## How to Run the App

```
git clone https://github.com/bellicose100xp/global_entry_appt_finder.git
cd global_entry_appt_finder
pip -m venv .venv

# mac-linux
./.venv/Scripts/activate

# windows - cmd
.\.venv\Scripts\activate.bat

# windows - powershell
.\.venv\Scripts\activate.ps1

pip install -r requirements.txt

python app.py
```