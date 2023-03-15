def _gncolor(color,c):
        colorcode = ""
        if color != False:
            vl = 0
            if type(color) == int:
                vl = color
                color = [color]
            while len(color) < 3:
                color.append(vl)
            r = color[0]
            g = color[1]
            b = color[2]
            colorcode += "\033["+c+";2;{};{};{}m".format(r, g, b)
        return colorcode

def colorize(fgcolor=False, bgcolor=False, weight=0):
    return _gncolor(fgcolor,"38") + _gncolor(bgcolor,"48")+"\033["+str(weight)+"m"

def fgcolor(fgcolor):
    return _gncolor(fgcolor,"38")

def bgcolor(bgcolor):
    return _gncolor(bgcolor,"48")

def uncolor():
    return "\033[0m"
