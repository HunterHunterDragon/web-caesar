from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")

def index():
    return """
    <form method = 'POST'>
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
            }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            Rotate by: <input type = "text" name = "rot" value = "0">
            <br><br>
            <textarea name = "text"></textarea>
            <br><br>
            <input type="submit" />
        </body>
    </html>
    </form>
    """

@app.route("/", methods=['POST'])

def encrypt():

    answer_string = []
    for answer in request.form.values():
        answer_string.append(answer)
    alpha_rotate = answer_string[0]
    beta_rotate = int(alpha_rotate)
    texta = answer_string[1]
    final_answer_Bob = rotate_string(texta, beta_rotate)
    answer = """
    <form method = 'POST'>
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
            }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            Rotate by: <input type = "text" name = "rot" value= 0>
            <br><br>
            <textarea name = "text">""" + final_answer_Bob + """</textarea>
            <br><br>
            <input type="submit" />
        </body>
    </html>
    </form>
    """
    return answer

app.run()