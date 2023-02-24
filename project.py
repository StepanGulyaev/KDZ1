class Project:
    def __init__(self,f1,f2):
        self.f1 = f1
        self.f2 = f2
        self.flag_list = []

    def is_exclused(self):
        if 'x' in self.flag_list:
            return True
        return False

