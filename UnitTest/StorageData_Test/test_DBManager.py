import os
from unittest import TestCase

from WonkasCrewApplication.DataStorageManager import DBManager
from WonkasCrewApplication.DTOs.OompaLoopmaDTO import OompaLoompaDTO



class TestDBManager(TestCase):

    db_name = "OompaLoompaDB.db"

    db_path = os.path.join(os.getcwd(), db_name)

    # ====================================
    #         *** Tool Test Methods ***
    # ====================================

    @classmethod
    def tearDownClass(self):
        os.remove(self.db_path)


    def _createOompaLoompa(self):

        id = 1
        name = "Fluffet"
        age = 34
        job = "Chocolate foundry"
        height = 110
        weight = 40
        description = "Good worker and always have a smile in her face"

        oompaDTO = OompaLoompaDTO(id, name, age, job, height, weight, description)

        return oompaDTO




    # ====================================
    #         *** Tests ***
    # ====================================

    def test_When_Creates_new_DB_on_Firts_Execution(self):
        new_DB = DBManager(self.db_name)
        self.assertTrue(os.path.exists(self.db_path))
        self.assertTrue(os.path.isfile(self.db_path))


    def test_When_Inserts_OopmaLoompa_Data_in_DB(self):
        new_DB = DBManager(self.db_name)
        self.assertTrue(os.path.exists(self.db_path))
        self.assertTrue(os.path.isfile(self.db_path))

        oompaData = self._createOompaLoompa()

        id = new_DB.InsertData(oompaData.GetName(), oompaData.GetAge(),oompaData.GetJob(),
                               oompaData.GetHeight(), oompaData.GetHeight(),oompaData.GetDescription())

        self.assertEquals(id,1)

        id = new_DB.InsertData(oompaData.GetName(), oompaData.GetAge(), oompaData.GetJob(),
                               oompaData.GetHeight(), oompaData.GetHeight(), oompaData.GetDescription())
        self.assertEquals(id,2)

        id = new_DB.InsertData(oompaData.GetName(), oompaData.GetAge(),
                               oompaData.GetJob(), oompaData.GetHeight(),
                               oompaData.GetHeight(), oompaData.GetDescription())

        self.assertEquals(id,3)

        id = new_DB.InsertData(oompaData.GetName(), oompaData.GetAge(),
                               oompaData.GetJob(), oompaData.GetHeight(),
                               oompaData.GetHeight(), oompaData.GetDescription())
        self.assertEquals(id,4)



    def test_UpdateData(self):

        new_DB = DBManager(self.db_name)
        self.assertTrue(os.path.exists(self.db_path))
        self.assertTrue(os.path.isfile(self.db_path))

        oompaData = self._createOompaLoompa()

        id = new_DB.InsertData(oompaData.GetName(), oompaData.GetAge(), oompaData.GetJob(),
                               oompaData.GetHeight(), oompaData.GetHeight(), oompaData.GetDescription())

        self.assertEquals(id, 1)

        id = new_DB.InsertData(oompaData.GetName(), oompaData.GetAge(), oompaData.GetJob(),
                               oompaData.GetHeight(), oompaData.GetHeight(), oompaData.GetDescription())

        self.assertEquals(id, 2)

        #update oompa loompa name where id is 2
        id = new_DB.UpdateData(id, "ThisNewName", oompaData.GetAge(), oompaData.GetJob(),
                               oompaData.GetHeight(), oompaData.GetHeight(), oompaData.GetDescription())



    def test_When_Gets_One_OompaLoompa_From_DB(self):

        desired_id= 7

        new_DB = DBManager(self.db_name)
        self.assertTrue(os.path.exists(self.db_path))
        self.assertTrue(os.path.isfile(self.db_path))

        for i in range(0,10):
            oompaData = self._createOompaLoompa()

            id = new_DB.InsertData(str(i), oompaData.GetAge(), oompaData.GetJob(),
                                   oompaData.GetHeight(), oompaData.GetHeight(), oompaData.GetDescription())

        oompa_loompa_7 = new_DB.GetData(desired_id)

        print(oompa_loompa_7)

    def test_When_Gets_All_OompaLoompas_From_DB(self):

            new_DB = DBManager(self.db_name)
            self.assertTrue(os.path.exists(self.db_path))
            self.assertTrue(os.path.isfile(self.db_path))

            for i in range(0,10):
                oompaData = self._createOompaLoompa()

                id = new_DB.InsertData("Oompa_Name_" + str(i), oompaData.GetAge(), oompaData.GetJob(),
                                       oompaData.GetHeight(), oompaData.GetHeight(), oompaData.GetDescription())

            oompa_loompas= new_DB.GetData()

            self.assertEquals(len(oompa_loompas), 10)




