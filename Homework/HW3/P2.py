
class Integer:
    def __init__(self, num_str):
        self.num_str = num_str

    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.num_str + other.num_str)
        return self.num_str + other

    def __repr__(self):
        result_str = ""

        for elem in self:
            result_str+= str(elem) + ","
        if len(self) > 0:
            result_str = result_str[:-2]
        result_str+= ""
        return result_str