"""
Scripts to run to set up our database
"""

from model import db, SavedTotal


# Create the database tables for our model
db.connect()
db.drop_tables([SavedTotal])
db.create_tables([SavedTotal])


