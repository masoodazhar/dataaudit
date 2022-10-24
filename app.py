from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from routes.bank_bp import bank_bp
from routes.audit_bp import audit_bp

from models.BankStatement import bankDB
from models.AuditRequest import auditDB
db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate()

db.init_app(app)

migrate.init_app(db, bankDB)
migrate.init_app(db, auditDB)




app.register_blueprint(bank_bp, url_prefix='/bank')
app.register_blueprint(audit_bp, url_prefix='/audit')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
