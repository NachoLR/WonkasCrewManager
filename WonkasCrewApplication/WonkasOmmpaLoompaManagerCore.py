from WonkasCrewApplication.Serializers.JsonSerializer import JsonSerializer
from WonkasCrewApplication.DTOs.OompaLoopmaDTO import OompaLoompaDTO



class WonkasOmmpaLoompaManagerCore(object):


    # ====================================
    #         *** CONSTRUCTOR ***
    # ====================================
    def __init__(self):
        pass

    # =====================================
    #       *** PRIVATE METHODS ***
    # =====================================

    # ====================================
    #       *** PUBLIC METHODS ***
    # ================================

    def InsertNewOompaLoompa(self, id, name, age, job, height, weight, description):
        """Add a new Oompa Loompa"""
        pass

    def GetAllOompaLoompa(self):
        """Get the list of Oompa Loompas. For that list, only name, age and job are required per Oompa Loompa."""
        pass

    def GetOneOompaLoompa(self, id):
        """Get the full detail of an Oompa Loompa"""
        pass

    def UpdateOompaLoompa(self, id, name, age, job, height, weight, description):
        """Edit a current Oompa Loompa"""
        pass