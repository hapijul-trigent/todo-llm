"""llmNote default emptystring

Revision ID: c7c743a1db01
Revises: 6a00eb901270
Create Date: 2024-08-06 06:28:23.305764

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7c743a1db01'
down_revision: Union[str, None] = '6a00eb901270'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
