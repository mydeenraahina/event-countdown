from datetime import datetime,date
class EventCountown:
    
    def __init__(self):
        print(f"Set EventCountown !")
        print(datetime.now())
        try:
            self.getting_year=int(input(f"Enter year(YYYY) "))
            self.getting_month=int(input(f"Enter month(MM) "))
            self.getting_day=int(input(f"Enter day(DD) "))
            self.getting_hour=int(input(f"Enter hour(HH) "))
            self.getting_minute=int(input(f"Enter minute(MM) "))
            self.getting_second=int(input(f"Enter second(SS) "))
            self.getting_event=input(f"Enter your Event here..")
        except (ValueError,TypeError):
            print(f"Enter a valid date/time value")
            exit()
    def time_and_date_calculation(self):
        dt=datetime(self.getting_year,self.getting_month,self.getting_day,self.getting_hour, self.getting_minute, self.getting_second)
        current_datetime=datetime.now()
        if self.getting_year<current_datetime.year:
            print( f"Times up!")
        else:
            result=dt-current_datetime
            print(  f"Your Event :{self.getting_event}")
            print(f"Countdown for your event!..{result}")

obj=EventCountown()
obj.time_and_date_calculation()
getting_choice=input("Do you want to continue setting the Event countown [yes\no]")
if  getting_choice.casefold()=="yes":
    obj=EventCountown()
    obj.time_and_date_calculation()
elif getting_choice.casefold()=="no":
    print("Event Countdown setup complete. Exiting...")
    exit()
else:
    print(f"please check your input!")
    exit()

                    
        
    
    
                     
