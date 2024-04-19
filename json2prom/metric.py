import logging

from dataclasses import dataclass


@dataclass
class Metric(object):
    __instance = None
    metrics = []

    @staticmethod
    def getInstance():
        """Static access method for a Singleton"""
        if Metric.__instance == None:
            Metric()
        return Metric.__instance

    def __init__(self):
        """Virtually private constructor"""
        if Metric.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            Metric.__instance = self
