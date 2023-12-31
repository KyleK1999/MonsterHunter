"""Add default_health to Character

Revision ID: 6594c1898452
Revises: 6c632025fa36
Create Date: 2023-08-10 20:17:37.965331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6594c1898452'
down_revision: Union[str, None] = '6c632025fa36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('default_health', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characters', 'default_health')
    # ### end Alembic commands ###
