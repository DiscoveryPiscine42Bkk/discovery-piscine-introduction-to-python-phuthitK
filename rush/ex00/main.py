import sys
from checkmate import checkmate

def main():
   if len(sys.argv) == 1:
      board = """\
....
..R.
..K.
....\
"""
      checkmate(board)

if __name__ == "__main__":
    main()
