from flask_cors import CORS

from run import create_app

application = create_app()
CORS(application)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
