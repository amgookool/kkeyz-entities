# Create an enum for the status of the user
from enum import Enum


class UserTypes(Enum):
    STAFF = "STAFF"
    CUSTOMER = "CUSTOMER"
    ADMIN = "ADMIN"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other


class ProductTypes(Enum):
    KEYBOARDS = "KEYBOARDS"
    MOUSES = "MOUSES"
    KEYBOARD_SWITCHES = "KEYBOARD_SWITCHES"
    CPUS = "CPUS"
    MOTHERBOARDS = "MOTHERBOARDS"
    GRAPHICS_CARDS = "GRAPHICS_CARDS"
    RAM = "RAM"
    STORAGE = "STORAGE"
    POWER_SUPPLIES = "POWER_SUPPLIES"
    MICROPHONES = "MICROPHONES"
    COOLING = "COOLING"
    OTHER = "OTHER"
    MONITORS = "MONITORS"
    HEADPHONES = "HEADPHONES"

    def __str__(self):
        return self.value

    def __repr__(self):
        if self.value.find("_") == -1:
            return self.value.lower().capitalize()
        else:
            temp = ""
            split_spaced_text = self.value.replace("_", " ").split()
            for text in split_spaced_text:
                t = text.lower().capitalize()
                temp += t + " "
            return temp

    def __eq__(self, other):
        return self.value == other


class UserPermissions(Enum):
    VIEW_CLIENT_USERS = "VIEW_CUSTOMER_USERS"
    VIEW_STAFF_USERS = "VIEW_STAFF_USERS"
    VIEW_PRODUCTS = "VIEW_PRODUCTS"
    VIEW_ORDERS = "VIEW_ORDERS"
    VIEW_PAYMENTS = "VIEW_PAYMENTS"
    VIEW_ANALYTICS = "VIEW_ANALYTICS"
    VIEW_REQUESTS = "VIEW_REQUESTS"

    CREATE_CLIENT_USER = "CREATE_CUSTOMER_USER"
    CREATE_STAFF_USER = "CREATE_STAFF_USER"
    CREATE_PRODUCT = "CREATE_PRODUCT"
    CREATE_ORDER = "CREATE_ORDER"
    CREATE_PAYMENT = "CREATE_PAYMENT"
    CREATE_ANALYTIC = "CREATE_ANALYTIC"
    CREATE_REQUEST = "CREATE_REQUEST"

    UPDATE_CLIENT_USERS = "UPDATE_CUSTOMER_USERS"
    UPDATE_STAFF_USERS = "UPDATE_STAFF_USERS"
    UPDATE_PRODUCTS = "UPDATE_PRODUCTS"
    UPDATE_ORDERS = "UPDATE_ORDERS"
    UPDATE_PAYMENTS = "UPDATE_PAYMENTS"
    UPDATE_ANALYTICS = "UPDATE_ANALYTICS"
    UPDATE_REQUESTS = "UPDATE_REQUESTS"

    DELETE_CLIENT_USERS = "DELETE_CUSTOMER_USERS"
    DELETE_STAFF_USERS = "DELETE_STAFF_USERS"
    DELETE_PRODUCTS = "DELETE_PRODUCTS"
    DELETE_ORDERS = "DELETE_ORDERS"
    DELETE_PAYMENTS = "DELETE_PAYMENTS"
    DELETE_ANALYTICS = "DELETE_ANALYTICS"
    DELETE_REQUESTS = "DELETE_REQUESTS"

    def __repr__(self):
        if (self.value.find("_") == -1):
            return self.value.lower().capitalize()
        else:
            temp = ""
            split_spaced_text = self.value.replace("_", " ").split()
            for text in split_spaced_text:
                t = text.lower().capitalize()
                temp += t + " "
            return temp

class UserStatus(Enum):
    ACTIVE = "ACTIVE"  # represents a logged in user (mainly for the admin)
    INACTIVE = "INACTIVE"  # represents a logged in user (mainly for the admin)
    BANNED = "BANNED"  # represents a banned customer
    DELETED = "DELETED"  # represents a deleted customer
    # SUSPENDED = 'SUSPENDED' # represents a suspended customer
    # UNCONFIRMED = 'UNCONFIRMED' # represents an unconfirmed customer
    # CONFIRMED = 'CONFIRMED' # represents a confirmed customer
    # EXPIRED = 'EXPIRED' # represents an expired customer
    # EXPIRING = 'EXPIRING' # represents an expiring customer
    # EXPIRING_SOON = 'EXPIRING_SOON' # represents an expiring soon customer
    # EXPIRED_SOON = 'EXPIRED_SOON' # represents an expired soon customer
    # NEW = 'NEW' # represents a new customer

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other


class OrderStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other


class PaymentStatus(Enum):
    PAID = "PAID"
    UNPAID = "UNPAID"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other


class ProductStatus(Enum):
    IN_STOCK = "IN_STOCK"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    RESTOCKING = "RESTOCKING"
    RESTOCKING_SOON = "RESTOCKING_SOON"
    NEW = "NEW"
    DISCONTINUED = "DISCONTINUED"

    def __str__(self):
        return self.value

    def __repr__(self):
        if (self.value.find("_") == -1):
            return self.value.lower().capitalize()
        else:
            temp = ""
            split_spaced_text = self.value.replace("_", " ").split()
            for text in split_spaced_text:
                t = text.lower().capitalize()
                temp += t + " "
            return temp
    def __eq__(self, other):
        return self.value == other