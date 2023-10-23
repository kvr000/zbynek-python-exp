from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from app.db.database import Database

class AppConfig(containers.DeclarativeContainer):
    db_name = "hello"


@inject
class DbContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        packages=[
            "app",
        ],
    )

    database: providers.Factory[Database] = providers.Factory(Database, db_name=AppConfig.db_name)


@inject
class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        packages=[
            "app",
        ],
    )

    db_container: DbContainer = providers.Container(DbContainer)
