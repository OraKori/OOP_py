class WrongSeconds(Exception):
    def __str__(self):
        return "Wrong amount of seconds passed (greater or equal 60)"
    
class WrongMinutes(Exception):
    def __str__(self):
        return "Wrong amount of minutes passed (greater or equal 60)"

    
    
class Czas:
    TIME_ZONES = { "warszawa": 2,
                   "londyn": 1,
                   "tokyo": 9,
                   "sydney": 10,
                   "moskwa": 3,
                   "los angeles": -7 }
    
    def __init__(self, d = 0, h = 0, m = 0, s = 0):
        self.days = d
        self.hours = h
        self.minutes = m
        self.seconds = s
        
    @property    
    def days(self):
        return self._d
    
    @days.setter
    def days(self, val):
        self._d = val
        
    @property    
    def hours(self):
        return self._h
    
    @hours.setter
    def hours(self, val):
        if val < 0:
            self.days += val//60
            val = 24 - abs(val)%24
        elif val >= 24:
            self.days += val//24
            val %= 24
        self._h = val
        
    @property    
    def minutes(self):
        return self._m
    
    @minutes.setter
    def minutes(self, val):
        if "_m" not in self.__dict__ and  val >= 60:
            raise WrongMinutes
        if val < 0:
            self.hours += val//60
            val = 60 - abs(val)%60
        elif val >= 60:
            self.hours += val//60
            val %= 60
        self._m = val
        
    @property    
    def seconds(self):
        return self._s
    
    @seconds.setter
    def seconds(self, val):
        if "_s" not in self.__dict__ and  val >= 60:
            raise WrongSeconds
        if val < 0:
            self.minutes += val//60
            val = 60 - abs(val)%60
        elif val >= 60:
            self.minutes += val//60
            val %= 60
        self._s = val
        
    def strefa(self, city):
        if city.lower() not in self.TIME_ZONES: raise ValueError(f"City {city} not in time zone database")
        
        result_time = self.__class__( self.days, self.hours, self.minutes, self.seconds )
        result_time.hours += self.TIME_ZONES[city.lower()]
        
        return str(result_time)
        
        
    def __add__(self, other):
        assert isinstance(other, self.__class__), f"Cannot add {type(other)} to a Czas object"
        result = self.__class__()
        
        result.seconds += self.seconds + other.seconds
        result.minutes += self.minutes + other.minutes
        result.hours   += self.hours   + other.hours
        result.days    += self.days    + other.days
        
        return result 
    
    def __lt__(self, other):
        assert isinstance(other, self.__class__), f"Cannot compare {type(other)} with a Czas object"
        
        if self.days < other.days: return True
        elif self.hours < other.hours: return True
        elif self.minutes < other.minutes: return True
        elif self.seconds < other.seconds: return True
        
        return False
        
    def __str__(self):
        s = f"{self.hours}:{self.minutes:02}:{self.seconds:02}"
                
        if self.days == 0 :
            return s + ", dzien bez zmiany"
        
        elif self.days == 1 :
            return s + ", dzien nastepny"
        
        elif self.days == -1 :
            return s + ", dzien poprzedni"
        
        return s + f", dzien {self.days}"
        
        
        
        
#  --- TEST CASES ---
try:
    time = Czas( m = 60 )
except Exception as e:
    print(e.__class__, e, "\n")
    
time = Czas( d = 0, h = 23, m = 59, s = 59 )
print(time)

time.seconds += 1
print(time, "\n")

time1 = Czas( h = 3, m = 2, s = 1 )
time2 = Czas( h = 6, m = 5, s = 4 )
print( time1 + time2, "\n" )

print( time1 < time2 )
print( time2 < time1, "\n" )

time_gmt = Czas( h = 2, m = 0, s = 0 )
print( time_gmt.strefa("Londyn") ) 
print( time_gmt.strefa("Sydney") ) 
print( time_gmt.strefa("Los Angeles") ) 
