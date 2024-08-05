from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy.orm import Session

from app.models import Accommodation, Transport, Activity, Expense, City, Travel, User


# Accommodation Repository
class AccommodationRepository(SQLAlchemySyncRepository[Accommodation]):  # type: ignore
    model_type = Accommodation


async def provide_accommodation_repo(db_session: Session) -> AccommodationRepository:
    return AccommodationRepository(session=db_session, auto_commit=True)


# Transport Repository
class TransportRepository(SQLAlchemySyncRepository[Transport]):  # type: ignore
    model_type = Transport


async def provide_transport_repo(db_session: Session) -> TransportRepository:
    return TransportRepository(session=db_session, auto_commit=True)


# Activity Repository
class ActivityRepository(SQLAlchemySyncRepository[Activity]):  # type: ignore
    model_type = Activity


async def provide_activity_repo(db_session: Session) -> ActivityRepository:
    return ActivityRepository(session=db_session, auto_commit=True)


# Expense Repository
class ExpenseRepository(SQLAlchemySyncRepository[Expense]):  # type: ignore
    model_type = Expense


async def provide_expense_repo(db_session: Session) -> ExpenseRepository:
    return ExpenseRepository(session=db_session, auto_commit=True)


# City Repository
class CityRepository(SQLAlchemySyncRepository[City]):  # type: ignore
    model_type = City


async def provide_city_repo(db_session: Session) -> CityRepository:
    return CityRepository(session=db_session, auto_commit=True)


# Travel Repository
class TravelRepository(SQLAlchemySyncRepository[Travel]):  # type: ignore
    model_type = Travel


async def provide_travel_repo(db_session: Session) -> TravelRepository:
    return TravelRepository(session=db_session, auto_commit=True)


# User Repository
class UserRepository(SQLAlchemySyncRepository[User]):  # type: ignore
    model_type = User


async def provide_user_repo(db_session: Session) -> UserRepository:
    return UserRepository(session=db_session, auto_commit=True)
