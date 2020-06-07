from flask import render_template, request, Blueprint
from content_aggregator.content_frontend.models import Post, Source


posts = Blueprint('posts', __name__)

@posts.route("/")
@posts.route("/home")
def home():
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(per_page=20, page=page)
    sources = Source.query.all()
    return render_template('home.html', posts=posts, sources=sources)


@posts.route("/posts/<string:source_name>")
def source_posts(source_name):
    page = request.args.get('page', default=1, type=int)
    source = Source.query.filter_by(source_name=source_name).first_or_404()
    posts = Post.query.filter_by(source=source)\
        .order_by(Post.date.desc()).paginate(per_page=20, page=page)
    sources = Source.query.all()
    return render_template('source_posts.html', posts=posts, sources=sources, current_source=source)
