from flask import Flask, jsonify, render_template, request
from modules.producer import produce_data
from modules.mongolist import products_list

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_input = data.get('user_input')
    produce_data(user_input)
    return jsonify({"message": f"You bought: {user_input}"})


@app.route('/api/data')
def data():
    items = products_list()
    message = {"message": f"{items}"}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
