from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    day: int
    month: str
    year: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


test_user = User(
    first_name='Maksim',
    last_name='Kudaev',
    email='maxim.cudaew@gmail.com',
    gender='Male',
    phone_number='9999999999',
    day=10,
    month='November',
    year='2000',
    subject='English',
    hobby='Sports',
    picture='resources/photo.jpg',
    address='Street fighter',
    state='NCR',
    city='Delhi'
)
