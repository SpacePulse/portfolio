# Define a class named Calculator.
class Calculator:
   
    # The __init__ method is the constructor. It initializes the attributes x and y. Gives them the values of 0.
    def __init__(self): # Self is used to represent itself.
        self.x = 0 
        self.y = 0

    # This method prompts the user to enter two numbers.
    def get_numbers(self):
        try:
            self.x = float(input('Enter the first number: '))
            self.y = float(input('\nEnter the second number: '))
        except ValueError:
            print('\nPlease enter two numbers for the mathematical operation ')

    # These methods simply return a value, which is enough for our desired outcome.
    
        # This method adds the attributes x and y and returns the result.
    def add(self):
        return self.x + self.y
    
        # This method subtracts the attributes x and y and returns the result.
    def sub(self):
        return self.x - self.y
     
        # This method multiplies the attributes x and y and returns the result.
    def multiply(self):
        return self.x * self.y
    
        # This method divides the attributes x and y and returns the result.
    def divide(self):
        if self.y !=0:
            return self.x / self.y
        else: # Error handling
            return ' Error: \'Division by zero\' '

    def run(self): # Creating a run method; which will always run on a loop
        while True: # Infinite loop
            
            print('\n Type 1 for Addition ')
            print(' Type 2 for Subtraction ')
            print(' Type 3 for Multiplication ')
            print(' Type 4 for Division ')
            print(' Finally, type 5 to Quit \n')

            choice = input('Please choose a number between 1 - 5: ')
            
            if choice == '5': # #5 will opt out of the loop and end the program
                print('Au revoir! :) ')
                break

            self.get_numbers() # Running the get_numbers method so that when Run() is executed, we retrieve those numbers.
            
            if choice == '1':
                print('\n Answer: ', self.add()) # If choice '1' then print and then run the method we created
            elif choice == '2':
                print('\n Answer: ', self.sub()) # If choice '2' then print and then run the method we created
            elif choice == '3':
                print('\n Answer: ', self.multiply()) # If choice '3' then print and then run the method we created
            elif choice == '4':
                print('\nAnswer: ', self.divide()) # If choice '4' then print and then run the method we created
            elif ValueError: 
                print('Sorry, you need to enter a number from 1 - 5 ') # Value error handling when asking for a certain type of value.

a = Calculator()
a.run()