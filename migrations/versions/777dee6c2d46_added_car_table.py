"""added car table

Revision ID: 777dee6c2d46
Revises: 145f79c0573a
Create Date: 2023-07-11 13:49:45.369927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '777dee6c2d46'
down_revision = '145f79c0573a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('make', sa.String(length=150), nullable=True),
    sa.Column('model', sa.String(length=150), nullable=True),
    sa.Column('year', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('color', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('miles_per_gallon', sa.String(length=150), nullable=True),
    sa.Column('max_speed', sa.String(length=100), nullable=True),
    sa.Column('seats', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###