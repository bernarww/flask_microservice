from flask import Flask
from service import service_bp

app = Flask(__name__)

app.register_blueprint(service_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
