cd /Users/houhuihua/source/python/dailyapp_googleplay/app
date > /tmp/dailyapp_date.log
pwd > /tmp/dailyapp_pwd.log
export PYTHONIOENCODING=utf8
/usr/local/bin/python2.7 collectapp.py >> /tmp/dailyapp.log 2>&1
#/usr/local/bin/python2.7 collectapp.py 
#/usr/local/bin/python2.7 testcollectapp.py >> /tmp/dailyapp.log 2>&1
##python testcollectapp.py >> /tmp/dailyapp.log 2>&1

