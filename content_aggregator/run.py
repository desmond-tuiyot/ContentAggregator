from content_aggregator.content_frontend import create_app, db

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
