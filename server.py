#from flask import Flask

#app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def root():
#    return "flask application version 2.0"

#app.run(host="0.0.0.0", port=4000)

from flask import Flask, render_template_string

app = Flask(__name__)

# Define an HTML template for better UI
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Flask Application</h1>
        <p>Version 2.0</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def root():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
