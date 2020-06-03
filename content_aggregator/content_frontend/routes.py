# import os
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from content_aggregator.content_frontend import app, db
# from content_aggregator.content_frontend.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from content_aggregator.content_frontend.models import Post


@app.route("/")
@app.route("/home")
def home():
    # page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date.desc())
        # .paginate(per_page=20, page=page)
    return render_template('home.html', posts=posts)


#
# @app.route('/about')
# def about():
#     return render_template('about.html', title="About")


# @app.route('/register')
# def register():
#     return render_template('register.html')
#
#
# @app.route('/login')
# def login():
#     return render_template('login.html')
#
#
# @app.route('/account')
# def account():
#     return render_template('account.html')
#
#
# @app.route('/logout')
# def logout():
#     return render_template('logout.html')


if __name__=="__main__":
    app.run(debug=True)