from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        # Get the number from the form
        number = int(request.form['number'])
    else:
        # Support for URL query like /convert?number=25
        number = request.args.get('number', default=0, type=int)
    
    # Convert to binary
    binary = bin(number)[2:]

    # Return result as JSON
    return jsonify({"decimal": number, "binary": binary})

if __name__ == '__main__':
    app.run(debug=True)
