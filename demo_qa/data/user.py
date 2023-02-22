import datetime
from dataclasses import dataclass
from typing import Literal


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birthday: datetime.date
    hobbies: str
    subject: Literal['Accounting', 'Arts', 'Biology', 'Chemistry', 'Civics', 'Commerce', 'Computer Science',
                      'Economics', 'English', 'Hindi', 'History', 'Maths', 'Physics', 'Social Studies']
    picture: str
    address: str
    state: Literal['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city: Literal['Delhi', 'Gurgaon', 'Noida', 'Agra', 'Lucknow', 'Merrut', 'Karnal', 'Panipat', 'Jaipur', 'Jaiselmer']


Sponge_Bob = User(
    first_name='Sponge',
    last_name='Bob',
    email='test@mail.com',
    gender='Male',
    phone_number='0123456789',
    birthday=datetime.date(1999, 2, 17),
    hobbies='Music',
    subject='Civics',
    picture='more.jpg',
    address='Ocean st',
    state='Uttar Pradesh',
    city='Lucknow')