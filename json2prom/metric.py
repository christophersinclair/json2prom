from dataclasses import dataclass


@dataclass
class Metric(object):
    """
    The Metric class acts as a Singleton. All code that uses Metric uses the same Metric instance.
    """

    __instance = None
    metrics = []

    @staticmethod
    def getInstance():
        # Return single instance
        if Metric.__instance == None:
            Metric()
        return Metric.__instance

    def __init__(self):
        # When constructed, set instance to self
        if Metric.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            Metric.__instance = self
