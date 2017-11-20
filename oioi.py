from flask import Flask
from time import sleep
import urllib3
import sys
app = Flask(__name__)
num=1

def reciveMail_sendtoNifty():
	while num:
		sleep(30)
		http = urllib3.PoolManager()
		r = http.request('GET', 'https://evening-badlands-62408.herokuapp.com/')
		num=num-1

#@app.route("/")
#def index():
    #return "Hello World!"

@app.route("/")
def send():
        sleep(1)
        reciveMail_sendtoNifty()
        return "url1"
    # reciveMail_sendtoNifty()


#@app.route("/stop")
#def stop():
    #stop_flag = False
    
    #return stop_flag

if __name__ == "__main__":
    app.run()