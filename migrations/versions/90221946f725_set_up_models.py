"""Set up models

Revision ID: 90221946f725
Revises: 
Create Date: 2018-07-19 17:23:25.949187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90221946f725'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('english_word', sa.String(), nullable=True),
    sa.Column('latin_top_choice', sa.String(), nullable=True),
    sa.Column('tweet_id', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('tweet_date', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entry_english_word'), 'entry', ['english_word'], unique=True)
    op.create_index(op.f('ix_entry_latin_top_choice'), 'entry', ['latin_top_choice'], unique=False)
    op.create_index(op.f('ix_entry_timestamp'), 'entry', ['timestamp'], unique=False)
    op.create_index(op.f('ix_entry_tweet_id'), 'entry', ['tweet_id'], unique=False)
    op.create_table('definitions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('latin_word', sa.String(), nullable=True),
    sa.Column('entry_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entry.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_definitions_latin_word'), 'definitions', ['latin_word'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_definitions_latin_word'), table_name='definitions')
    op.drop_table('definitions')
    op.drop_index(op.f('ix_entry_tweet_id'), table_name='entry')
    op.drop_index(op.f('ix_entry_timestamp'), table_name='entry')
    op.drop_index(op.f('ix_entry_latin_top_choice'), table_name='entry')
    op.drop_index(op.f('ix_entry_english_word'), table_name='entry')
    op.drop_table('entry')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###