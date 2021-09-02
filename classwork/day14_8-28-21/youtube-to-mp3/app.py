from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def converter():
    youtube_link = ""
    if request.method == "POST" and "youtube_link" in request.form:

        # Declare all variables.
        youtube_link = str(request.form.get("youtube_link"))

        print(youtube_link)

    return render_template("index.html", youtube_link=youtube_link)


if __name__ == "__main__":
    # Use 'debug=True' to avoid resarting vs code
    # everytime there is an update in the code.
    app.run(debug=True)