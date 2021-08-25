class DockerConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:test@postgres-link:5432/postgres"
    )
    API_LINK_PORT = "5005"
    API_LINK_HOST = "api-link"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class LocalConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:test@0.0.0.0:35431/postgres"
    )
    API_LINK_PORT = "5005"
    API_LINK_HOST = "localhost"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
