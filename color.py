class Color:
    def __init__(self, r:int, g:int, b:int, name:str):
        self.rgb = (r, g, b)
        self.name = name

    def __str__(self):
        return f"{self.name}: RGB{self.rgb}"
    

if __name__ == '__main__':
    cor1 = Color(127, 78, 198, 'Rosazul')
    print(cor1)