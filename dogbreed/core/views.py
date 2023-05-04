# core/views.py
from flask import url_for, render_template, request, Blueprint
from dogbreed.core.form import UpdateUserForm
from dogbreed.core.picture_handler import add_profile_pic

core = Blueprint('core', __name__)

@core.route('/',methods=["GET","POST"])
def index():
    form = UpdateUserForm()
    pic = ""
    if form:
        if form.picture.data:
            pic = add_profile_pic(form.picture.data)
            #current_user.profile_image = pic

        #return redirect(url_for("users.account"))

    profile_image = url_for('static', filename='dog_pics/'+pic)
    return render_template("index.html",profile_image=form.picture.data,form=form)

# acount (update UserForm)
""" @core.route("/upload",methods=["GET","POST"])
def upload():

    return render_template("iindex.html",profile_image=profile_image,form=form) """
