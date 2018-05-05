"""add chat column

Revision ID: db8aa0436455
Revises: 9a9f38036759
Create Date: 2018-05-05 02:15:19.042397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db8aa0436455'
down_revision = '9a9f38036759'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('chat_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'image', 'chat', ['chat_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.drop_column('image', 'chat_id')
    # ### end Alembic commands ###
