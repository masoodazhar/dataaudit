from flask_sqlalchemy import SQLAlchemy

auditDB = SQLAlchemy()

class AuditRequest(auditDB.Model):
    __tablename__ = 'auditrequest'

    id = auditDB.Column(auditDB.Integer, primary_key=True)
    tracking_id = auditDB.Column(auditDB.Integer())
    name = auditDB.Column(auditDB.Text)
    amount = auditDB.Column(auditDB.String(120))
    comment = auditDB.Column(auditDB.Text)
    request_type = auditDB.Column(auditDB.String(50))
    date = auditDB.Column(auditDB.DateTime)
    audit_date = auditDB.Column(auditDB.DateTime)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'tracking_id': self.tracking_id,
            'name': self.name,
            'amount': self.amount,
            'request_type': self.request_type,
            'comment': self.comment,
            'date': self.date,
            'audit_date': self.audit_date
        }