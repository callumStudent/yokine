from flask import Flask, request, render_template
from flask_admin import Admin
from flask_mail import Mail, Message
from flask.ext.admin.base import MenuLink
from flask.ext.security import SQLAlchemyUserDatastore, Security
#from flask_security.utils import encrypt_password
from sqlalchemy import desc#, exc
import os

app = Flask(__name__)
app.config.from_pyfile('settings.py')
mail = Mail(app)

from database import db
from news.models import NewsPost, Category

#Blueprints
#from yokine-archery.folder.views import blueprint_name
#app.register_blueprint(blueprint_name)

# Security
from security import models
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

# Set the admin/logout to redirect to the login page if not already logged in
#security.login_manager.login_view = 'loginview.index'

# Set up Admin
from admin import IndexView, LoginView#, NewsPostView#, CategoryView

admin = Admin(name='Members/Admin', index_view=IndexView(url='/a'))
admin.add_link(MenuLink(name='Back to site', url='/'))
admin.add_view(LoginView(name='Login',url='/members_login'))
#admin.add_view(NewsPostView(db.session))
#admin.add_view(CategoryView(db.session))
admin.init_app(app)

@app.route('/')
def index():
    #news = NewsPost.query.order_by(desc(NewsPost.date)).limit(5).all()
    return render_template('index.html')#, news=news)

@app.route('/news')
def news():
    #news = NewsPost.query.order_by(desc(NewsPost.date))

    return render_template('news.html')#, news=news)

@app.route('/shooting')
def shooting():
    return render_template('shooting.html')

@app.route('/beginners')
def beginners():
    return render_template('beginners.html')

#@app.route('/members_login', methods=('GET','POST'))
#def members():
#    login_user_form = LoginForm()
#
#    if login_user_form.validate_on_submit():
#        user = user_datastore.get_user(login_user_form.email.data)
#        if verify_and_update_password(login_user_form.password.data, user):
#            login_user(user, login_user_form.remember.data)
#            return redirect(url_for('admin.index'))
#
        #self._template_args['login_user_form'] = login_user_form
#    return render_template('members.html', form = login_user_form)
#    return render_template('members.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/submit', methods=['POST'])
def submit():
    if(request.method == 'POST'):
        about = request.form.get("about")
        recipient = 'yokinearcheryclub@gmail.com'
        enquiry = {
            1 : "General Enquiry",
            2 : "Come & Try",
            3 : "Beginner's course"
        }
        body = []
        first = request.form.get("form-first-name")
        last =  request.form.get("form-last-name")
        email = request.form.get("form-email")
        size = request.form.get("size")
         #age check for beginner's course
        info = request.form.get("info")

        body.append("Contact Name: %s %s" % (first,last))
        body.append("Email: %s" % (email))
        if(int(about) > 1):
            body.append("Group Size: %s" % (size))
        body.append("Enquiry Details:")
        body.append(info)
        msg = Message(enquiry.get(int(about)))
        msg.add_recipient(recipient)
        msg.body = "\r\n".join(body)
        mail.send(msg)
        return render_template('contact.html')

# initialise admin role and superuser
#@app.before_first_request
#def _init_admin_user_and_roles():
#    with app.app_context():
        # OLD WAY OF ADDING ROLE
        #admin_role = models.Role(name='admin', description='Administrator')
        #db.session.add(admin_role)
        #db.session.commit()

        # Add role if it doesn't exist
#        user_datastore.find_or_create_role(name='admin', description='Administrator')

#        try:
#            admin_user = user_datastore.create_user(
#                id=1,
#                first='Admin',
#                last='YokineArcheryClub',
#                email='callum.ingley@gmail.com',
#                password=encrypt_password('R0bert1ngley'),
#                roles=[models.Role.query.first() ]
#            )
#            db.session.add(admin_user)
#            db.session.flush()
#            db.session.commit()
#        except exc.IntegrityError:
#            db.session.rollback()
            #print('@@@Integrity Error')
#        except TypeError:
#            print "HERE TYPE ERROR"
#        finally:
#            db.session.commit()

def _delete_admin_user():
    with app.app_context():
        user = user_datastore.find_user(first='Callum')
        #print(user)
        if user:
            print(user.first)
            user_datastore.delete_user(user)
            db.session.query(models.User).filter_by(first='Callum').delete()
            print("Deleted user")
            db.session.commit()

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

if __name__ == "__main__":
    port = int(os.getenv('PORT','8080'))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)