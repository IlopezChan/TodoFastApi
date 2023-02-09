from abc import ABC, abstractmethod
from app.shared.base.BaseRepository import BaseRepository

class BaseController():

    def get_all(): pass

    def get(self, id:int): pass

    def create(self, requestBody): pass

    def update(self, requestBody, id: int): pass

    def delete(self, id: int): pass

    