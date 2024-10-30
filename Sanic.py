from sanic import Sanic
from sanic.response import json
app = Sanic("MyApp")

@app.route("/hello") #decorator- maps the url hello to the test function
async def test(request): #async route handler
    return json({"message": "Hello, Kamiri. How are you?"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)