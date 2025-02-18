"""Added Order table

Revision ID: 1e4a91be377f
Revises: ba8b96da950a
Create Date: 2024-07-14 09:06:35.260987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e4a91be377f'
down_revision: Union[str, None] = 'ba8b96da950a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['public.user_profiles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_orders_user_id'), 'orders', ['user_id'], unique=False, schema='public')
    op.drop_constraint('addresses_user_profile_id_fkey', 'addresses', type_='foreignkey')
    op.create_foreign_key(None, 'addresses', 'user_profiles', ['user_profile_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('cart_items_cart_id_fkey', 'cart_items', type_='foreignkey')
    op.drop_constraint('cart_items_product_id_fkey', 'cart_items', type_='foreignkey')
    op.create_foreign_key(None, 'cart_items', 'carts', ['cart_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.create_foreign_key(None, 'cart_items', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('carts_product_id_fkey', 'carts', type_='foreignkey')
    op.drop_constraint('carts_user_id_fkey', 'carts', type_='foreignkey')
    op.create_foreign_key(None, 'carts', 'user_profiles', ['user_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.create_foreign_key(None, 'carts', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('inventory_product_id_fkey', 'inventory', type_='foreignkey')
    op.create_foreign_key(None, 'inventory', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.drop_constraint('product_reviews_user_id_fkey', 'product_reviews', type_='foreignkey')
    op.drop_constraint('product_reviews_product_id_fkey', 'product_reviews', type_='foreignkey')
    op.create_foreign_key(None, 'product_reviews', 'products', ['product_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
    op.create_foreign_key(None, 'product_reviews', 'user_profiles', ['user_id'], ['id'], source_schema='public', referent_schema='public', ondelete='CASCADE')
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
    op.create_foreign_key('product_reviews_product_id_fkey', 'product_reviews', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('product_reviews_user_id_fkey', 'product_reviews', 'user_profiles', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'inventory', schema='public', type_='foreignkey')
    op.create_foreign_key('inventory_product_id_fkey', 'inventory', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'carts', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'carts', schema='public', type_='foreignkey')
    op.create_foreign_key('carts_user_id_fkey', 'carts', 'user_profiles', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('carts_product_id_fkey', 'carts', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'cart_items', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'cart_items', schema='public', type_='foreignkey')
    op.create_foreign_key('cart_items_product_id_fkey', 'cart_items', 'products', ['product_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('cart_items_cart_id_fkey', 'cart_items', 'carts', ['cart_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'addresses', schema='public', type_='foreignkey')
    op.create_foreign_key('addresses_user_profile_id_fkey', 'addresses', 'user_profiles', ['user_profile_id'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_public_orders_user_id'), table_name='orders', schema='public')
    op.drop_table('orders', schema='public')
    # ### end Alembic commands ###
