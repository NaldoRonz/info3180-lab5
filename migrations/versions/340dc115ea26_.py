"""empty message

Revision ID: 340dc115ea26
Revises: 
Create Date: 2020-04-08 17:45:02.943761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '340dc115ea26'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###