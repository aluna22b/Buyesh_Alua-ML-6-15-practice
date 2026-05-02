import time
import schedule

from batch_predict import run_batch_prediction


# Run immediately once
run_batch_prediction()

# Run every 5 minutes
schedule.every(5).minutes.do(run_batch_prediction)

print("Scheduler started.")
print("Batch prediction will run every 5 minutes.")

while True:
    schedule.run_pending()
    time.sleep(1)