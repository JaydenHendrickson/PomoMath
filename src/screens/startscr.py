def startscr(stdsdr):
    # Find Center
    height, width = stdsdr.getmaxyx()
    centerX = width // 2
    centerY = height // 2

    # Text
    title = "PomoMath"

    # Writing Text
    stdsdr.addstr(centerY, centerX - len(title), title)  # Title
    # Why does it use (y,x) and not (x,y) ?? :(
