from flask import Flask
import time
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_value = random.uniform(0, 0.5)
    time.sleep(random_value)
    return str(random_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)