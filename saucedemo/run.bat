pytest -s -v -m "login" --log-file=./Logs/automation.log --html=./Reports/report.html --self-contained-html --capture sys -rP  --disable-warnings testCases/test_login.py --browser chrome
