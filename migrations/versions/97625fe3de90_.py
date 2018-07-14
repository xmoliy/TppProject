"""empty message

Revision ID: 97625fe3de90
Revises: 50a3f21417d2
Create Date: 2018-06-06 16:23:53.005058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97625fe3de90'
down_revision = '50a3f21417d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('nickname', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=12), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_life', sa.Boolean(), nullable=True),
    sa.Column('regist_time', sa.DateTime(), nullable=True),
    sa.Column('last_login_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_user')
    # ### end Alembic commands ###