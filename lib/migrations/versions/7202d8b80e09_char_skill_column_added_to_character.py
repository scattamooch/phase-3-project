"""char_skill column added to character

Revision ID: 7202d8b80e09
Revises: 771ba1100259
Create Date: 2023-07-19 12:06:54.165382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7202d8b80e09'
down_revision = '771ba1100259'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('char_skill', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characters', 'char_skill')
    # ### end Alembic commands ###
