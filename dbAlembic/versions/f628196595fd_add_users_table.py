"""add users table

Revision ID: f628196595fd
Revises: 02a266dae019
Create Date: 2022-01-18 11:40:16.126680

"""
from time import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f628196595fd'
down_revision = '02a266dae019'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
