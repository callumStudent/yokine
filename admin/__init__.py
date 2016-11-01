from flask import redirect, url_for, render_template
from flask_admin import AdminIndexView, expose, BaseView
from flask_admin.contrib import sqla
from flask.ext.security.forms import LoginForm
from flask.ext.security.utils import verify_and_update_password, login_user
from flask.ext.security.core import current_user
from yokine import user_datastore

class IndexView(AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('admin/master.html')

class LoginView(BaseView):

    def is_visible(self):
        return not current_user.is_authenticated

    @expose('/', methods=('GET', 'POST'))
    def index(self):
        login_user_form = LoginForm()

        if login_user_form.validate_on_submit():
            user = user_datastore.get_user(login_user_form.email.data)
            if verify_and_update_password(login_user_form.password.data, user):
                login_user(user, login_user_form.remember.data)
                return self.render('admin/master.html')#redirect(url_for('indexview.index'))

        #self._template_args['login_user_form'] = login_user_form
        return render_template('members.html', login_user_form=login_user_form)

#class NewsPostView(sqla.ModelView):

#    column_list = ['title', 'content', 'date', 'live']
#    column_editable_list = ('live',)
#    form_columns = ['title', 'content']
#    form_widget_args = {
#        'content': {
#            'rows': 15
#        }
#    }

#    def is_accessible(self):
#        return current_user.is_authenticated

    #def get_save_return_url(self, model, is_created):
    #    return url_for('newspost.index_view')

    #def _handle_view(self, name, **kwargs):
    #    if not self.is_accessible():
    #        return redirect(url_for('loginview.index', next=request.url))

#    def __init__(self, session, **kwargs):
#        super(NewsPostView, self).__init__(NewsPost, session, **kwargs)

#class CategoryView(sqla.ModelView):

#    form_columns = ['name']
#    column_labels = dict(name='Category')

#    def is_accessible(self):
#        return current_user.is_authenticated

    #def _handle_view(self, name, **kwargs):
    #    if not self.is_accessible():
    #        return redirect(url_for('loginview.index', next=request.url))

#    def __init__(self, session,  **kwargs):
#        super(CategoryView, self).__init__(Category, session, **kwargs)