"""Utility file to seed set database from fake data for demo."""

from sqlalchemy import func
from model import User, connect_to_db, db
from photo_url import PHOTOS_F as womenpics, PHOTOS_M as menpics
from datetime import datetime
from server import app
from faker import Faker
# import re
import random

fake = Faker()

##############################################################################

def create_users():
    """
    Users data created from mockaroo API for consistency of user.

    Merges with fake user pics from randomuser.me pics rather than robohash url.
    """

    print 'Users'

    with open('users.txt', 'r') as users:
        # Randomly chooses photo url to append to each user
        lines = [''.join([x.strip(), '|' + random.choice(womenpics + menpics),
                 '\n']) for x in users.readlines()]

    with open('users.txt', 'w') as users:
        users.writelines(lines)


def create_friends():
    """Creates friends relationships from Faker."""

    print 'Friends'

    with open('friends.txt', 'w+') as friends:

        for i in range(500):
            # Max is based on maximum users that were seeded from mockaroo
            user_id = fake.random_int(min=1, max=100)

            friend_id = fake.random_int(min=1, max=100)

            # Generates new friend_id if user is friends with him/herself
            while user_id == friend_id:
                friend_id = fake.random_int(min=1, max=100)

            friends.write('{}|{}\n'.format(user_id, friend_id))


def create_cards():
    """Creates card combinations in set game."""

    # TO DO: Either build out or find url/images for pic of each card for game

    print 'Cards'

    numbers = ['one', 'two', 'three']
    shadings = ['solid', 'striped', 'outlined']
    shapes = ['oval', 'squiggle', 'diamond']
    colors = ['red', 'purple', 'green']

    with open('cards.txt', 'w+') as cards:
        for num in numbers:
            num = num
            for shade in shadings:
                shade = shade
                for shape in shapes:
                    shape = shape
                    for color in colors:
                        color = color
                        cards.write('{}|{}|{}|{}\n'.format(num, shade, shape, color))


# TO DO: determine if we need to seed data for the other tables or will they populate
# from game play


def create_invites():
    """Creates invites from Faker."""

    print 'Invites'

    with open('invites.txt', 'w+') as invites:
        for i in range(200):
            invites.write('{}|{}|{}\n'.format(fake.random_int(min=1, max=100),
                                              fake.free_email(),
                                              fake.boolean(chance_of_getting_true=10),
                                              ))


def load_users():
    """Loads users from fake data into database."""

    print 'Users'

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users; however, user_id would be
    # sequential so may want to delete and create database if need be.
    User.query.delete()

    # Read user file and insert data
    for line in open('users.txt', 'rU'):
        line = line.rstrip()

        (user_id, username, pw, fname, lname, email, valid_email, date_str, lat,
            lng, pic) = line.split('|')

        # Convert to datetime format
        join_date = datetime.strptime(date_str, '%Y-%m-%d')

        # Convert string to boolean
        if valid_email == 'true':
            valid_email = True
        else:
            valid_email = False

        user = User(username=username,
                    password=password,
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    valid_email=valid_email,
                    join_date=join_date,
                    user_pic=pic,
                    location='POINT({} {})'.format(lng, lat),
                    lat=float(lat),
                    lng=float(lng),
                    )

        # Add each user to the session
        db.session.add(user)

    # Commit at end
    db.session.commit()


def load_friends():
    """Loads friends relationships from fake data into database."""

    print 'Friends'

##############################################################################

# Helper functions


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()