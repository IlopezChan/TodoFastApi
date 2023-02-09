from abc import ABC, abstractmethod

class IAuthInteractor(ABC):

    @abstractmethod
    def login(user, userRepository): pass

