# =============================================================================
# Class File for skillAudit
# =============================================================================
class skillAudit:
    
    skillDictionary = []
    skillCurrent = []
    errorList = []
    
    def __init__(self, sDict, sCurrent):
        self.skillDictionary = sDict
        self.skillCurrent = sCurrent
        if self.skillCurrent != self.skillDictionary:
            self.errorList.append('Not Equal')
        else:
            self.errorList.append('Equal')



