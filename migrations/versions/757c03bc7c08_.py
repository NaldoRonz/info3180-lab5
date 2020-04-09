"""empty message

Revision ID: 757c03bc7c08
Revises: 340dc115ea26
Create Date: 2020-04-08 17:46:00.240637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '757c03bc7c08'
down_revision = '340dc115ea26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###