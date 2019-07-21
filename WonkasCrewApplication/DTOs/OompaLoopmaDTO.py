

class OompaLoompaDTO(object):
    """

    OompaLoompaDTO class: Contains basic info of OompaLoompas. Only use as Data Transfer Object

    """

    Name = None
    Age = None
    Job = None
    Height = None
    Weight = None
    Description = None

    ###########################    CONSTRUCTOR  ###########################

    def __init__(self, name, age, job, height, weight, description):
        """

        :param name: string
        :param age: int
        :param job: string
        :param height: float
        :param weight: float
        :param description: string
        """
        self.Name = name
        self.Age = age
        self.Job = job
        self.Height = height
        self.Weight = weight
        self.Description = description


    ###########################    PUBLIC METHODS  ###########################

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
        :param height: float
        """
        self.Height = height

    def GetHeight(self):
        """
        :return: Float
        """
        return  self.Height



    def SetWeight(self, weight):
        """
        :param weight: float
        """
        self.Weight = weight

    def GetWeight(self):
        """
        :return: float
        """
        return self.Weight


    def SetName(self, description):
        """
        :param description: string
        """
        self.Description = description

    def GetName(self):
        """
        :return: string
        """
        return self.Description






