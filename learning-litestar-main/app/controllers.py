import select
from typing import Sequence

from advanced_alchemy.exceptions import NotFoundError
from advanced_alchemy.filters import CollectionFilter
from litestar import Controller, delete, get, patch, post
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException

from app.dtos import (
    UserCreateDTO,
    UserReadDTO,
    UserUpdateDTO,
    TravelCreateDTO,
    TravelReadDTO,
    TravelUpdateDTO,
    AccommodationCreateDTO,
    AccommodationReadDTO,
    AccommodationReadFullDTO,
    AccommodationUpdateDTO,
    TransportCreateDTO,
    TransportReadDTO,
    TransportUpdateDTO,
    ActivityCreateDTO,
    ActivityReadDTO,
    ActivityReadFullDTO,
    ActivityUpdateDTO,
    ExpenseCreateDTO,
    ExpenseReadDTO,
    ExpenseUpdateDTO,
    CityCreateDTO,
    CityReadDTO,
    CityUpdateDTO,
)
from app.models import User, Travel, Accommodation, Transport, Activity, Expense, City
from app.repositories import (
    UserRepository,
    TravelRepository,
    AccommodationRepository,
    TransportRepository,
    ActivityRepository,
    ExpenseRepository,
    CityRepository,
    provide_user_repo,
    provide_travel_repo,
    provide_accommodation_repo,
    provide_transport_repo,
    provide_activity_repo,
    provide_expense_repo,
    provide_city_repo,
)

class UserController(Controller):
    path = "/users"
    tags = ["users"]
    return_dto = UserReadDTO
    dependencies = {"user_repo": provide_user_repo}

    @get()
    async def list_users(self, user_repo: UserRepository) -> list[User]:
        return user_repo.list()

    @get("/{user_id:int}")
    async def get_user(self, user_repo: UserRepository, user_id: int) -> User:
        try:
            return user_repo.get(user_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e

    @post(dto=UserCreateDTO)
    async def add_user(self, user_repo: UserRepository, data: User) -> User:
        return user_repo.add(data)

    @patch("/{user_id:int}", dto=UserUpdateDTO)
    async def update_user(self, user_repo: UserRepository, user_id: int, data: DTOData[User]) -> User:
        try:
            user, _ = user_repo.get_and_update(id=user_id, **data.as_builtins(), match_fields=["id"])
            return user
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e

    @delete("/{user_id:int}")
    async def delete_user(self, user_repo: UserRepository, user_id: int) -> None:
        try:
            user_repo.delete(user_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e

class AccommodationController(Controller):
    path = "/accommodations"
    tags = ["accommodations"]
    dependencies = {"accommodation_repo": provide_accommodation_repo}
    return_dto = AccommodationReadDTO

    @get()
    async def list_accommodations(
        self, accommodation_repo: AccommodationRepository
    ) -> Sequence[Accommodation]:
        return accommodation_repo.list()

    @get("/{accommodation_id:int}", dto=AccommodationReadFullDTO)
    async def get_accommodation(
        self, accommodation_repo: AccommodationRepository, accommodation_id: int
    ) -> Accommodation:
        try:
            return accommodation_repo.get(accommodation_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e

    @post(dto=AccommodationCreateDTO)
    async def add_accommodation(
        self, accommodation_repo: AccommodationRepository, data: Accommodation
    ) -> Accommodation:
        return accommodation_repo.add(data)

    @patch("/{accommodation_id:int}", dto=AccommodationUpdateDTO)
    async def update_accommodation(
        self,
        accommodation_repo: AccommodationRepository,
        accommodation_id: int,
        data: DTOData[Accommodation],
    ) -> Accommodation:
        try:
            accommodation, _ = accommodation_repo.get_and_update(
                id=accommodation_id, **data.as_builtins(), match_fields=["id"]
            )
            return accommodation
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e

    @delete("/{accommodation_id:int}")
    async def delete_accommodation(
        self, accommodation_repo: AccommodationRepository, accommodation_id: int
    ) -> None:
        try:
            accommodation_repo.delete(accommodation_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e

class TransportController(Controller):
    path = "/transports"
    tags = ["transports"]
    dependencies = {"transport_repo": provide_transport_repo}
    return_dto = TransportReadDTO

    @get()
    async def list_transports(
        self, transport_repo: TransportRepository
    ) -> Sequence[Transport]:
        return transport_repo.list()

    @get("/{transport_id:int}")
    async def get_transport(
        self, transport_repo: TransportRepository, transport_id: int
    ) -> Transport:
        try:
            return transport_repo.get(transport_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transport_id} no encontrado") from e

    @post(dto=TransportCreateDTO)
    async def add_transport(
        self, transport_repo: TransportRepository, data: Transport
    ) -> Transport:
        return transport_repo.add(data)

    @patch("/{transport_id:int}", dto=TransportUpdateDTO)
    async def update_transport(
        self,
        transport_repo: TransportRepository,
        transport_id: int,
        data: DTOData[Transport],
    ) -> Transport:
        try:
            transport, _ = transport_repo.get_and_update(
                id=transport_id, **data.as_builtins(), match_fields=["id"]
            )
            return transport
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transport_id} no encontrado") from e

    @delete("/{transport_id:int}")
    async def delete_transport(
        self, transport_repo: TransportRepository, transport_id: int
    ) -> None:
        try:
            transport_repo.delete(transport_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transport_id} no encontrado") from e

class ActivityController(Controller):
    path = "/activities"
    tags = ["activities"]
    dependencies = {"activity_repo": provide_activity_repo}
    return_dto = ActivityReadDTO

    @get()
    async def list_activities(
        self, activity_repo: ActivityRepository
    ) -> Sequence[Activity]:
        return activity_repo.list()

    @get("/{activity_id:int}", dto=ActivityReadFullDTO)
    async def get_activity(
        self, activity_repo: ActivityRepository, activity_id: int
    ) -> Activity:
        try:
            return activity_repo.get(activity_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Actividad {activity_id} no encontrada") from e

    @post(dto=ActivityCreateDTO)
    async def add_activity(
        self, activity_repo: ActivityRepository, data: Activity
    ) -> Activity:
        return activity_repo.add(data)

    @patch("/{activity_id:int}", dto=ActivityUpdateDTO)
    async def update_activity(
        self,
        activity_repo: ActivityRepository,
        activity_id: int,
        data: DTOData[Activity],
    ) -> Activity:
        try:
            activity, _ = activity_repo.get_and_update(
                id=activity_id, **data.as_builtins(), match_fields=["id"]
            )
            return activity
        except NotFoundError as e:
            raise NotFoundException(detail=f"Actividad {activity_id} no encontrada") from e

    @delete("/{activity_id:int}")
    async def delete_activity(
        self, activity_repo: ActivityRepository, activity_id: int
    ) -> None:
        try:
            activity_repo.delete(activity_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Actividad {activity_id} no encontrada") from e

class ExpenseController(Controller):
    path = "/expenses"
    tags = ["expenses"]
    dependencies = {"expense_repo": provide_expense_repo}
    return_dto = ExpenseReadDTO

    @post(dto=ExpenseCreateDTO)
    async def add_expense(
        self, expense_repo: ExpenseRepository, data: Expense
    ) -> Expense:
        return expense_repo.add(data)
    
    @get("/{expense_id:int}")
    async def get_expense(
        self, expense_repo: ExpenseRepository, expense_id: int
    ) -> Expense:
        try:
            return expense_repo.get(expense_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e

    @patch("/{expense_id:int}", dto=ExpenseUpdateDTO)
    async def update_expense(
        self,
        expense_repo: ExpenseRepository,
        expense_id: int,
        data: DTOData[Expense],
    ) -> Expense:
        try:
            expense, _ = expense_repo.get_and_update(
                id=expense_id, **data.as_builtins(), match_fields=["id"]
            )
            return expense
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e

    @delete("/{expense_id:int}")
    async def delete_expense(
        self, expense_repo: ExpenseRepository, expense_id: int
    ) -> None:
        try:
            expense_repo.delete(expense_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e

class CityController(Controller):
    path = "/cities"
    tags = ["cities"]
    dependencies = {"city_repo": provide_city_repo}
    return_dto = CityReadDTO

    @get()
    async def list_cities(self, city_repo: CityRepository) -> list[City]:
        return city_repo.list()

    @post(dto=CityCreateDTO)
    async def create_city(self, city_repo: CityRepository, data: City) -> City:
        return city_repo.add(data)

    @patch("/{city_id:int}", dto=CityUpdateDTO)
    async def update_city(self, city_repo: CityRepository, city_id: int, data: DTOData[City]) -> City:
        try:
            city, _ = city_repo.get_and_update(id=city_id, **data.as_builtins(), match_fields=["id"])
            return city
        except NotFoundError as e:
            raise NotFoundException(detail=f"Ciudad {city_id} no encontrada") from e
        
    @delete("/{city_id:int}")
    async def delete_city(self, city_repo: CityRepository, city_id: int) -> None:
        city_repo.delete(city_id)

class TravelController(Controller):
    path = "/travels"
    tags = ["travels"]
    dependencies = {
        "travel_repo": provide_travel_repo,
        "user_repo": provide_user_repo,
        "accommodation_repo": provide_accommodation_repo,
        "transport_repo": provide_transport_repo,
        "activity_repo": provide_activity_repo,
        "expense_repo": provide_expense_repo
    }

    @get("/", return_dto = TravelReadDTO)
    async def list_travels(self, travel_repo: TravelRepository) -> list[Travel]:
        return travel_repo.list()

    @get("/{travel_id:int}", return_dto = TravelReadDTO)
    async def get_travel(self, travel_repo: TravelRepository, travel_id: int) -> Travel:
        try:
            return travel_repo.get(travel_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

    @post("/", dto=TravelCreateDTO, return_dto = TravelCreateDTO)
    async def add_travel(self, travel_repo: TravelRepository, data: Travel) -> Travel:
        return travel_repo.add(data)

    @patch("/{travel_id:int}", dto=TravelUpdateDTO)
    async def update_travel(self, travel_repo: TravelRepository, travel_id: int, data: DTOData[Travel]) -> Travel:
        try:
            travel, _ = travel_repo.get_and_update(id=travel_id, **data.as_builtins(), match_fields=["id"])
            return travel
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

    @delete("/{travel_id:int}", return_dto = TravelReadDTO)
    async def delete_travel(self, travel_repo: TravelRepository, travel_id: int) -> None:
        try:
            travel_repo.delete(travel_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

    @get("/{travel_id:int}/users", return_dto = UserReadDTO)
    async def get_travel_users(self, travel_repo: TravelRepository, travel_id: int) -> list[User]:
        try:
            travel = travel_repo.get(travel_id)
            return travel.users
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} o usuarios no encontrados") from e

    @post("/{travel_id:int}/users", return_dto=TravelReadDTO)
    async def add_travel_users(
        self,
        travel_repo: TravelRepository,
        user_repo: UserRepository,
        travel_id: int,
        user_ids: list[int]
    ) -> Travel:
        try:
            # Verificar la existencia del viaje
            travel = travel_repo.get(travel_id)
            
            # Verificar la existencia de los usuarios
            existing_users = user_repo.list(CollectionFilter(field_name="id", values=user_ids))
            existing_user_ids = {user.id for user in existing_users}
            missing_user_ids = set(user_ids) - existing_user_ids

            if missing_user_ids:
                raise NotFoundException(detail=f"Usuarios con IDs {', '.join(map(str, missing_user_ids))} no encontrados")

            # Verificar si el usuario ya está asociado al viaje
            existing_user_ids_in_travel = {user.id for user in travel.users}
            new_users = [user for user in existing_users if user.id in user_ids and user.id not in existing_user_ids_in_travel]

            if new_users:
                travel.users.extend(new_users)
                travel_repo.update(travel)
            
            return travel

        except NotFoundError as e:
            # Si el viaje no se encuentra, lanzar una excepción específica
            raise NotFoundException(detail=f"Viaje con ID {travel_id} no encontrado") from e

    @delete("/{travel_id:int}/users/{user_id:int}", return_dto = TravelReadDTO)
    async def remove_travel_user(self, travel_repo: TravelRepository, travel_id: int, user_id: int) -> None:
        try:
            travel = travel_repo.get(travel_id)
            user = next(user for user in travel.users if user.id == user_id)
            travel.users.remove(user)
            travel_repo.update(travel)
        except (NotFoundError, StopIteration) as e:
            raise NotFoundException(detail=f"Viaje {travel_id} o usuario {user_id} no encontrado") from e

    @get("/{travel_id:int}/accommodations", return_dto = AccommodationReadDTO)
    async def list_travel_accommodations(self, accommodation_repo: AccommodationRepository, travel_id: int) -> list[Accommodation]:
        accommodations = accommodation_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))
        if not accommodations:
            raise NotFoundException(detail=f"No accommodations found for travel ID {travel_id}")
        return accommodations

    @get("/{travel_id:int}/transports", return_dto = TransportReadDTO)
    async def list_travel_transports(self, transport_repo: TransportRepository, travel_id: int) -> list[Transport]:
        transport = transport_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))
        if not transport:
            raise NotFoundException(detail=f"No transport found for travel ID {travel_id}")
        return transport

    @get("/{travel_id:int}/activities", return_dto = ActivityReadDTO)
    async def list_travel_activities(self, activity_repo: ActivityRepository, travel_id: int) -> list[Activity]:
        activity = activity_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))
        if not activity:
            raise NotFoundException(detail=f"No activity found for travel ID {travel_id}")
        return activity
    
    @get("/{travel_id:int}/expenses", return_dto = ExpenseReadDTO)
    async def list_travel_expenses(self, expense_repo: ExpenseRepository, travel_id: int) -> list[Expense]:
        expense = expense_repo.list(CollectionFilter(field_name="travel_id", values=[travel_id]))
        if not expense:
            raise NotFoundException(detail=f"No expense found for travel ID {travel_id}")
        return expense
    