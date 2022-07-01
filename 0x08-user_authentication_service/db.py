#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


valid_fields = [
    "id",
    "email",
    "hashed_password",
    "session_id",
    "reset_token"
]


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Generates a new session if not exist
            Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """saves an new user to the database and return it
        """
        new_user = User()

        new_user.email = email
        new_user.hashed_password = hashed_password

        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """takes in arbitrary keyword arguments
            and returns the first row found in the users table
            as filtered by the method’s input arguments
        """
        if not kwargs:
            raise InvalidRequestError

        for k in kwargs.keys():
            if k not in valid_fields:
                raise InvalidRequestError

        result = self._session.query(User).filter_by(**kwargs).first()

        if not result:
            raise NoResultFound

        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates an user in the database
        """
        user = self.find_user_by(id=user_id)

        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError

            setattr(user, k, v)

        self._session.commit()
