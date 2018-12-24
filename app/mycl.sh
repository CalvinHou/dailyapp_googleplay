cd /home/min/dailyapp_googleplay/app
date > /tmp/dailyapp_date.log
pwd > /tmp/dailyapp_pwd.log
export PYTHONIOENCODING=utf8
/usr/bin/python2.7 collectapp.py >> /tmp/dailyapp.log 2>&1

