from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    reuturn "Hello World from node 2!\n"


app.run( 
    host="0.0.0.0",
    port=5002
)
