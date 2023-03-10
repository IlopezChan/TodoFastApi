"""First migration

Revision ID: 66d8290fe30e
Revises: 
Create Date: 2023-02-07 12:36:48.441865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66d8290fe30e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Nombre', sa.String(length=255), nullable=True),
    sa.Column('UserName', sa.String(length=100), nullable=True),
    sa.Column('Email', sa.String(length=255), nullable=True),
    sa.Column('Password', sa.String(length=250), nullable=True),
    sa.Column('Estatus', sa.Enum('Activo', 'Inactivo', 'Bloqueado', name='estatusenum'), nullable=True),
    sa.Column('FechaAlta', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Nombre', sa.String(length=255), nullable=True),
    sa.Column('Descripcion', sa.String(length=255), nullable=True),
    sa.Column('Estatus', sa.Enum('Activo', 'Completado', name='estatusenum'), nullable=True),
    sa.Column('FechaAlta', sa.Date(), nullable=True),
    sa.Column('FechaBaja', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_id'), 'tasks', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tasks_id'), table_name='tasks')
    op.drop_table('tasks')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
