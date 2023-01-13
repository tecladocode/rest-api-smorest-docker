"""empty message

Revision ID: 01c10acae368
Revises: e31961f78e35
Create Date: 2023-01-13 15:52:09.120185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01c10acae368'
down_revision = 'e31961f78e35'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_constraint('tags_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.create_unique_constraint('tags_name_key', ['name'])

    # ### end Alembic commands ###
