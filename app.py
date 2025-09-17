from flask import Flask
import config
from exts import db
from flask_migrate import Migrate
from models import auth
from apps.front import front_bp

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)

# 注册蓝图
app.register_blueprint(front_bp)

if __name__ == "__main__":
    app.run(debug=True)
