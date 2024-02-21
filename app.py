import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']
    return  f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name']
    return  f"Goodbye {name}!"


# == EXERCISE 1 ==
#Create a new route that responds to A method   POST
# A path /submit
# Body parameters name and message

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return  f"Thank you {name} for your message: {message}!"

# run in the terminal with the following command: curl -X POST -d "name=Leo&message=Hello world" http://localhost:5001/submit
#for my local host is 5001.

# == CHALLENGE ==
# Create a new route that responds to A method   GET
# A path /wave
# Query parameters name
# The route should return a string that says "I am waving at [NAME]" followed by the name in the query parameter.

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return  f"I am waving at {name}!"

# run in the terminal with the following command: curl http://localhost:5001/wave?name=Leo

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

