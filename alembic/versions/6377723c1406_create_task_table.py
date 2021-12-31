"""create task table

Revision ID: 6377723c1406
Revises: 
Create Date: 2021-12-30 20:31:44.440679

"""
import sqlalchemy as sa

from alembic import op

revision = '6377723c1406'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('message', sa.Text(), nullable=False),
        sa.Column('is_done', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_is_done'), 'tasks', ['is_done'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_tasks_is_done'), table_name='tasks')
    op.drop_table('tasks')
