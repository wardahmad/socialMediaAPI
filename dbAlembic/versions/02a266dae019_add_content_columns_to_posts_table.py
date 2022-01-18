"""add content columns to posts table

Revision ID: 02a266dae019
Revises: 40c7b5037c4b
Create Date: 2022-01-18 11:35:29.106710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02a266dae019'
down_revision = '40c7b5037c4b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
