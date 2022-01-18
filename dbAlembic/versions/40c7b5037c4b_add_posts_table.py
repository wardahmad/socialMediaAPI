"""add posts table

Revision ID: 40c7b5037c4b
Revises: 
Create Date: 2022-01-18 11:14:38.397159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40c7b5037c4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
