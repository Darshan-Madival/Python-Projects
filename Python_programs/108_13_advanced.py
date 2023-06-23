from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''Hello World! <!DOCTYPE html>
    <html>

    <head>
    <title>Our Company</title>
    </head>


    <body>

    <h1>Welcome to Our Company</h1>
    <h2>Web Site Main Ingredients:</h2>

    <p>Pages (HTML)</p>
    <p>Style Sheets (CSS)</p>
    <p>Computer Code (JavaScript)</p>
    <p>Live Data (Files and Databases)</p>

    </body>
    </html>'''


if __name__ == '__main__':
    app.run()
