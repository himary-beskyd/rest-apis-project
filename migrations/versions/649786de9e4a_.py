"""empty message

Revision ID: 649786de9e4a
Revises: 
Create Date: 2024-02-26 17:14:24.410519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '649786de9e4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
