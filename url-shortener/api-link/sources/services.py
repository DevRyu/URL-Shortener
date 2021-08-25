from datetime import datetime
import re
from models import Link, db
from create_short_link import get_unique_short_id
from sqlalchemy.exc import IntegrityError
from flask import abort


def create_one_link(link_json):
    result = Link.get_one_by_url(link_json["url"])
    if result:
        return {
            "data": [
                {
                    "url": result.url,
                    "name": result.shortId,
                    "createdAt": result.createdAt,
                }
            ]
        }

    short_id = get_unique_short_id()
    one_link = Link.create_one(link_json["url"], short_id)
    try:
        db.session.add(one_link)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return abort(500)
    except Exception:
        db.session.rollback()
        return abort(500)

    response_model = {
        "data": [
            {
                "url": str(link_json["url"]),
                "name": short_id,
                "createdAt": str(
                    datetime.utcnow().isoformat(sep=" ", timespec="milliseconds")
                ),
            }
        ]
    }
    return response_model


def short_link_redirect(short_id):
    result = Link.get_one_by_short_id(short_id)
    return str(result.url)


def get_pagenated_urls(size, page):
    result = Link.get_pagenated(size, page)
    response_model = {
        "data": [
            {
                "url": data.url,
                "name": data.shortId,
                "createdAt": data.createdAt,
            }
            for data in result.items
        ],
    }
    return response_model


def get_one_detail_short_link(short_id):
    print(type(short_id))
    result = Link.get_one_with_alias(short_id)
    response_model = {
        "data": [
            {
                "shortId": str(result.url),
                "aliasName": "" if result.aliasName is None else result.aliasName,
                "createdAt": str(result.createdAt),
            }
        ]
    }
    return response_model


def update_alias_name(short_id, alias_name):
    result = Link.update_one_alias_name(short_id, alias_name)
    print(result.aliasName)
    result.aliasName = str(alias_name)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return abort(500)


def alias_name_redirect(alias_name):
    result = Link.get_one_by_alias(alias_name)
    return str(result.url)


def delete_one_short_id(short_id):
    result = Link.delete_row(short_id)
    try:
        db.session.delete(result)
        db.session.commit()
    except Exception:
        db.session.rollback()

    return {}
