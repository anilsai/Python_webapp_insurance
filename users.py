# Utilized the data from the lotsofmenususer.py as user.py from the
# udacity GitHub repo to populate the database.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Insurance, Base, InsuranceField, User

engine = create_engine('sqlite:///insuranceBritecore.db')
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


# Create dummy user
User1 = User(name="Xarvis", email="abc@xyz.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Insurances for Mr.XYZ
insurance1 = Insurance(user_id=1, name="Inusrance for Mr. XYZ ")

session.add(insurance1)
session.commit()

InsTypeItem1 = InsuranceField(user_id=1, name="Auto", Address="2111 hollyhall",
                     InsuredValue="$700000.00", Type="Auto", insurance=insurance1)

session.add(InsTypeItem1)
session.commit()


InsTypeItem2 = InsuranceField(user_id=1, name="Renters", Address="2111 lincon Dr",
                     InsuredValue="100000.00", Type="Rent", insurance=insurance1)

session.add(InsTypeItem2)
session.commit()

InsTypeItem3 = InsuranceField(user_id=1, name="Prize", Address="spaceship fields",
                     InsuredValue="1000000.00", Type="Prize", insurance=insurance1)

session.add(InsTypeItem3)
session.commit()

InsTypeItem4 = InsuranceField(user_id=1, name="Home", Address="spaceship fields",
                     InsuredValue="1000000.00", Type="Prize", insurance=insurance1)

session.add(InsTypeItem4)
session.commit()




# # Insurances for Mr.ABC
# insurance2 = Insurance(user_id=1, name="Inusrance for Mr. ABC ")

# session.add(insurance1)
# session.commit()

# InsTypeItem1 = InsuranceField(user_id=1, name="Auto", Address="Sonic drive",
#                      InsuredValue="$99000.00", Type="Auto", insurance=insurance2)

# session.add(InsTypeItem1)
# session.commit()


# InsTypeItem2 = InsuranceField(user_id=1, name="Renters", Address="seriously  Dr",
#                      InsuredValue="99999.00", Type="Rent", insurance=insurance2)

# session.add(InsTypeItem2)
# session.commit()

# InsTypeItem3 = InsuranceField(user_id=1, name="Prize", Address="No where",
#                      InsuredValue="9009000.00", Type="Prize", insurance=insurance2)

# session.add(InsTypeItem3)
# session.commit()

# InsTypeItem4 = InsuranceField(user_id=1, name="Prize", Address="apple park",
#                      InsuredValue="343400.00", Type="Home", insurance=insurance2)

# session.add(InsTypeItem4)
# session.commit()

print "added menu items!"
