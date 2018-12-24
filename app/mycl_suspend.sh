cd /home/min/dailyapp_googleplay/app
date > /tmp/dailyapp_date_s.log
pwd > /tmp/dailyapp_pwd_s.log
export PYTHONIOENCODING=utf8
/usr/bin/python2.7 suspend_developer.py >> /tmp/dailyapp.log 2>&1

