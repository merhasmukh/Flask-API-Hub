from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)  

# open this to view swagger UI: http://127.0.0.1:5000/apidocs/

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    A simple GET endpoint.
    ---
    responses:
      200:
        description: Returns a greeting message
        examples:
          message: "Hello, World!"
    """
    return jsonify({"message": "Hello, World!"})

@app.route('/add', methods=['POST'])
def add_numbers():
    """
    Add two numbers.
    ---
    parameters:
      - name: num1
        in: formData
        type: number
        required: true
        description: The first number
      - name: num2
        in: formData
        type: number
        required: true
        description: The second number
    responses:
      200:
        description: The sum of the two numbers
        examples:
          result: 7
    """
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    return jsonify({"result": num1 + num2})

if __name__ == "__main__":
    app.run(debug=True)
