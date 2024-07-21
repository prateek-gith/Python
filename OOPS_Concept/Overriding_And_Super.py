# variable Or Attribute Or Method Overriding
class A:
    var_1="Var_1 of Class A"
    # Note 1 : We Can't Call The Class A Constroctor With the Help Of Class B Object Because We Override The Constructor
    # Note 2 : If We Want To Call The Class A Constructor With The Help Of Class B Object The It Is Essential We Use "super().__init__()" Keyword Inside The Class B Constructor

    def __init__(self) -> None:
        self.var="Var Of Class Constructor A"
        self.var_1="Override Instance Var_1 Of Class Constructor A"
        self.Special="Special"

class B(A):
    # pass
    var_1="Override Var_1 Of Class B"
    def __init__(self) -> None:
        # If We Use Before The Constructor Instance Variable, super().__init__() Keyword Then it Call First super Class Constructor Then Travell In The Sub_Class Constructor
        # super().__init__()
        self.var="Var Of Class Constructor B"
        self.var_1="Overrride Instance Var_1 Of Class Constructor B"
        self.Special="Override Super"
        # If We Use After The Constructor Instance Variable, super().__init__() Keyword Then it Call First SUb_Class Constructor Instance Variable Then Travell In The Super_Class Constructor
        super().__init__()


if __name__=='__main__':
    obj_1=B()

    print(obj_1.Special)