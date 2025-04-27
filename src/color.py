class Color:
    def __init__(self, r:int, g:int, b:int, name:str):
        self.rgb = (r, g, b)
        self.name = name

    def __str__(self):
        return f"{self.name}: RGB{self.rgb}"
    
    @property
    def hsv(self):
        rgb = [v / 255 for v in self.rgb]
        cmax = max(rgb)
        cmin = min(rgb)
        delta = cmax - cmin

        if abs(cmax - rgb[0]) < 0.001:
            h = (60 * ((rgb[1] - rgb[2]) / delta) + 360) % 360
        elif abs(cmax - rgb[1] < 0.001):
            h = (60 * ((rgb[1] - rgb[2]) / delta) + 120) % 360
        else:
            h = (60 * ((rgb[1] - rgb[2]) / delta) + 240) % 360   

        s = 0 if cmax == 0 else ( delta / cmax ) * 100

        v = cmax * 100

        return(round(h), round(s), round(v))



if __name__ == '__main__':
    cor1 = Color(127, 78, 198, 'Rosazul')
    print("RGB: ", cor1.rgb)
    print("HSV: ", cor1.hsv)