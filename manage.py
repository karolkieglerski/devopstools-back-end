import unittest
import coverage

from flask_script import Manager

from devopstools import create_app, db
from devopstools.api.models import User

COV = coverage.coverage(
    branch=True,
    include='devopstools/*',
    omit=[
        'devopstools/tests/*'
    ]
)
COV.start()

app = create_app()
manager = Manager(app)


@manager.command
def test():
    tests = unittest.TestLoader().discover('devopstools/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('devopstools/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='michael', email="michael@realpython.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.commit()


if __name__ == '__main__':
    manager.run()
