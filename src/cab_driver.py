from base_user import BaseUser

class CabDriver(BaseUser):
    def __init__(self, name : str):
        super().__init__(name)
        self.bad_users = set()
    
    def add_bad_user(self, name : str) -> None:
        self.bad_users.add(name)
    
    def __str__(self):
        return "\n".join([f"My name is {self.name}", 
                f"My current rating is {self.current_rating}", 
                f"My total rating count is {self.rating_count}",
                f"Users I don't like : {[str(x) for x in self.bad_users]} \n"])