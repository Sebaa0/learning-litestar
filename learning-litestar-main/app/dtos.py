from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import Accommodation, Transport, Activity, Expense, City, Travel, User


# Accommodation DTOs
class AccommodationReadDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "city", "expenses"})

class AccommodationReadFullDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"city_id"})

class AccommodationCreateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city", "expenses"})

class AccommodationUpdateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city", "expenses"}, partial=True)


# Transport DTOs
class TransportReadDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "start_city", "end_city", "expenses"})

class TransportCreateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "start_city", "end_city", "expenses"})

class TransportUpdateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "start_city", "end_city", "expenses"}, partial=True)


# Activity DTOs
class ActivityReadDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "city", "expenses"})

class ActivityReadFullDTO(SQLAlchemyDTO[Activity]):
    pass

class ActivityCreateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city", "expenses"})

class ActivityUpdateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city", "expenses"}, partial=True)


# Expense DTOs
class ExpenseReadDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "user"})

class ExpenseCreateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "user", "accommodation", "transport", "activity"})

class ExpenseUpdateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "user", "accommodation", "transport", "activity"}, partial=True)


# City DTOs
class CityReadDTO(SQLAlchemyDTO[City]):
   pass


class CityCreateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id"})


class CityUpdateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)


# Travel DTOs
class TravelReadDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"users", "accommodations", "transports", "activities", "expenses"})


class TravelCreateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id", "users", "accommodations", "transports", "activities", "expenses"})


class TravelUpdateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id", "users", "accommodations", "transports", "activities", "expenses"}, partial=True)


# User DTOs
class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"travels", "expenses"})


class UserCreateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travels", "expenses"})


class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travels", "expenses"}, partial=True)
