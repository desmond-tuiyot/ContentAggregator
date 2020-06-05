from content_frontend import db
from content_frontend.models import Post, Source
from datetime import datetime


db.create_all()


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


create_db()