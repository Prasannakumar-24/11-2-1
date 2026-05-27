from flask import Flask, request
import random
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# ---------------------------------------------------
# MACHINE LEARNING MODEL
# ---------------------------------------------------

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

y = np.array([
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
])

model = LinearRegression()

model.fit(X, y)

# ---------------------------------------------------
# NUMBER GUESSING GAME
# ---------------------------------------------------

secret_number = random.randint(1, 100)

# ---------------------------------------------------
# HTML PAGE
# ---------------------------------------------------

HTML_PAGE = """

<!DOCTYPE html>

<html>

<head>

<title>Python Basics + AI</title>

<style>

body{
    background:#020617;
    color:white;
    font-family:Arial;
    text-align:center;
    padding:30px;
}

.container{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:20px;
}

.card{
    background:#0f172a;
    padding:25px;
    border-radius:15px;
    width:350px;
    box-shadow:0 0 15px rgba(0,0,0,0.4);
}

h1{
    color:#38bdf8;
    margin-bottom:30px;
}

h2{
    color:#22c55e;
}

input,select{
    width:90%;
    padding:10px;
    margin:10px 0;
    border:none;
    border-radius:8px;
    font-size:16px;
}

button{
    background:#38bdf8;
    color:white;
    border:none;
    padding:12px 20px;
    border-radius:8px;
    cursor:pointer;
    font-size:16px;
    font-weight:bold;
}

button:hover{
    background:#0ea5e9;
}

.result{
    margin-top:15px;
    font-size:20px;
    color:#facc15;
    font-weight:bold;
}

.info{
    margin-top:40px;
    background:#111827;
    padding:20px;
    border-radius:15px;
}

</style>

</head>

<body>

<h1>PYTHON PROGRAMMING BASICS + AI</h1>

<div class="container">

<!-- CALCULATOR -->

<div class="card">

<h2>Calculator</h2>

<form method="POST">

<input type="number" step="any" name="num1" placeholder="Enter Number 1" required>

<input type="number" step="any" name="num2" placeholder="Enter Number 2" required>

<select name="operation">

<option>Addition</option>
<option>Subtraction</option>
<option>Multiplication</option>
<option>Division</option>

</select>

<button type="submit" name="action" value="calculate">

CALCULATE

</button>

</form>

<div class="result">

{calc_result}

</div>

</div>

<!-- NUMBER GUESSING GAME -->

<div class="card">

<h2>Number Guessing Game</h2>

<form method="POST">

<input type="number" name="guess" placeholder="Guess Number 1-100" required>

<button type="submit" name="action" value="guess">

CHECK GUESS

</button>

</form>

<div class="result">

{game_result}

</div>

</div>

<!-- AI PREDICTION -->

<div class="card">

<h2>Machine Learning AI</h2>

<form method="POST">

<input type="number" name="value" placeholder="Enter Number" required>

<button type="submit" name="action" value="predict">

AI PREDICT

</button>

</form>

<div class="result">

{ai_result}

</div>

</div>

</div>

<div class="info">

<h2>PROJECT FEATURES</h2>

<p>

✔ Python Functions<br><br>

✔ Arithmetic Operations<br><br>

✔ Number Guessing Game<br><br>

✔ Machine Learning Prediction<br><br>

✔ Flask Web Application<br><br>

✔ Render Cloud Deployment

</p>

</div>

</body>

</html>

"""

# ---------------------------------------------------
# MAIN ROUTE
# ---------------------------------------------------

@app.route("/", methods=["GET", "POST"])

def home():

    global secret_number

    calc_result = ""
    game_result = ""
    ai_result = ""

    if request.method == "POST":

        action = request.form.get("action")

        # ---------------------------------------------------
        # CALCULATOR
        # ---------------------------------------------------

        if action == "calculate":

            try:

                num1 = float(request.form.get("num1"))
                num2 = float(request.form.get("num2"))

                operation = request.form.get("operation")

                if operation == "Addition":
                    result = num1 + num2

                elif operation == "Subtraction":
                    result = num1 - num2

                elif operation == "Multiplication":
                    result = num1 * num2

                elif operation == "Division":

                    if num2 == 0:
                        result = "Cannot divide by zero"

                    else:
                        result = num1 / num2

                calc_result = f"Result: {result}"

            except:

                calc_result = "Invalid Input"

        # ---------------------------------------------------
        # NUMBER GUESSING GAME
        # ---------------------------------------------------

        elif action == "guess":

            try:

                guess = int(request.form.get("guess"))

                if guess < secret_number:

                    game_result = "Too Low!"

                elif guess > secret_number:

                    game_result = "Too High!"

                else:

                    game_result = "Correct Guess!"

                    secret_number = random.randint(1, 100)

            except:

                game_result = "Invalid Input"

        # ---------------------------------------------------
        # AI PREDICTION
        # ---------------------------------------------------

        elif action == "predict":

            try:

                value = int(request.form.get("value"))

                prediction = model.predict([[value]])

                ai_result = f"AI Prediction: {prediction[0]:.2f}"

            except:

                ai_result = "Invalid Input"

    return HTML_PAGE.format(
        calc_result=calc_result,
        game_result=game_result,
        ai_result=ai_result
    )

# ---------------------------------------------------
# RUN APP
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)