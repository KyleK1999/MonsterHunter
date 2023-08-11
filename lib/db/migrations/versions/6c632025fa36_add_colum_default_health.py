"""add colum default health

Revision ID: 6c632025fa36
Revises: 77e82df02488
Create Date: 2023-08-10 16:18:56.985398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c632025fa36'
down_revision: Union[str, None] = '77e82df02488'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('monsters', sa.Column('default_health', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('monsters', 'default_health')
    # ### end Alembic commands ###
