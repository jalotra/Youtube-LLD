from collections import OrderedDict
from cab_driver import CabDriver
from cab_rider import CabRider


if __name__ == "__main__":
    # Suppose entries are comma separated values
    # Take Data inputs
    entries = int(input())
    drivers = OrderedDict()
    users = OrderedDict()
    
    for _ in range(entries):
        driver_name, driver_rating, user_name, user_rating = map(str, input().split(" ")) 
        driver_rating = int(driver_rating)
        user_rating = int(user_rating)
        
        # Get the driver object for {driver_name} 
        curr_driver = drivers.get(driver_name, None)
        if (curr_driver is None):
            curr_driver = drivers[driver_name] = CabDriver(driver_name)
        
        # Get the user object for {user_name}
        curr_user = users.get(user_name, None)
        if curr_user is None:
            curr_user = users[user_name] = CabRider(user_name)

        # Now update the rating of both {curr_driver} and {curr_user}
        curr_driver.update_rating(user_rating)
        curr_user.update_rating(driver_rating)

        # Add bad drivers or users 
        if driver_rating == 1 or user_rating == 1:
            curr_user.add_bad_driver(driver_name)
            curr_driver.add_bad_user(user_name)        
            

        
    for user in users.values():
        print(str(user))
    
    for driver in drivers.values():
        print(str(driver))