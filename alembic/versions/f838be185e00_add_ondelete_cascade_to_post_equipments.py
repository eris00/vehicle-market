"""Add ondelete cascade to post_equipments

Revision ID: f838be185e00
Revises: 9ced23b2b68a
Create Date: 2024-12-25 03:23:51.902731

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f838be185e00'
down_revision: Union[str, None] = '9ced23b2b68a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('images_post_id_fkey', 'images', type_='foreignkey')
    op.create_foreign_key(None, 'images', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('post_equipments_post_id_fkey', 'post_equipments', type_='foreignkey')
    op.drop_constraint('post_equipments_equipment_id_fkey', 'post_equipments', type_='foreignkey')
    op.create_foreign_key(None, 'post_equipments', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'post_equipments', 'equipments', ['equipment_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post_equipments', type_='foreignkey')
    op.drop_constraint(None, 'post_equipments', type_='foreignkey')
    op.create_foreign_key('post_equipments_equipment_id_fkey', 'post_equipments', 'equipments', ['equipment_id'], ['id'])
    op.create_foreign_key('post_equipments_post_id_fkey', 'post_equipments', 'posts', ['post_id'], ['id'])
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.create_foreign_key('images_post_id_fkey', 'images', 'posts', ['post_id'], ['id'])
    # ### end Alembic commands ###
