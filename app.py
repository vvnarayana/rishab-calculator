#from flask import render_template, request
#from keep_alive import keep_alive, app
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("calculator.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    number_one = request.form["number_one"]
    number_two = request.form["number_two"]
    operation = request.form["operation"]

    if operation == "add":
        result = float(number_one) + float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "subtract":
        result = float(number_one) - float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "multiply":
        result = float(number_one) * float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "divide":
        if float(number_two) == 0:
            return render_template("calculator.html", result="Error: Cannot divide by zero")
        result = float(number_one) / float(number_two)
        return render_template("calculator.html", result=result)

    else:
        return render_template("calculator.html", result="Error: Invalid operation")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)


if __name__ == "__main__":
    app.run()
