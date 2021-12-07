
from base_user import BaseUser

class CabRider(BaseUser):
    def __init__(self, name : str):
        super().__init__(name)
        self.bad_drivers = set()

    def add_bad_driver(self, name : str) -> None:
        self.bad_drivers.add(name)
    
    def __str__(self):
        return "\n".join([f"My name is {self.name}", 
                f"My current rating is {self.current_rating}", 
                f"My total rating count is {self.rating_count}",
                f"Drivers I don't like : {[str(x) for x in self.bad_drivers]} \n"])