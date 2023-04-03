from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')

def index():
    cpu_perc = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    message = None
    if cpu_perc > 80 or memory_usage > 80:
        message = "High CPU Utilization detected!"
    return render_template("index.html",cpu_perc=cpu_perc,memory_usage=memory_usage,message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)