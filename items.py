from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

admin = User(name="Hayden Colson", email="colsoncode@gmail.com",
             picture="https://www.facebook.com/photo.php?fbid=761611290681005&l=f7be698461")
session.add(admin)
session.commit()

category1 = Category(user_id=1, name="Programming Languages")
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Python", category=category1)
session.add(item1)
session.commit()

print "added first items!"
