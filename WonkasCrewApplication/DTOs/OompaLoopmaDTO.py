

class OompaLoompaDTO(object):
    """

    OompaLoompaDTO class: Contains basic info of OompaLoompas. Only use as Data Transfer Object

    """
    Id = None
    Name = None
    Age = None
    Job = None
    Height = None
    Weight = None
    Description = None

    # ====================================
    #         *** CONSTRUCTOR ***
    # ====================================

    def __init__(self, id=None, name=None, age=None, job=None, height=None, weight=None, description=None):
        """

        :param name: string
        :param age: int
        :param job: string
        :param height: float
        :param weight: float
        :param description: string
        """
        self.Id = id
        self.Name = name
        self.Age = age
        self.Job = job
        self.Height = height
        self.Weight = weight
        self.Description = description



    # ====================================
    #       *** PUBLIC METHODS ***
    # ====================================

    def SetId(self, id):
        """
        :param id: int
        :
        """
        self.Id = id

    def GetId(self):
        """
        :return: int
        """
        return self.Id


    def SetName(self, name):
        """
        :param name: string
        """
        self.Name = name

    def GetName(self):
        """
        :return:  string
        """
        return self.Name


    def SetAge(self, age):
        """
        :param age: int
        """
        self.Age = age

    def GetAge(self):
        """
        :return: int
        """
        return self.Age


    def SetJob(self, job):
        """
        :param job: string
        """
        self.Job = job

    def GetJob(self):
        """
        :return: string
        """
        return self.Job


    def SetHeight(self, height):
        """
        :param height: int
        """
        self.Height = height

    def GetHeight(self):
        """
        :return: int
        """
        return  self.Height



    def SetWeight(self, weight):
        """
        :param weight: inr
        """
        self.Weight = weight

    def GetWeight(self):
        """
        :return: int
        """
        return self.Weight


    def SetDescription(self, description):
        """
        :param description: string
        """
        self.Description = description

    def GetDescription(self):
        """
        :return: string
        """
        return self.Description






