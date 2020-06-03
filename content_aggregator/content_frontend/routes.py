# import os
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from content_aggregator.content_frontend import app, db
# from content_aggregator.content_frontend.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from content_aggregator.content_frontend.models import Post, Source
from datetime import datetime

# db.create_all()


def create_db():
    # create dummy source data and post data
    source1 = Source(source_name='Analytics Vidhya',
                     link='https://www.analyticsvidhya.com/blog/',
                     )
    source2 = Source(source_name='KDnuggets',
                     link='https://www.kdnuggets.com/news/index.html',
                     )
    source3 = Source(source_name='CSS Tricks',
                     link='https://css-tricks.com/archives/',
                     )
    source4 = Source(source_name='CodePen Blog',
                     link='https://blog.codepen.io/',
                     )
    db.session.add(source1)
    db.session.add(source2)
    db.session.add(source3)
    db.session.add(source4)
    db.session.commit()
    print("we got here. abount to be a problem")

    date = datetime.strptime('2020-06-03', '%Y-%m-%d')
    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source1)
    db.session.add(post)

    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source2)
    db.session.add(post)

    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source4)
    db.session.add(post)

    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source1)
    db.session.add(post)

    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source1)
    db.session.add(post)

    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source2)
    db.session.add(post)

    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source3)
    db.session.add(post)

    post = Post(title='6 Open Source Data Science Projects to Impress your Interviewer',
                link='https://www.analyticsvidhya.com/blog/2020/06/6-open-source-data-science-projects-interviewer/',
                date=date,
                source=source4)
    db.session.add(post)

    db.session.commit()
    print("we got here. No problems")


# create_db()

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(per_page=2, page=page)
    # posts = Post.query.order_by(Post.date.desc())
    sources = Source.query.all()
    return render_template('home.html', posts=posts, sources=sources)


@app.route("/posts/<string:source_name>")
def source_posts(source_name):
    # page = request.args.get('')
    source = Source.query.filter_by(source_name=source_name).first_or_404()
    posts = Post.query.filter_by(source=source).order_by(Post.date.desc())
    sources = Source.query.all()
    return render_template('source_posts.html', posts=posts, sources=sources, current_source=source)
    pass

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
