from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/greet', methods=['GET'])
def greet():
    """
    A simple API to greet users.
    ---
    parameters:
        - name: name
        in: query
        type: string
        required: false
        description: The name of the person to greet.
    responses:
        200:
        description: A greeting message
    """
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(debug=True)