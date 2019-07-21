from WonkasCrewApplication.DTOs.OompaLoopmaDTO     import   OompaLoompaDTO

import unittest


class MasterMindLogic_Tests(unittest.TestCase):


    def test_When_Creates_New_OompaLoompaDTO(self):

        oompaDTO = OompaLoompaDTO()
        self.assertIsInstance(oompaDTO, OompaLoompaDTO)



    def test_OompaLoompaDTO_data_consistend_using_constructor(self):

        id = 1
        name = "Fluffet"
        age = 34
        job = "Chocolate foundry"
        height = 110
        weight = 40
        description = "Good worker and always have a smile in her face"

        oompaDTO = OompaLoompaDTO(id, name, age, job, height, weight, description)
        self.assertIsInstance(oompaDTO, OompaLoompaDTO)

        self.assertEquals(oompaDTO.Id, id)
        self.assertEquals(oompaDTO.GetName(), name)
        self.assertEquals(oompaDTO.GetAge(), age)
        self.assertEquals(oompaDTO.GetJob(), job)
        self.assertEquals(oompaDTO.GetHeight(), height)
        self.assertEquals(oompaDTO.GetWeight(), weight)
        self.assertEquals(oompaDTO.GetDescription(), description)

    def  test_OompaLoompaDTO_data_consistend_using_Setters(self):

        id = 1
        name = "Fluffet"
        age = 34
        job = "Chocolate foundry"
        height = 110
        weight = 40
        description = "Good worker and always have a smile in her face"

        oompaDTO = OompaLoompaDTO()
        self.assertIsInstance(oompaDTO, OompaLoompaDTO)

        #Check if DTO was initializated at None default values
        self.assertEquals(oompaDTO.GetId(), None)
        self.assertEquals(oompaDTO.GetName(), None)
        self.assertEquals(oompaDTO.GetAge(), None)
        self.assertEquals(oompaDTO.GetJob(), None)
        self.assertEquals(oompaDTO.GetHeight(), None)
        self.assertEquals(oompaDTO.GetWeight(), None)
        self.assertEquals(oompaDTO.GetDescription(), None)


        oompaDTO.SetId(id)
        oompaDTO.SetName(name)
        oompaDTO.SetAge(age)
        oompaDTO.SetJob(job)
        oompaDTO.SetHeight(height)
        oompaDTO.SetWeight(weight)
        oompaDTO.SetDescription(description)


        #Check Dto values setted
        self.assertEquals(oompaDTO.GetId(), id)
        self.assertEquals(oompaDTO.GetName(), name)
        self.assertEquals(oompaDTO.GetAge(), age)
        self.assertEquals(oompaDTO.GetJob(), job)
        self.assertEquals(oompaDTO.GetHeight(), height)
        self.assertEquals(oompaDTO.GetWeight(), weight)
        self.assertEquals(oompaDTO.GetDescription(), description)


if __name__ == '__main__':
    unittest.main()