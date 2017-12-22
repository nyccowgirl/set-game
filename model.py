from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import func
from geoalchemy2 import Geometry
# from datetime import datetime

db = SQLAlchemy()

##############################################################################

# Model definitions


class User(db.Model):
    """ User model """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    # TO DO: encrypt
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    valid_email = db.Column(db.Boolean, nullable=False, default=False)
    # TO DO: send email with url to validate email after registration
    join_date = db.Column(db.DateTime, nullable=False,
                          default=db.func.current_timestamp())
    user_pic = db.Column(db.String(50), nullable=True)
    location = db.Column(Geometry(geometry_type='POINT'), nullable=True)

    # FIXME: Not sure if lat/lng are needed to store geocode or if duplicative with location
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)

    # Built-in regex constraint for email
    __table_args__ = (db.CheckConstraint("email ~ '^[A-Z0-9a-z._%+-]+@[A-Z0-9a-z.-]+\.[A-Za-z]{2,}$'"),)

    # TO DO: build out relationship mapping once all tables are built out
    friends = db.relationship('User', secondary='friends',
                              primaryjoin='User.user_id == Friend.user_id',
                              secondaryjoin='User.user_id == Friend.friend_id')

    def __repr__(self):
        """ Displays info for user. """

        return (u'<user_id={} username={} email={}>'.format(self.user_id,
                self.username, self.email))


class Friend(db.Model):
    """ Relationship information between user profiles. """

    __tablename__ = 'friends'

    link_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        """ Displays friend info. """

        return (u'<user_id={} friend_id={}>'.format(self.user_id, self.friend_id))


class Card(db.Model):
    """ Card model """

    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    number = db.Column(db.Enum('one', 'two', 'three'), nullable=False)
    shading = db.Column(db.Enum('solid', 'striped', 'outlined'), nullable=False)
    shape = db.Column(db.Enum('oval', 'squiggle', 'diamond'), nullable=False)
    color = db.Column(db.Enum('red', 'purple', 'green'), nullable=False)
    card_pic = db.Column(db.String(50), nullable=False)

    # TO DO: build out relationship mapping once all tables are built out

    def __repr__(self):
        """ Displays info for game card. """

        return (u'<card_id={} no.={} fill={} shape={} color={}>'.format(self.card_id,
                self.number, self.fill, self.shape, self.color))


class Game(db.Model):
    """ Game model """

    __tablename__ = 'games'

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    start_date = db.Column(db.DateTime, nullable=False,
                           default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime, nullable=True)

    # TO DO: build out relationship mapping once all tables are built out

    def __repr__(self):
        """ Displays info for game. """

        return (u'<game_id={} progress={} end_date={}>'.format(self.game_id,
                self.progress, self.end_date))


class GamePlayer(db.Model):
    """ Players for each game model """

    __tablename__ = 'gplayers'

    gplayer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)

    # TO DO: build out relatioship mapping once all tables are built out
    user = db.relationship('User', backref='gplayer')  # FIXME: one to one or one to many?
    game = db.relationship('Game', backref='gplayers')  # FIXME: one to one or one to many?

    def __repr__(self):
        """ Displays info for player per game. """

        return (u'<gplayer_id={} game_id={} player_id={} score={}'.format(self.gplayer_id,
                self.game_id, self.player_id, self.score))


class GameCard(db.Model):
    """ Cards for each game model """

    __tablename__ = 'gcards'

    gcard_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.card_id'), nullable=False)
    status = db.Column(db.Enum('deck', 'dealt', 'played'), nullable=False,
                       default='deck')

    # TO DO: build out relationship mapping once all tables are built out
    game = db.relationship('Game', backref='gcards')
    cards = db.relationship('Card', backref='gcards')

    def __repr__(self):
        """ Displays info for card per game. """

        return (u'<gcard_id={} game_id={} card_id={} progress={}>'.format(self.gcard_id,
                self.game_id, self.card_id, self.progress))


class Stat(db.Model):
    """ Statistic model """

    __tablename__ = 'stats'

    stat_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    stat_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """ Displays info for statistic type. """

        return (u'<stat_id={} stat_name={}>'.format(self.stat_id, self.stat_name))


class StatPlayer(db.Model):
    """ Statistics per player model """

    __tablename__ = 'splayers'

    splayer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    stat_id = db.Column(db.Integer, db.ForeignKey('stats.stat_id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    result = db.Column(db.Integer, nullable=False)
    # FIXME: Would all results be integers or can be strings?

    # TO DO: build out relationship mapping once all tables are built out
    games = db.relationship('Game', backref='splayers')
    stat = db.relationship('Stat', backref='splayers')

    def __repr__(self):
        """ Displays info for stats per player. """

        return (u'<splayer_id={} stat_id={} game_id={} result={}>'
                .format(self.splayer_id, self.stat_id, self.game_id, self.result))


class GamePlay(db.Model):
    """ Game transactions model """

    __tablename__ = 'gplays'

    gplay_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    gplayer_id = db.Column(db.Integer, db.ForeignKey('gplayers.gplayer_id'), nullable=False)
    card1 = db.Column(db.Integer, db.ForeignKey('cards.card_id'), nullable=False)
    card2 = db.Column(db.Integer, db.ForeignKey('cards.card_id'), nullable=False)
    card3 = db.Column(db.Integer, db.ForeignKey('cards.card_id'), nullable=False)
    is_set = db.Column(db.Boolean, nullable=False)

    # TO DO: build out relationship mapping once all tables are built out
    gplayers = db.relationship('GamePlayer', backref='gplays')
    cards = db.relationship('Card', backref='gplays')

    def __repr__(self):
        """ Displays info for each move/play. """

        return (u'<gplay_id={} gplayer_id={} is_set={}>'.format(self.gplay_id,
                self.gplayer_id, self.is_set))


class Invite(db.Model):
    """ Invite model """

    __tablename__ = 'invites'

    invite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    friend_email = db.Column(db.String(50), nullable=False)
    accepted = db.Column(db.Boolean, nullable=False, default=False)

    # Built-in regex constraint for email
    __table_args__ = (db.CheckConstraint("friend_email ~ '^[A-Z0-9a-z._%+-]+@[A-Z0-9a-z.-]+\.[A-Za-z]{2,}$'"),)

    # TO DO: build out relationship mapping once all tables are built out
    users = db.relationship('User', backref='invites')

    def __repr__(self):
        """ Displays invite info. """

        return (u'<invite_id={} user_id={} accepted={}>'.format(self.invite_id,
                self.user_id, self.accepted))

##############################################################################

# Helper functions


def connect_to_db(app, db_uri='postgresql:///set'):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."

    db.create_all()
