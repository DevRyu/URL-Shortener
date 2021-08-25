from logging import debug
from app import create_app
from settings import DockerConfig

if __name__ == "__main__":
    app = create_app(config=DockerConfig)
    app.run(host="0.0.0.0", port=5005, debug=True, threaded=True)
