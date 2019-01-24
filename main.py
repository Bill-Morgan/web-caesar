from flask import Flask, request
from caesar import rotate_string

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                .errmsg {{
                    color: red;
                    font-weight: bold;
                    margin: 10px auto;
                }}
            </style>
        </head> 
        <body>
            <form method="POST">
                <label>Rotate By:
                    <input type="text" name="rot">
                </label>
                <textarea type="text" name="text">{txtarea}</textarea>
                <input type="submit" text="Submit Query">
            </form>
        </body>
    </html>
"""

def encrypt(text, rot):
    return (rotate_string(text, rot))


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return form.format(errmsg='',txtarea='')

@app.route("/", methods=['POST'])
def process():
    text = request.form['text']
    rot = int(request.form['rot'])
    retvalue = encrypt(text, rot)
    return form.format(errmsg='',txtarea=retvalue)

app.run()