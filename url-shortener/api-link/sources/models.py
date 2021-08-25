from datetime import datetime
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask import abort
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import NoResultFound

db = SQLAlchemy()


class Link(db.Model):
    __tablename__ = "Link"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300), nullable=False)
    shortId = db.Column(db.String(5), nullable=False, unique=True)
    aliasName = db.Column(db.String(300), nullable=True, unique=True)
    createdAt = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    @classmethod
    def create_one(cls, url, short_id):
        one_link = Link(url=url, shortId=short_id)
        return one_link

    @classmethod
    def get_one_by_url(cls, url):
        try:
            return Link.query.filter_by(url=url).one()
        except NoResultFound:
            return None

    @classmethod
    def get_one_by_alias(cls, alias_name):
        try:
            return Link.query.filter_by(aliasName=alias_name).one()
        except NoResultFound:
            return None

    @classmethod
    def get_one_by_short_id(cls, short_id):
        try:
            return Link.query.filter_by(shortId=short_id).one()
        except NoResultFound:
            return abort(404)

    @classmethod
    def get_recent_one(cls):
        try:
            return Link.query.order_by(Link.shortId.desc()).first()
        except NoResultFound:
            return None

    @classmethod
    def get_pagenated(cls, size, page):
        try:
            return Link.query.paginate(int(page), per_page=int(size))
        except OperationalError:
            return abort(404)

    @classmethod
    def get_one_with_alias(cls, short_id):
        try:
            return Link.query.filter_by(shortId=short_id).one()
        except NoResultFound:
            return abort(404)

    @classmethod
    def update_one_alias_name(cls, short_id, alias_name):
        return Link.query.filter_by(shortId=short_id).one()

    @classmethod
    def delete_row(cls, short_id):
        try:
            return Link.query.filter_by(shortId=short_id).one()
        except NoResultFound:
            return abort(404)
