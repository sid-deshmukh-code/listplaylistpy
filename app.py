from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        flag = "="
        
        index = url.index(flag)
        a = url[index+1:]
        print("Character found at index", index)
        print(a)
    
        return render_template('result.html', name=a)
    return render_template('index.html')



@app.route('/ff', methods=["GET", "POST"])
def ff():
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
