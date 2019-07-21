import json

class JsonSerializer(object):

    @classmethod
    def SerializeObject(self, data):
        """
        Converts an object into a json string

        :param data: object
        :return: string
        """

        if isinstance(data,dict):
            serializad_data = json.dumps(data)
        else:
            serializad_data = json.dumps(data.__dict__)

        return serializad_data

    @classmethod
    def DeserializeJson(self, json_string, object_to_serialize):
        """
        Converts json string in related object

        object_to_serialize have to be an instace of the desired to
        convert object

        :param json_string: String
        :param object_to_serialize: object
        :return: object
        """


        object_to_serialize.__dict__ = json.loads(str(json_string))
        return object_to_serialize

