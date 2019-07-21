


class DataValidator(object):

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
    # ====================================


    def ValidateString(self,data_str):
        try:
            if isinstance(data_str, str):
                return data_str
            else:
                return str(data_str).encode('utf-8')

        except Exception as e:
            raise e


    def ValidateInteger(self,data_int):
        try:
            if isinstance(data_int, int):
                return data_int
            else:
                return str(data_int)
        except Exception as e:
            raise e


    def ValidateSFloat(self, data_float):
        try:
            if isinstance(data_float, float):
                return data_float
            else:
                return float(data_float)
        except Exception as e:
            raise e



