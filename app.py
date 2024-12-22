from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    word = ""
    result = ""
    reverse=""
    if request.method == "POST":
        word = request.form.get("inputP", "")
        reverse= word[::-1]
        if word == reverse:
            result = f"Yes, the word '{word}' is a palindrome."
        else:
            result = f"Oops, the word '{word}' is not a palindrome, try again."
    return render_template("index.html",word=word, result=result,reverse=reverse)

if __name__ == "__main__":
    app.run(debug=True)
