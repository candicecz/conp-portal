# -*- coding: utf-8 -*-
"""Configuration Module

Module that contains the Data Models

"""
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from pytz import timezone

eastern = timezone('US/Eastern')


@login_manager.user_loader
def load_user(id):
    """
        Ensures that the loaded user in templates is
        a user class and not a context class

        Args:
            id: the id of the user from current_user

        Returns:
            the user class for the id
    """
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    """
        Provides User Model
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True, unique=True)
    oauth_id = db.Column(db.String(256), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    is_whitelisted = db.Column(db.Boolean, default=False, nullable=False)
    is_pi = db.Column(db.Boolean, default=False, nullable=False)
    is_account_expired = db.Column(db.Boolean, default=False, nullable=False)
    affiliation = db.Column(db.String(128))
    expiration = db.Column(db.DateTime, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=eastern))
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=eastern))

    def set_password(self, password):
        """
            utility function to hashes and sets the password

            Args:
                password: the plain text password
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
            utility function that checks the hashed password

            Args:
                password: plain text to check hashed password against

            Returns:
                boolean as to whether the two strings match
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Dataset(db.Model):
    """
        Provides DataSet Model
    """
    __tablename__ = 'datasets'

    id = db.Column(db.Integer, primary_key=True)
    dataset_id = db.Column(db.String(64), index=True, unique=True)
    annex_uuid = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text, index=True)
    owner_id = db.Column(db.Integer, index=True)
    download_path = db.Column(db.String(64), index=True)
    raw_data_url = db.Column(db.String(128), index=True)
    image = db.Column(db.LargeBinary, default=None)
    name = db.Column(db.String(256), index=True)
    modality = db.Column(db.String(64), index=True)
    version = db.Column(db.String(6), index=True)
    format = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True)
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_updated = db.Column(db.DateTime, default=datetime.now())
    is_private = db.Column(db.Boolean, index=True)

    def __repr__(self):
        return '<Dataset {}>'.format(self.name)


class DatasetStats(db.Model):
    """
        Provides DatasetStats model for keeping stats on downloads and views
    """
    __tablename__ = 'dataset_stats'

    id = db.Column(db.Integer, primary_key=True)
    dataset_id = db.Column(db.String(64), index=True, unique=True)
    size = db.Column(db.Integer, index=True)
    files = db.Column(db.Integer, index=True)
    sources = db.Column(db.Integer, index=True)
    num_subjects = db.Column(db.Integer, index=True)
    num_downloads = db.Column(db.Integer, index=True)
    num_likes = db.Column(db.Integer, index=True)
    num_views = db.Column(db.Integer, index=True)
    date_updated = db.Column(db.DateTime, default=datetime.now())


class Pipeline(db.Model):
    """
        Provides Pipeline Model for describing metadata for an execution pipeline
    """
    __tablename__ = 'pipelines'

    id = db.Column(db.Integer, primary_key=True)
    pipeline_id = db.Column(db.Integer, index=True, unique=True)
    owner_id = db.Column(db.Integer, index=True)
    name = db.Column(db.String(256), index=True)
    version = db.Column(db.String(128), index=True)
    is_private = db.Column(db.Boolean, index=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=eastern))
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=eastern))

    def __repr__(self):
        return '<Pipeline {}>'.format(self.name)
