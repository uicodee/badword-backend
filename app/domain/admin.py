import asyncio

from app.api.dependencies import AuthProvider
from app.config import load_config
from app.infrastructure.database.dao import HolderDao
from app.infrastructure.database.factory import create_pool, make_connection_string


async def main():
    settings = load_config()
    auth_provider = AuthProvider(settings)
    firstname = input(">> Enter firstname: ")
    lastname = input(">> Enter lastname: ")
    email = input(">> Enter email: ")
    password = input(">> Enter password: ")
    pool = create_pool(url=make_connection_string(settings=settings))
    async with pool() as session:
        dao = HolderDao(session=session)
        await dao.user.add_user(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=auth_provider.get_password_hash(password=password),
        )


if __name__ == "__main__":
    asyncio.run(main())
