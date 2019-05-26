class myColor():
    def __init__(self):
        self.red = 50
        self.green = 10
        self.blue = 100
    
    #using __getattr__ to create attributes
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")    


def main():
    c1 = myColor()
    print(c1.red) 
    print(c1.rgbcolor)  
    print(c1.hexcolor) 
    c1.rgbcolor = (100, 10, 1)
    print(c1.rgbcolor)
    print(c1.__dir__())


if __name__ == "__main__":
    main()