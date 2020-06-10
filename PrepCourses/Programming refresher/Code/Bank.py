
class Bank:
    
    IFSC_Code = 241
    bankname = "Standard Chartered Bank"
    
    def __init__(self, branchname, branchlocation):
        
        self.branchname = branchname
        self.loc = branchlocation