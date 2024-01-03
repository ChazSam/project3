

class Trainer:
    
    def __init__(self, name, work_days):
        self.name = name
        self.work_days = work_days
   
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError ("Please enter a valid name")
        
    @property
    def work_days(self):
        return self._work_days
    
    @work_days.setter
    def work_days(self, work_days):
        if isinstance(work_days, str):
            self._work_days = work_days
        else:
            raise ValueError ("Please enter days with a single letter and commas (M,T,W,H,F,S)")

    def get_all(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def change_work_days(self):
        pass

    def assign_member(self):
        pass

    def remove_member(self):
        pass