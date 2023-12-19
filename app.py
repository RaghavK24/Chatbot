# Flask code
from flask import Flask, render_template, request, jsonify
from chat import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.get_json()
        user_message = data.get('userMessage')  # Use the correct key from your JSON data
        # Return a JSON response
        return jsonify({'response': user_message})

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
