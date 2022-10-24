from flask import Blueprint

from controllers.BankStatementController import index, store, show, update, destroy

bank_bp = Blueprint('bank_bp', __name__)

bank_bp.route('/', methods=['GET'])(index)
bank_bp.route('/create', methods=['POST'])(store)
bank_bp.route('/<int:user_id>', methods=['GET'])(show)
bank_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
bank_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)