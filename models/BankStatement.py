from flask_sqlalchemy import SQLAlchemy

bankDB = SQLAlchemy()

class BankStatement(bankDB.Model):
    __tablename__ = 'bankstatement'

    id = bankDB.Column(bankDB.Integer, primary_key=True)
    tracking_id = bankDB.Column(bankDB.Integer())
    name = bankDB.Column(bankDB.Text)
    amount = bankDB.Column(bankDB.String(120))
    comment = bankDB.Column(bankDB.Text)
    date = bankDB.Column(bankDB.DateTime)
    auditdate = bankDB.Column(bankDB.DateTime)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'tracking_id': self.tracking_id,
            'name': self.name,
            'amount': self.amount,
            'comment': self.comment,
            'date': self.date,
            'auditdate': self.auditdate
        }