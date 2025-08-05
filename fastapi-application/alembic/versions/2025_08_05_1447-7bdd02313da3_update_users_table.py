"""update users table

Revision ID: 7bdd02313da3
Revises: f9219f0c4f35
Create Date: 2025-08-05 14:47:38.096122

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "7bdd02313da3"
down_revision: Union[str, Sequence[str], None] = "f9219f0c4f35"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f("uq_users_foo"), "users", ["foo", "bar"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("uq_users_foo"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
