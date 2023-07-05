import os

import psycopg2
from sqlalchemy import Column, Integer, String, Text, create_engine, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')

ADMINS = os.getenv('ADMINS').split(',')
Base = declarative_base()

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

session = sessionmaker(bind=engine)
session = session()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), unique=True)
    phone = Column(String(32), unique=True)
    answer_1 = Column(String(256))
    answer_2 = Column(Integer, nullable=True)
    answer_3 = Column(nullable=True)
    answer_4 = Column(nullable=True)
    answer_5 = Column(nullable=True)
    answer_6 = Column(Text, nullable=True)
    answer_7 = Column(Text, nullable=True)
    answer_8 = Column(Text, nullable=True)
    answer_9 = Column(Text, nullable=True)
    answer_10 = Column(Text, nullable=True)
    answer_11 = Column(Text, nullable=True)
    answer_12 = Column(Integer, nullable=True)
    answer_13 = Column(Integer, nullable=True)
    answer_14 = Column(Integer, nullable=True)
    answer_15 = Column(Integer, nullable=True)
    answer_16 = Column(Integer, nullable=True)
    answer_17 = Column(nullable=True)
    answer_18 = Column(nullable=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String(64), unique=True)
    username = Column(String(128), unique=True)

    __table_args__ = (
        UniqueConstraint('telegram_id', name='uq_telegram_id'),
        UniqueConstraint('username', name='uq_username')
    )
