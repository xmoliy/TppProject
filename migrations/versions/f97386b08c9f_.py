"""empty message

Revision ID: f97386b08c9f
Revises: 97625fe3de90
Create Date: 2018-06-07 00:15:26.369726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f97386b08c9f'
down_revision = '97625fe3de90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_user', sa.Column('photo_url', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_user', 'photo_url')
    # ### end Alembic commands ###
