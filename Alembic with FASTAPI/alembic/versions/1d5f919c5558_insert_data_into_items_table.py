"""insert data into items table

Revision ID: 1d5f919c5558
Revises: 7b1ba8e1d3a2
Create Date: 2024-11-29 16:00:21.855721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d5f919c5558'
down_revision: Union[str, None] = '7b1ba8e1d3a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Insert records into the 'items' table (at least 10 records)
    op.execute("""
    INSERT INTO items (name, description) VALUES
    ('Laptop', 'A high-end gaming laptop'),
    ('Phone', 'Latest smartphone model'),
    ('Headphones', 'Noise-cancelling over-ear headphones'),
    ('Smartwatch', 'Fitness tracking smartwatch'),
    ('Camera', 'DSLR camera for professional photography'),
    ('Mouse', 'Wireless mouse with ergonomic design'),
    ('Keyboard', 'Mechanical keyboard with RGB lights'),
    ('Monitor', 'Curved 27-inch 4K monitor'),
    ('Speaker', 'Bluetooth speaker with surround sound'),
    ('Charger', 'Fast charging USB-C charger')
    """)


def downgrade():
    # Optionally, you can add logic here to delete these records if needed
    op.execute("""
    DELETE FROM items WHERE name IN (
        'Laptop', 'Phone', 'Headphones', 'Smartwatch', 'Camera',
        'Mouse', 'Keyboard', 'Monitor', 'Speaker', 'Charger'
    )
    """)