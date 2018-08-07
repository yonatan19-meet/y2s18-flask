from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    # players = ["Asi Abu", "Ben Boy", "Cinnamon Comfortable", "Dori Debest"]
    return render_template("index.html")
    # , players=players, like_same_sport=True)

if __name__ == '__main__':
    app.run(debug = True)


