from flask import Flask, render_template, url_for
import os

app = Flask(__name__)
app.debug = True
#app.config.from_object('settings')
#db - SQLAlchemy(app)

#Migrations
#migrate = Migrate(app, db)

#Blueprints
#from yokine-archery.folder.views import blueprint_name
#app.register_blueprint(blueprint_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')
    
@app.route('/media')
def media():
    return render_template('media.html')
    
@app.route('/location')
def location():
    return render_template('location.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/submit', methods=['POST'])
def submit():
    if(request.method == 'POST'):
        return render_template()
    
if __name__ == "__main__":
    port = int(os.getenv('PORT','8080'))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
