# Scheduling are used to schedule the job according to the particular time .
# It requires a loop , to continuouly chack the time for print .
# schedule.run_pending() is common thing in the scheduling .
import schedule
import time
"""def job():
    print("Job is running")
while True:
    job()
    time.sleep(5)"""
def job():
    print("ETL is running")

schedule.every().day.at("13:39").do(job)
schedule.every(5).seconds.do(job)
schedule.every(5).minutes.do(job)
schedule.every().monday.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)