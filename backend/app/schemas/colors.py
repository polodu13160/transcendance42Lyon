import enum

class Colors(enum.Enum):
    GREEN = {"id": 1, "min_bayesian": 70, "value": 400} 
    BLUE = {"id": 2, "min_bayesian": 73, "value": 800} 
    PURPLE = {"id" : 3, "min_bayesian": 76, "value": 1300}
    GOLD = {"id" : 4, "min_bayesian": 81, "value": 2300} 
    GREY = {"id" : 0, "min_bayesian": None, "value": 200} 