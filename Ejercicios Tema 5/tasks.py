from invoke import task, run

@task 
def start(context):
	run("pm2 start app1.py --name DailyReport --interpreter python3 -i 8")
@task 
def stop(context):
	run("pm2 stop DailyReport")

