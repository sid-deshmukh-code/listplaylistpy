from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        return render_template('result.html', name=url)
    return render_template('index.html')



@app.route('/ff', methods=["GET", "POST"])
def ff():
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
