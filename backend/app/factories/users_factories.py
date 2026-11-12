from faker import Factory, Faker
from app.models import Users
from app.models.base import SessionLocal

faker = Faker('fr_FR')


class UserFactory():
    value_wallet = 1
    def __init__(self):
        self.last_name = faker.last_name()
        self.first_name= faker.first_name()
        self.nick_name=faker.user_name()
        UserFactory.value_wallet += 1
        self.id_wallet= UserFactory.value_wallet + 1
    
    

def createUsersFactory(nb: int):
    with SessionLocal() as session:
        for i in range(1, nb):
            userFake = UserFactory()
            user = Users(
                last_name=userFake.last_name,
                first_name=userFake.first_name,
                nick_name=userFake.nick_name,
                id_wallet=userFake.id_wallet
            )
            session.add(user)
        session.commit()
