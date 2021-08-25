from flask import request, Blueprint
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from services import (
    short_link_redirect,
    create_one_link,
    get_pagenated_urls,
    get_one_detail_short_link,
    update_alias_name,
    alias_name_redirect,
    delete_one_short_id,
)
from pydantic import ValidationError
from schemas import UrlValidation

link_link = Blueprint("link_link", __name__)


@link_link.route("/short-links", methods=["POST"])
def post_short_link_request():
    try:
        link_json_ = {} if request.json is None else request.json
        link_json = UrlValidation(**link_json_).dict()
    except ValidationError:
        return {}, 404
    res = create_one_link(link_json)
    return res, 200


@link_link.route("/r/<short_id>", methods=["GET"])
def get_short_link_redirect(short_id):
    return short_link_redirect(short_id), 302


@link_link.route("/short-links", methods=["GET"])
def get_pagenated_short_links():
    size = request.args.get("size")
    page = request.args.get("page")
    return get_pagenated_urls(size, page), 200


@link_link.route("/short-links/<short_id>", methods=["GET"])
def get_one_short_link(short_id):
    print(short_id)
    return get_one_detail_short_link(short_id), 200


@link_link.route("/short-links/<short_id>", methods=["PATCH"])
def patch_alias_url(short_id):
    alias_json = {} if request.json is None else request.json
    update_alias_name(short_id, alias_json["aliasName"])
    return {}, 200


@link_link.route("/a/<alias_name>", methods=["GET"])
def get_alias_name_redirect(alias_name):
    return alias_name_redirect(alias_name), 302


@link_link.route("/short-links/<short_id>", methods=["DELETE"])
def delete_one_short_links(short_id):
    return delete_one_short_id(short_id), 200
