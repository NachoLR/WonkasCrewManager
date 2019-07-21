#Python module imports
import os
import sys

#Custom Imports
from WonkasCrewApplication.Serializers.JsonSerializer import JsonSerializer
from WonkasCrewApplication.DataValidators.DataValidator import DataValidator
from WonkasCrewApplication.DTOs.OompaLoopmaDTO import OompaLoompaDTO
from WonkasCrewApplication.DataStorageManager import DBManager



class WonkasOmmpaLoompaManagerCore(object):

    db_path = "WonkasCrewApplication/OompaLoompaDB/OompaLoompaDB.db"
    # ====================================
    #         *** CONSTRUCTOR ***
    # ====================================
    def __init__(self):
        self._validator = DataValidator()
        self._dbManager = DBManager(self.db_path)

    # =====================================
    #       *** PRIVATE METHODS ***
    # =====================================
    def _converOompaLoompaListToLiteDict(self, list_oompa):

        lite_oompaList = {}
        for oompa in list_oompa:
            lite_oompaList[oompa[0]] = ((oompa[0], oompa[1], oompa[2], oompa[3]))

        return lite_oompaList
    def _converTupleToOompaLoompaDTO(self, oompa_dto):

        return OompaLoompaDTO(oompa_dto[0], oompa_dto[1], oompa_dto[2], oompa_dto[3], oompa_dto[4], oompa_dto[5], oompa_dto[6])



    # ====================================
    #       *** PUBLIC METHODS ***
    # ================================

    def InsertNewOompaLoompa(self, name, age, job, height, weight, description):
        """Add a new Oompa Loompa"""

        name = self._validator.ValidateString(name)
        age = self._validator.ValidateInteger(age)
        job = self._validator.ValidateString(job)
        height = self._validator.ValidateInteger(height)
        weight = self._validator.ValidateInteger(weight)
        description = self._validator.ValidateString(description)

        oompa_dto = OompaLoompaDTO(name, age, job, height, weight, description)
        insert_response = self._dbManager.InsertData(name, age, job, height, weight, description)

        if isinstance(insert_response, int):
            oompa_dto.SetId(insert_response)
            return JsonSerializer.SerializeObject(oompa_dto)
        else:
            return "{Error: %s}" %(insert_response,)


    def GetAllOompaLoompa(self):
        """Get the list of Oompa Loompas. For that list, only name, age and job are required per Oompa Loompa."""

        try:
            oompa_list = self._dbManager.GetData()
            oompa_dict = self._converOompaLoompaListToLiteDict(oompa_list)
            response = JsonSerializer.SerializeObject(oompa_dict)

        except Exception as e:
            raise e

        return response

    def GetOneOompaLoompa(self, id):
        """Get the full detail of an Oompa Loompa"""
        try:

            id = self._validator.ValidateInteger(id)
            oompa_db_response = self._dbManager.GetData(id)
            oompa_dto = self._converTupleToOompaLoompaDTO(oompa_db_response)
            response = JsonSerializer.SerializeObject(oompa_dto)

        except Exception as e:
            raise e

        return response

    def UpdateOompaLoompa(self, id, name, age, job, height, weight, description):
        """Edit a current Oompa Loompa"""
        try:

            id = self._validator.ValidateInteger(id)
            oompa_db_response = self._dbManager.GetData(id)
            oompa_dto = self._converTupleToOompaLoompaDTO(oompa_db_response)

            if name is not None:
                name = self._validator.ValidateString(name)
                oompa_dto.SetName(name)
            if age is not None:
                age = self._validator.ValidateInteger(age)
                oompa_dto.SetAge(age)
            if job is not None:
                job = self._validator.ValidateString(job)
                oompa_dto.SetJob(job)
            if height is not None:
                height = self._validator.ValidateInteger(height)
                oompa_dto.SetHeight(height)
            if weight is not None:
                weight = self._validator.ValidateInteger(weight)
                oompa_dto.SetWeight(weight)
            if description is not None:
                description = self._validator.ValidateString(description)
                oompa_dto.SetDescription(description)

            self._dbManager.UpdateData(id, oompa_dto.GetName(), oompa_dto.GetAge(), oompa_dto.GetJob(), oompa_dto.GetHeight(), oompa_dto.GetWeight(), oompa_dto.GetDescription())

            response = JsonSerializer.SerializeObject(oompa_dto)

        except Exception as e:
            raise e

        return response
