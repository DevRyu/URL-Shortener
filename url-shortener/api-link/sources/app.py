import os
import logging

from flask import Flask
from views import link_link
from settings import LocalConfig


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(link_link)

    from models import db, Link

    db.init_app(app)
    with app.app_context():
        import sqlalchemy

        link_existed = sqlalchemy.inspect(db.engine).has_table(Link.__tablename__)
        if not link_existed:
            db.create_all()

    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.root.setLevel(logging.INFO)

    return app


if __name__ == "__main__":
    app = create_app(config=LocalConfig)
    app.run(host="0.0.0.0", port=5005, debug=True, threaded=True)
