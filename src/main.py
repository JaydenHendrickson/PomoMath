def main(stdsdr):
    startscr(stdsdr)
    stdsdr.getch()
if __name__ == '__main__':
    import curses
    from screens.startscr import startscr
    curses.wrapper(main)