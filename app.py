from flask import Flask, render_template
import os

app = Flask(__name__)

video_projects = [

    {
        'title': 'Music Video',
        'description': 'Lyric video for independent artist',
        'thumbnail': 'music-thumb.jpg',
        'skills': ['Visual Effects', 'Transitions', 'Audio Sync'],
        'link': 'https://drive.google.com/drive/folders/1jJeOtVRf-qFiJcFuEY6gRUs_tdcBVufc?usp=drive_link'
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video-editing')
def video_editing():
    return render_template('video-editing.html', projects=video_projects)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)