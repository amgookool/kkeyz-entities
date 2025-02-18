"""Added Payments and Cart Tables

Revision ID: ba8b96da950a
Revises: 5cc64e587899
Create Date: 2024-07-14 09:03:13.863346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba8b96da950a'
down_revision: Union[str, None] = '5cc64e587899'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('is_converted', sa.Boolean(), nullable=False),
    sa.Column('subtotal', sa.Float(), nullable=False),
    sa.Column('tax', sa.Float(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['public.products.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['public.user_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_carts_product_id'), 'carts', ['product_id'], unique=False, schema='public')
    op.create_index(op.f('ix_public_carts_user_id'), 'carts', ['user_id'], unique=False, schema='public')
    op.create_table('cart_items',
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('coupon', sa.String(length=255), nullable=True),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['public.carts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['public.products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_cart_items_cart_id'), 'cart_items', ['cart_id'], unique=False, schema='public')
    op.create_index(op.f('ix_public_cart_items_product_id'), 'cart_items', ['product_id'], unique=False, schema='public')
    op.drop_constraint('addresses_user_profile_id_fkey', 'addresses', type_='foreignkey')
    op.create_foreign_key(None, 'addresses', 'user_profiles', ['user_profile_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('inventory_product_id_fkey', 'inventory', type_='foreignkey')
    op.create_foreign_key(None, 'inventory', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('product_reviews_product_id_fkey', 'product_reviews', type_='foreignkey')
    op.drop_constraint('product_reviews_user_id_fkey', 'product_reviews', type_='foreignkey')
    op.create_foreign_key(None, 'product_reviews', 'user_profiles', ['user_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.create_foreign_key(None, 'product_reviews', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('products_category_id_fkey', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'categories', ['category_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('user_profiles_user_id_fkey', 'user_profiles', type_='foreignkey')
    op.create_foreign_key(None, 'user_profiles', 'users', ['user_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('wishlists_product_id_fkey', 'wishlists', type_='foreignkey')
    op.drop_constraint('wishlists_user_id_fkey', 'wishlists', type_='foreignkey')
    op.create_foreign_key(None, 'wishlists', 'user_profiles', ['user_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.create_foreign_key(None, 'wishlists', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wishlists', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'wishlists', schema='public', type_='foreignkey')
    op.create_foreign_key('wishlists_user_id_fkey', 'wishlists', 'user_profiles', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('wishlists_product_id_fkey', 'wishlists', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'user_profiles', schema='public', type_='foreignkey')
    op.create_foreign_key('user_profiles_user_id_fkey', 'user_profiles', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'products', schema='public', type_='foreignkey')
    op.create_foreign_key('products_category_id_fkey', 'products', 'categories', ['category_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'product_reviews', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'product_reviews', schema='public', type_='foreignkey')
    op.create_foreign_key('product_reviews_user_id_fkey', 'product_reviews', 'user_profiles', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('product_reviews_product_id_fkey', 'product_reviews', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'inventory', schema='public', type_='foreignkey')
    op.create_foreign_key('inventory_product_id_fkey', 'inventory', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'addresses', schema='public', type_='foreignkey')
    op.create_foreign_key('addresses_user_profile_id_fkey', 'addresses', 'user_profiles', ['user_profile_id'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_public_cart_items_product_id'), table_name='cart_items', schema='public')
    op.drop_index(op.f('ix_public_cart_items_cart_id'), table_name='cart_items', schema='public')
    op.drop_table('cart_items', schema='public')
    op.drop_index(op.f('ix_public_carts_user_id'), table_name='carts', schema='public')
    op.drop_index(op.f('ix_public_carts_product_id'), table_name='carts', schema='public')
    op.drop_table('carts', schema='public')
    # ### end Alembic commands ###
