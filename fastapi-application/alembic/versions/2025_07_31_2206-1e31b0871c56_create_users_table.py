"""create users table

Revision ID: 1e31b0871c56
Revises:
Create Date: 2025-07-31 22:06:49.528549

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "1e31b0871c56"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
