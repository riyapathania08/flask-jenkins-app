from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <head>
            <title>Flask CI/CD App</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #000;   /* Black background */
                    color: #fff;              /* White text */
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                }
                h1 {
                    font-size: 24px;
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>🌸 Hello from Flask app deployed via Jenkins + Docker!</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
