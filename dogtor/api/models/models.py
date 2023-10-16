from . import db
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column


class User(db.Model):
    __tablename__ = 'user'

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, unique=True, nullable=False)
    email = mapped_column(String, unique=True)


class Owner(db.Model):
    __tablename__ = 'owner'
    """Pet owner object"""

    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(length=50))
    last_name = db.Column(String(length=50))
    phone = db.Column(String(length=15))
    mobile = db.Column(String(length=15))
    email = db.Column(String)
    pets = db.relationship("Pet", backref="owner")


class Species(db.Model):
    __tablename__ = 'species'
    """Pet species object"""

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))
    pet = db.relationship("Pet", backref="species")


class Pet(db.Model):
    __tablename__ = 'pet'
    """Pet object"""

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))
    owner_id = db.Column(Integer, db.ForeignKey("owner.id"))
    age = db.Column(Integer)
    species_id = db.Column(Integer, db.ForeignKey("species.id"))
    record_id = db.Column(Integer, db.ForeignKey("record.id"))


record_category_m2m = db.Table(
    "record_category",
    db.Column("record_id", Integer, db.ForeignKey("record.id")),
    db.Column("category_id", Integer, db.ForeignKey("category.id")),
)


class Record(db.Model):
    __tablename__ = 'record'
    """Pet record object"""

    id = db.Column(Integer, primary_key=True)
    category = db.Column(String(length=20))
    procedure = db.Column(String(length=255))
    pet = db.relationship("Pet", backref="record")
    date = db.Column(DateTime)
    categories = db.relationship(
        "Category", secondary=record_category_m2m, backref="records"
    )


class Category(db.Model):
    __tablename__ = 'category'
    """Record category object"""

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))
    records = db.relationship(
        "Record", secondary=record_category_m2m, backref="categories"
    )