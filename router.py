from flask import Flask, render_template, request, session


import sys

sys.path.append(".")

app = Flask(__name__)
app.secret_key = 'My Keys'
RS_URL = 'https://us-4.rightscale.com/'


@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

