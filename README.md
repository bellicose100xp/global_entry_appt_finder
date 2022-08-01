# Global Entry Appointment Finder
Finds earliest Global Entry appointment for provided service center and optionally notifies user via GMail and Slack.

## Configurations Needed

### Update `configure_app.py`
Set whether you wnat to receive email and slack notificaitons. Allowed values are `yes` and `no`.
```
EMAIL_NOTIFICATION = "yes"
SLACK_NOTIFICATION = "yes"
```

Configure for which available appointments you want to be notified. You'll only be notified if the appointment found is earlier than the date you set below.

```
YEAR = 2023
MONTH = 8
DAY = 1
```

Set location ID to the Global Entry service center you want to track. You can find this by checking the API requests made in the Network tab of the Chrome or Firefox Developer Tools when you click on the service center name in the Global Entry appointment scheduler.

Ex. this sets the location ID to Los Angeles service center.

```python
LOCATION_ID = 5180
```

### Create `cred_store_local.py` with the credentials needed to send Email and Slack notifications (Required, if those options are configured in `configure_app.py`)
For gmail, you won't be able to use your regular credentials. You must have 2-Step Verificaton set up for your gmail account and you must create an [app password](https://support.google.com/accounts/answer/185833?hl=en) to use with the app (for app select 'other' when creating app password).

```python
EMAIL_PASS = "gmail_app_password"
EMAIL_USERNAME = "gmail username"
EMAIL_SENDER = "gmail username"
EMAIL_RECEIVER = "email where you want to be notified"
SLACK_WEBHOOK = "slack webhook of the channel where you want to be notified"
```

## Initial app setup and run

```
git clone https://github.com/bellicose100xp/global_entry_appt_finder.git
cd global_entry_appt_finder
python -m venv .venv

# mac-linux
./.venv/Scripts/activate

# windows - cmd
.\.venv\Scripts\activate.bat

# windows - powershell
.\.venv\Scripts\activate.ps1

pip install -r requirements.txt
python app.py
```

## How to Stop the App
Press `ctrl +c` on the keyboard

## How to re-run the app after intitial setup
```
cd global_entry_appt_finder

# mac-linux
./.venv/Scripts/activate

# windows - cmd
.\.venv\Scripts\activate.bat

# windows - powershell
.\.venv\Scripts\activate.ps1

python app.py
```