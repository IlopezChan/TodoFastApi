from typing import List
from abc import ABC
from abc import abstractmethod

class BaseRepository():
    
    def get_all(self) -> List:pass

    def get_by_id(self, id: int): pass

    def create(self, Entity): pass

    def update(self, Entity): pass
    
    def delete(self, id: int): pass
    