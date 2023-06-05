from src.driver.driver import Driver
from src.engine.engine import *
from src.team.team import Team
from typing import List

class TeamFactory:
    def createTeam(self, name: str, engine: EngineInt | str, country: str, drivers: List(Driver)) -> Team:
        """
        create a team with a custom engine

        params:

        name: str
        engine: EngineInt | str
        country: str
        drivers: List(Driver)
        
        returns:
        Team
        """

        if isinstance(engine, str):
            engine = Engine(engine = engine)

        return Team(name = name, engine = engine, country = country, drivers = drivers)

    def createTeamFerrariEngine(self, name: str, country: str, drivers: List(Driver)) -> Team:
        """
        create a team with a Ferrari engine

        params:

        name: str
        country: str
        drivers: List(Driver)
        
        returns:
        Team
        """

        return Team(name = name, engine = FerrariEngine(), country = country, drivers = drivers)
    
    def createTeamHondaRBPTEngine(self, name: str, country: str, drivers: List(Driver)) -> Team:
        """
        create a team with a Honda Red Bull Power Trains engine

        params:

        name: str
        country: str
        drivers: List(Driver)
        
        returns:
        Team
        """

        return Team(name = name, engine = HondaRBPTEngine(), country = country, drivers = drivers)
    
    def createTeamMercedesEngine(self, name: str, country: str, drivers: List(Driver)) -> Team:
        """
        create a team with a Mercedes engine

        params:

        name: str
        country: str
        drivers: List(Driver)
        
        returns:
        Team
        """

        return Team(name = name, engine = MercedesEngine(), country = country, drivers = drivers)
    
    def createTeamRenaultEngine(self, name: str, country: str, drivers: List(Driver)) -> Team:
        """
        create a team with a Renault engine

        params:

        name: str
        country: str
        drivers: List(Driver)
        
        returns:
        Team
        """

        return Team(name = name, engine = RenaultEngine(), country = country, drivers = drivers)
   