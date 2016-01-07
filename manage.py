from flask.ext.script import Manager
from app import webapp

manager = Manager(webapp)

@manager.command
def hello():
    from app.models import User,Mailer
    Mailer.welcomeMailer(User(1))

@manager.command
def indexer():
    from app.scripts import Indexer
    Indexer().getAllDataFromDB(query_condition=' and i.item_id>958')

if __name__ == "__main__":
    manager.run()
