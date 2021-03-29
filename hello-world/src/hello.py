class HelloWorld:
    def __init__(self):
        print("init")
    
    def say(self):
        print("hello world")
        
    def greetins(self, name):
        return f"Hello, {name}"

    def capital_case(self, text):
        if not isinstance(text, str):
            raise TypeError('Please provide a string argument')
        return text.capitalize()

if "__main__" == __name__:
    hello_world = HelloWorld()
    
    hello_world.say()
    
    hi = hello_world.greetins("aurelio")
    hi2 = hello_world.capital_case(9)
    
    print(hi)