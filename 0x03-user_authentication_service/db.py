#!/usr/bin/env python3
"""
create user
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add user to database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find User"""
        key, value = kwargs.popitem()
        if not hasattr(User, key):
            raise InvalidRequestError
        column = getattr(User, key)
        try:
            return self.__session.query(User).filter(column== value).one()
        except NoResultFound:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user"""
        user = self.find_user_by(id=user_id)
        key, value = kwargs.popitem()

        if not hasattr(user, key):
            raise ValueError
        setattr(user, key, value)
