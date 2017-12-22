"""Utility file to seed set database from fake data for demo."""

from sqlalchemy import func
from model import User, Friend, Card, Invite, connect_to_db, db
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
                    password=pw,
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

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate friend relationships.
    Friend.query.delete()

    # Read friend file and insert data
    for line in open('friends.txt', 'rU'):
        line = line.rstrip()

        user_id, friend_id = line.split('|')

        friend = Friend(user_id=int(user_id), friend_id=int(friend_id))

        # Add each friend relationship to the session
        db.session.add(friend)

    # Commit at end
    db.session.commit()


def load_cards():
    """Loads cards in a deck into database."""

    print 'Cards'

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate cards.
    Card.query.delete()

    # Read cards file and insert data
    for line in open('cards.txt', 'rU'):
        line = line.rstrip()

        num, shade, shape, color = line.split('|')

        card = Card(number=num, shading=shade, shape=shape, color=color)

        # Add each card to the session
        db.session.add(card)

    # Commit at end
    db.session.commit()


def load_invites():
    """Loads invites from fake data into database."""

    print 'Invites'

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate cards.
    Invite.query.delete()

    # Read invites file and insert data
    for line in open('invites.txt', 'rU'):
        line = line.rstrip()

        user_id, email, accepted = line.split('|')

        # Convert string to boolean
        if accepted == 'True':
            accepted = True
        else:
            accepted = False

        invite = Invite(user_id=int(user_id), friend_email=email, accepted=accepted)

        # Add each invite to the session
        db.session.add(invite)

    # Commit at end
    db.session.commit()


def set_val_id():
    """Sets value for the next autoincrement after seeding database"""

    # Get the max autoincremented primary key in the database
    result = db.session.query(func.max(User.user_id)).one()
    user_max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': user_max_id + 1})

    # Get the max autoincremented primary key in the database
    result = db.session.query(func.max(Friend.link_id)).one()
    friend_max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('friends_link_id_seq', :new_id)"
    db.session.execute(query, {'new_id': friend_max_id + 1})

    # Get the max autoincremented primary key in the database
    result = db.session.query(func.max(Card.user_id)).one()
    card_max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('cards_card_id_seq', :new_id)"
    db.session.execute(query, {'new_id': card_max_id + 1})

    # Get the max autoincremented primary key in the database
    result = db.session.query(func.max(Invite.invite_id)).one()
    invite_max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('invites_invite_id_seq', :new_id)"
    db.session.execute(query, {'new_id': invite_max_id + 1})

    # Commit at end
    db.session.commit()


##############################################################################

# Helper functions


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Create fake data
    create_users()
    create_friends()
    create_cards()
    create_invites()

    # Import data for various tables into database
    load_users()
    load_friends()
    load_cards()
    load_invites()
    set_val_id()
