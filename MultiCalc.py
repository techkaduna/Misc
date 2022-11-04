#Creating a class that does the greeting
class Greeting():
    def __init__(self,req="Nobody"):
        self.req = input(" Welcome,what is  your name?  ")
    '''
    create a method that welcomes
    '''
    def welcome(self):
        try:
            print("welcome, " + str(self.req))
        except:
            TypeError("There was an input error")
    '''
    this class does the farewell greeting
    '''
    def farewell(self):
        print(f"Thank you {self.req} for using this app!")

#this function is used in the while loop to control the running of the app
def stop_operation():
    choice = str(input(" press 1 to continue and 2 to stop:  "))
    return choice == "1"

# A class that is used to solve the cylinder problem
class cylinder():
    
    def __init__(self,radius=0,height=0):
        #this takes the input of users
        self.radius = input("Input radius: ")
        self.height = input("Input height: ")
    '''
    this method solves the volume of the cylindeer
    '''
    def volumer(self):
        pi = 3.14
        
        result = ((float(self.radius)**2)*pi* float(self.height))
        print("The volume of the cylinder is "+str(result))
    '''
    this method solves the total surface area
    '''
    def total_surf_area(self):
        pi = 3.14
        #this is the calculation proceedure
        result2 = (((float(self.radius))*pi* float(self.height))*2)+(2*pi*float((float(self.radius)**2)))
        print("The total surface area is "+ str(result2))
#this is the line class
class line():
    pi = 3.14
    def __init__(self,coordX1=0,coordY1=0,coordX2=0,coordY2=0):
        '''
        take the user input 
        '''
        self.coordX1 = input("input X1:  ")
        self.coordY1 = input("input Y1:  ")
        self.coordX2 = input("input X2:  ")
        self.coordY2 = input("input Y2:  ")
    '''
    this method calculates the distance between two points
    '''
    def distance(self):
        X1 = float(self.coordX1) 
        X2 = float(self.coordX2)
        Y1 = float(self.coordY1)
        Y2 = float(self.coordY2)
        dist = ((X2-X1)**2 + (Y2-Y1)**2)**0.5
        print("The distance between the points is "+ str(dist))
    '''
    this method calculates the slope
    '''
    def slope(self):
        X1 = float(self.coordX1) 
        X2 = float(self.coordX2)
        Y1 = float(self.coordY1)
        Y2 = float(self.coordY2)
        
        slp = (Y2-Y1) / (X2-X1)
        print("The slope of the line is "+ str(slp))

#declaring the simple interest class
class Simple_Interest():
    def __init__(self,principal=0,rate=0,time=0,convtime=0):

        self.principal = input("Please input principal: ")
        self.rate = input("Please input rate: ")
        self.time = input("Please input time in months: ")
        self.convtime = int((self.time))/12
    '''
    this method does the output
    '''
    def output(self):
        princp = float(self.principal)
        r8te = float(self.rate)
        tiime = float(self.convtime)
        #declaring variables inside the method
        result = ((princp)*(r8te)*(tiime))/100
        total_fee = float(result) + princp
        print("Your Simple Interest is: "+ str(result) + " total fee payable is " + str(total_fee))

#Running the program
while True:
    #greeting the users 
    greet = Greeting()
    print(greet.welcome())
    '''
    Asking user to select operator
    '''
    def choose_operation():
        operator = input("choose operation: (1:Volume of cylinder ) '\n' (2:surface area of cyliner)'\n'(3:Slope of line)'\n'(4:distance btw 2 lines)'\n'(5:Simple interest) ")
        
        if operator == "1":
            mycyl = cylinder()
            return mycyl.volumer()
        elif operator == "2":
            mycyl = cylinder()
            return mycyl.total_surf_area()
        elif operator == "3":
            myline = line()
            return myline.slope()
        elif operator == "4":
            myline = line()
            return myline.distance()
        elif operator == "5":
            simp = Simple_Interest()
            return simp.output()
        else:
            print("No operation chosen")
    choose_operation()

    #breaking the while loop with some conditions
    if not stop_operation():
            print(greet.farewell())
            break
