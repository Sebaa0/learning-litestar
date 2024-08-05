from datetime import date
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    travels: Mapped[list["Travel"]] = relationship("Travel", secondary="users_travels", back_populates="users")
    expenses: Mapped[list["Expense"]] = relationship("Expense", back_populates="user")


class Travel(Base):
    __tablename__ = "travels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    start_date: Mapped[date]
    end_date: Mapped[date]

    accommodations: Mapped[list["Accommodation"]] = relationship("Accommodation", back_populates="travel")
    transports: Mapped[list["Transport"]] = relationship("Transport", back_populates="travel")
    activities: Mapped[list["Activity"]] = relationship("Activity", back_populates="travel")
    expenses: Mapped[list["Expense"]] = relationship("Expense", back_populates="travel")
    users: Mapped[list["User"]] = relationship("User", secondary="users_travels", back_populates="travels")


class Accommodation(Base):
    __tablename__ = "accommodations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    location: Mapped[str]
    price: Mapped[int]
    start_date: Mapped[date]
    end_date: Mapped[date]
    observations: Mapped[Optional[str]]

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    travel_id:Mapped[int] = mapped_column(ForeignKey("travels.id"))

    travel: Mapped["Travel"] = relationship("Travel", back_populates="accommodations")
    city: Mapped["City"] = relationship()


class Transport(Base):
    __tablename__ = "transport"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    company: Mapped[str]
    price: Mapped[int]
    start_date: Mapped[date]
    start_location: Mapped[str]
    end_date: Mapped[date]
    end_location: Mapped[str]

    start_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    end_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))

    travel: Mapped["Travel"] = relationship("Travel", back_populates="transports")
    start_city: Mapped["City"] = relationship("City", foreign_keys=[start_city_id])
    end_city: Mapped["City"] = relationship("City", foreign_keys=[end_city_id])


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    location: Mapped[str]
    start_datetime: Mapped[date]
    price: Mapped[int]
    duration: Mapped[int]

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))

    travel: Mapped["Travel"] = relationship("Travel", back_populates="activities")
    city: Mapped["City"] = relationship()


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    amount: Mapped[int]
    datetime: Mapped[date]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))

    user: Mapped["User"] = relationship("User", back_populates="expenses")
    travel: Mapped["Travel"] = relationship("Travel", back_populates="expenses")

class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    country: Mapped[str]

    #accommodations: Mapped[list["Accommodation"]] = relationship("Accommodation", back_populates="city")
    #activities: Mapped[list["Activity"]] = relationship("Activity", back_populates="city")
    #start_transports: Mapped[list["Transport"]] = relationship("Transport", foreign_keys=[Transport.start_city_id])
    #end_transports: Mapped[list["Transport"]] = relationship("Transport", foreign_keys=[Transport.end_city_id])

class UsersTravels(Base):
    __tablename__ = "users_travels"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), primary_key=True)