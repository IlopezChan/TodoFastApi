from abc import ABC, abstractmethod
from app.shared.base.BaseRepository import BaseRepository

class BaseInteractor():

    def get_all(self, repository): pass

    def get(self, id:int, repository): pass

    def create(self, requestBody, repository): pass

    def update(self, requestBody, id: int, repository): pass

    def delete(self, id: int, repository): pass

    