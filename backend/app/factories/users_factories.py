from faker import Factory, Faker
from app.models import Users
from app.models.base import SessionLocal
from app.auth.auth import create_user

faker = Faker('fr_FR')


class UserFactory():
    def __init__(self):
        self.last_name = faker.last_name()
        self.first_name= faker.first_name()
        self.nick_name=faker.user_name()
        self.email = faker.email()
    
    

def createUsersFactory(nb: int):
    with SessionLocal() as session:
        for i in range(1, nb):
            userFake = UserFactory()
            user = create_user(userFake.first_name,userFake.last_name,userFake.nick_name, userFake.email, 'password')
