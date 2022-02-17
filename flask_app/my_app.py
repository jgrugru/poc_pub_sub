from flask import Flask
from redis import Redis
app = Flask(__name__)
r = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    r.incr("hits")
    return 'Hello, World!' + r.get("hits").decode("utf-8") 


if __name__ == "__main__":
    app.run(debug=True)