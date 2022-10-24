"""inititing tables (BankStatement and AuditRequests)

Revision ID: bde23627cba4
Revises: 
Create Date: 2022-10-24 14:52:38.480171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bde23627cba4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditrequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tracking_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('amount', sa.String(length=120), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('request_type', sa.String(length=50), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('audit_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auditrequest')
    # ### end Alembic commands ###
