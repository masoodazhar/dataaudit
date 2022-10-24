from flask import Blueprint

from controllers.AuditRequestController import index, store, show, update, destroy

audit_bp = Blueprint('audit_bp', __name__)

audit_bp.route('/', methods=['GET'])(index)
audit_bp.route('/create', methods=['POST'])(store)
audit_bp.route('/<int:user_id>', methods=['GET'])(show)
audit_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
audit_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)