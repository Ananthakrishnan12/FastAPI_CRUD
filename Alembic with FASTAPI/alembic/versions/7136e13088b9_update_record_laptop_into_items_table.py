"""update record LAPTOP into items table

Revision ID: 7136e13088b9
Revises: 1d5f919c5558
Create Date: 2024-11-29 16:02:46.374871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7136e13088b9'
down_revision: Union[str, None] = '1d5f919c5558'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Update a record in the 'items' table
    op.execute("""
    UPDATE items
    SET description = 'Updated description for Laptop'
    WHERE name = 'Laptop'
    """)

def downgrade():
    # Optionally, revert the update in case of downgrade
    op.execute("""
    UPDATE items
    SET description = 'A high-end gaming laptop'
    WHERE name = 'Laptop'
    """)
