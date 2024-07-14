from sqlalchemy import (UUID, Boolean, Column, Enum, Float, ForeignKey,
                        Integer, MetaData, String, Text)
from sqlalchemy.orm import Relationship, declarative_base

from kkeyz_entities.enumerations import UserStatus, UserTypes

from .templates import IntegerBase, UUIDBase

metadata = MetaData(schema="public")

Base = declarative_base(metadata=metadata)

class Category(IntegerBase,Base):
    """
    The Category Model

    This is a one-to-many relationship with the Product model.
        - A category can have multiple products
        - A product can only belong to one category

    Relationships:
        - Products

    Fields:
        - name
        - description
    """
    # Metadata
    __tablename__ = "categories"
    # Fields
    name = Column("name", String(255), nullable=False)
    description = Column("description", String(255), nullable=True)

    # Relationships
    # One-to-Many
    products = Relationship("Product", back_populates="categories", passive_deletes=True)


class Product(IntegerBase, Base):
    """The Product Model
    
    This is a one-to-many relationship with the Category model.
        - A category can have multiple products
        - A product can only belong to one category
    
    This is a one-to-many relationship with the ProductReviews model.
        - A product can have multiple reviews
        - A review can only belong to one product

    Relationships:
        - Categories
        - ProductReviews

    Fields:
        - name
        - description
        - price
        - category
        - quantity -> refers to the quantity of the product available to sell
        - reviews
        - media
        - status -> refers to the status of the product in retail
    """
    # Metadata
    __tablename__ = "products"
    # Fields
    name = Column("name", String(255), nullable=False)
    description = Column("description", String(255), nullable=False)
    quantity = Column("quantity", Integer, nullable=False)
    price = Column("price", Float, nullable=False)
    media = Column("media", Text, nullable=True)
    category_id = Column(
        Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, index=True
    )
    # Relationships
    # One-to-Many
    reviews = Relationship("ProductReviews", back_populates="products", passive_deletes=True)
    # One-to-One
    inventory = Relationship("Inventory", back_populates="products", uselist=False)


class Inventory(IntegerBase, Base):
    """The Inventory Model
    
    This is a one-to-one relationship with the Product model.
        - A product can only have one inventory
        - An inventory can only belong to one product

    Relationships:
        - Product
    Fields:
        - quantity -> refers to the quantity of the inventory product
        - status -> refers to the status of the inventory product
        - price -> refers to the purchase price of the inventory product

    """
    # Metadata
    __tablename__ = "inventory"
    # Fields
    quantity = Column("quantity", Integer, nullable=False)
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    status = Column("status", String(255), nullable=False )
    price = Column("price", Float, nullable=False)

    # Relationships
    


class User(IntegerBase, Base):
    """The User Model
    
    The User model represent three types of users:
        - Customer
        - Staff
        - Admin
    
    Each user type has its the following characteristics:
        * email, username and password
        * type of user
        * flag to indicate that the user needs to reset their password
        * flag to indicate that the user is verified
        * status of the user
        * flag to indicate if two factor authentication is enabled
        * two factor authentication secret
        * flags to indicate the user sign in is via github, google or microsoft
    
    Relationships:
        - Orders
        - User Profile
        - Addresses
        - Product Reviews
    """
    # Metadata
    __tablename__ = "users"
    
    # Fields
    username = Column("username", String(255), nullable=False, unique=True)
    password = Column("password", String(255), nullable=False)
    email = Column("email", String(255), nullable=False, unique=True)
    user_type = Column(
        "user_type", Enum(f"{UserTypes.ADMIN.value}",f"{UserTypes.CUSTOMER.value}", f"{UserTypes.STAFF.value}", name="user_type", create_type=False), nullable=False, default=UserTypes.CUSTOMER.value
    )
    force_password_reset = Column(
        "force_password_reset", Boolean, nullable=False, default=False
    )
    user_status = Column(
        "user_status", Enum(f"{UserStatus.ACTIVE.value}",f"{UserStatus.INACTIVE.value}", f"{UserStatus.BANNED.value}", f"{UserStatus.DELETED.value}",name="user_status", create_type=False), nullable=False, default=UserStatus.INACTIVE
    )
    two_fa_enabled = Column("two_fa_enabled", Boolean, nullable=False, default=False)
    two_fa_secret = Column("two_fa_secret", String(255), nullable=False)
    is_github_login = Column("is_github_login", Boolean, nullable=False, default=False)
    is_google_login = Column("is_google_login", Boolean, nullable=False, default=False)
    is_microsoft_login = Column("is_microsoft_login", Boolean, nullable=False, default=False) 

    # Relationships
    # One-to-One
    user_profile = Relationship("UserProfile", back_populates="user", passive_deletes=True, uselist=False)
    # One-to-Many


    def __repr__(self):
        return f"{self.__class__.__name__}: {self.username}(type={self.user_type}, id={self.id})"


class UserProfile(IntegerBase, Base):
    """The User Profile Model
    
    This is a one-to-one relationship with the User model.
        - A user can only have one user profile
        - A user profile can only belong to one user
    
    Relationships:
        - User
        - Addresses
        - Orders
        - Product Reviews
        - WishList
    
    Fields:
        - first_name
        - last_name
        - phone_number
        - is_verified
        - avatar

    """
    # Metadata
    __tablename__ = "user_profiles"
    # Fields
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True, unique=True
    )
    first_name = Column("first_name", String(255), nullable=False)
    last_name = Column("last_name", String(255), nullable=False)
    phone_number = Column("phone_number", String(255), nullable=False)
    is_verified = Column("is_verified", Boolean, nullable=False, default=False)
    avatar = Column("avatar", String(255), nullable=True)
    # Relationships
    # One-to-Many
    addresses = Relationship("Address", back_populates="user_profiles", passive_deletes=True)
    orders = Relationship("Order", back_populates="user_profiles", passive_deletes=True)
    reviews = Relationship("ProductReviews", back_populates="user_profiles", passive_deletes=True)
    wishlist = Relationship("WishList", back_populates="user_profiles", passive_deletes=True)

    # One-to-One
    user = Relationship("User", back_populates="user_profiles", uselist=False)
    cart = Relationship("Cart", back_populates="user_profiles", passive_deletes=True, uselist=False)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.first_name} {self.last_name}(type={self.user_type}, id={self.id})"


class Address(IntegerBase, Base):
    """The Address Model
    This is a one-to-many relationship with the User model.
        - A user can have multiple addresses
        - An address can only belong to one user
    """
    # Metadata
    __tablename__ = "addresses"
    # Fields
    user_profile_id = Column(
        Integer, ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    street = Column("street", String(255), nullable=False)
    city = Column("city", String(255), nullable=False)
    zipcode = Column("zipcode", String(255), nullable=False)
    # Relationships
    # One-to-Many
    user_profile = Relationship("UserProfile", back_populates="addresses")

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.user_profile.first_name} {self.user_profile.last_name}(address_id(id)={self.id})"


class ProductReviews(IntegerBase, Base):
    """The Product Reviews Model
    This is a one-to-many relationship with the Product model.
        - A product can have multiple reviews
        - A review can only belong to one product
        - A review can only belong to one user
    """
    # Metadata
    __tablename__ = "product_reviews"
    # Fields
    user_id = Column(
        Integer, ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    heading = Column("heading", String(255), nullable=False)
    description = Column("description", Text, nullable=True)
    rating = Column("rating", Float, nullable=False)
    media = Column("media", Text, nullable=True)

    # Relationships
    # One-to-Many
    user_profiles = Relationship("UserProfile", back_populates="reviews")
    products = Relationship("Product", back_populates="reviews")


class WishList(IntegerBase, Base):
    # Metadata
    __tablename__ = "wishlists"
    # Fields
    user_id = Column(
        Integer, ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name = Column("name", String(255), nullable=False)


class Cart(IntegerBase, Base):
    """The Cart Model
    
    This is a one-to-many relationship with the User model.
        - A user can have multiple carts
        - A cart can only belong to one user
    
    The 'is_converted' flag is used to indicate that the cart has been converted to an order.

    The 'subtotal', 'tax' and 'total' fields are calculated when the cart is converted to an order.

    """
    # Metadata
    __tablename__ = "carts"
    # Fields
    user_id = Column(
        Integer, ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    is_converted = Column("is_converted", Boolean, nullable=False, default=False)
    subtotal = Column("subtotal", Float, nullable=False)
    tax = Column("tax", Float, nullable=False)
    total = Column("total", Integer, nullable=False)

    # Relationships


class CartItem(IntegerBase, Base):
    # Metadata
    __tablename__ = "cart_items"
    # Fields
    cart_id = Column(
        Integer, ForeignKey("carts.id", ondelete="CASCADE"), nullable=False, index=True
    )
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    quantity = Column("quantity", Float, nullable=False)
    coupon = Column("coupon", String(255), nullable=True)
    discount = Column("discount", Float, nullable=True)

    # Relationships



class Order(UUIDBase, Base):
    """The Order Model
    This is a one-to-many relationship with the User model.
        - An order can only belong to one user
        - A user can have multiple orders
    """

    # Metadata
    __tablename__ = "orders"
    # Fields
    user_id = Column(
        Integer, ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    # Relationships
    user = Relationship("UserProfile", back_populates="orders")

    def __repr__(self):
        return f"{self.__class__.__name__}: Order Id:{self.id}"




class Payment(IntegerBase,Base):
    # Metadata
    __tablename__ = "payments"
    # Fields
    user_id = Column(
        Integer, ForeignKey("user_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    order_id = Column(
        UUID, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True
    )
    total = Column("total", Float, nullable=False)

    # Relationships