from content_aggregator.content_frontend import create_app, db
from content_aggregator.content_frontend.models import Source, Post

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Source': Source, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
