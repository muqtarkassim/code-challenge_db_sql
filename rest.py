from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Restaurant and Customer
restaurant_customer_association = Table(
    'restaurant_customer_association',
    Base.metadata,
    Column('restaurant_id', Integer, ForeignKey('restaurants.id')),
    Column('customer_id', Integer, ForeignKey('customers.id'))
)

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary=restaurant_customer_association, back_populates='restaurants')

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary=restaurant_customer_association, back_populates='customers')

# Create SQLite database in memory (replace 'sqlite:///:memory:' with your database URL)
engine = create_engine('sqlite:///:resturant')
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
restaurant1 = Restaurant(name='Restaurant 1')
restaurant2 = Restaurant(name='Restaurant 2')
customer1 = Customer(name='Customer 1')
customer2 = Customer(name='Customer 2')

# Establishing relationships
restaurant1.customers.append(customer1)
restaurant1.customers.append(customer2)
customer1.restaurants.append(restaurant2)

# Adding objects to the session
session.add_all([restaurant1, restaurant2, customer1, customer2])

# Committing changes to the database
session.commit()

# Querying data
print("Restaurants for Customer 1:")
for restaurant in customer1.restaurants:
    print(restaurant.name)

print("\nCustomers for Restaurant 1:")
for customer in restaurant1.customers:
    print(customer.name)
