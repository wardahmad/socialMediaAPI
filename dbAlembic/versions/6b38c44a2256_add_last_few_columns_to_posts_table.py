"""add last few columns to posts table

Revision ID: 6b38c44a2256
Revises: 2b6f6e823e35
Create Date: 2022-01-18 12:06:58.997098

"""
from time import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b38c44a2256'
down_revision = '2b6f6e823e35'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
