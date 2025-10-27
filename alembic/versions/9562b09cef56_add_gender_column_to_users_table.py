"""add gender column to users table

Revision ID: 9562b09cef56
Revises: e52a4de9fb5f
Create Date: 2025-10-27 11:09:52.984054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9562b09cef56'
down_revision: Union[str, Sequence[str], None] = 'e52a4de9fb5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  
    op.add_column('users', sa.Column('gender', sa.String(20), nullable=True))

def downgrade() -> None:
    op.drop_column('users', 'gender')