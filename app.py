from flask import Flask, render_template, request  
from pytube import Playlist



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # getting url from HTML page
        url = request.form.get('url')      

        # getting playlist URLs
        p = Playlist(url)
                      
        url_list = []                  # empty list

        for u_id in p.video_urls:
            
            print(u_id)
            index = u_id.index("=")
            vid_id = u_id[index+1:]   #video is stored in vid_id
            url_list.append(vid_id)
        
        # print(url_list)
        return render_template('result.html', name=url_list)   # 
    return render_template('index.html')



@app.route('/ff', methods=["GET", "POST"])
def ff():
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
