from flask import Flask, jsonify, render_template, request
from modules.producer import produce_data
from modules.mongolist import products_list, is_available

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_input = data.get('user_input')

    if is_available(user_input):
        bought_item = f"You bought: {user_input}"
        produce_data(user_input)
    
    else:
        bought_item = f"{user_input} Not Found"

    return jsonify({"message": f"{bought_item}"})


@app.route('/api/data')
def data():
    items = products_list()
    message = {"message": f"{items}"}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
