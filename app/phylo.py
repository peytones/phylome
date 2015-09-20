from flask import Flask, request, render_template
from biotree import bio_tree
app = Flask(__name__)

@app.route('/')
def enter_species():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def get_species():
    animals = request.form['text']
    animals = animals.split(',')
    return render_template('tree.html', tree= bio_tree(animals))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
