"""empty message

Revision ID: 0db3567e61dd
Revises: 7c0494128ab3
Create Date: 2020-07-05 14:37:21.342134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0db3567e61dd'
down_revision = '7c0494128ab3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testdb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('news_site_one_1', sa.String(length=25), nullable=True),
    sa.Column('news_site_two_2', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('news_site_one_1'),
    sa.UniqueConstraint('news_site_two_2')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testdb')
    # ### end Alembic commands ###
