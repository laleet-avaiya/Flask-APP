from flask import Flask, render_template, json,  request, session,redirect, url_for, escape



app = Flask(__name__)


@app.route("/")
def main():
        return render_template('index.html')


@app.route('/aboutus')
def aboutus():
        return render_template('aboutus.html')

# Main
if __name__ == "__main__":
    app.run()
