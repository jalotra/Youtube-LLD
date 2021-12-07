
class BaseUser():
    def __init__(self, name : str):
        self.name = name
        self.current_rating = 0
        self.rating_count = 0
     
     
    def update_rating(self, rating : float) -> None: 
        self.current_rating  = (self.rating_count * self.current_rating) + rating
        self.rating_count += 1
        self.current_rating /= (self.rating_count)
    
    def get_rating(self) -> float:
        return self.current_rating