class Library :
    def __init__(self,List_Of_Books,Library_Name) :
        self.List_Of_boks=List_Of_Books
        self.Library_Name=Library_Name
        self.L_Dict={}

    def Display_Boks(self):
        return f"\n Book List Is : {self.List_Of_boks} \nLend Book : {self.L_Dict}\n"
    

    def Lend_Book(self,B_Name,U_Name):
        if B_Name in self.L_Dict.keys():
            print(f"\nBook Is Given To {self.L_Dict[B_Name]}\n")
        else:
            self.L_Dict.update({B_Name:U_Name})
            print("\n!! Thank You For Lend Book !!\n")

    # @staticmethod
    def Add_Book(self,A_Book):
        self.List_Of_boks.append(A_Book)
        print("\n!!  Book Is Added  !!\n")

    # @staticmethod
    def Return_Book(self,R_Name):
        self.L_Dict.pop(R_Name)
        print("\n!!  Thank You Visit Again  !!\n")

if __name__=='__main__':
    print("\n!!-------Welcome To Library Management--------!!\n")

    List_Book=["Python","C++","Java","HTML","CSS","Java Script","C","DataBase"]

    Pr_Library=Library(List_Book,"Pr Library")

    

    while(True):
        
        a=int(input('List Of Library Is \n 1.Pr_library \nEnter What You Want : '))

        if a == 1:
            print("\n!!   Welcome To Pr Library   !!\n")
            while (True) :
            
                b=int(input("Press 1.For Display The Library Books\nPress 2.For Lend Book\nPress 3.For Add Book\nPress 4.For Return The Book\nPress 5.Exit : "))

                if b == 1:
                    print(Pr_Library.Display_Boks())

                elif b == 2:
                    L_Book=input("\nEnter The Name Of Book : ")
                    L_User=input("Enter your Name : ")
                    Pr_Library.Lend_Book(L_Book,L_User)

                elif b==3:
                    A_Book=input("\nEnter The Book Name : ")
                    Pr_Library.Add_Book(A_Book)

                elif b==4 :
                    R_Book=input("\nEnter The Book Name : ")
                    Pr_Library.Return_Book(R_Book)

                elif b==5:
                    print("\n!!   Thank You For Vist The Pr_Library   !!\n")
                    break
                else :
                    print("\n!!   Sorry   !!\n!!   Wrong Choice   !!\n")
                    exit()
        else :
            print("\n!!   Sorry   !!\n!!   Wrong Choice   !!")
            break