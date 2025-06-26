import sys
from checkmate import checkmate

def main():
    if len(sys.argv) == 1:
        print("No file provided.")
    else:
        for filename in sys.argv[1:]:
            print(f"Checking file: {filename}")
            try:
                with open(filename, 'r') as file:
                    board_data = file.read().strip()
                    checkmate(board_data)
            except Exception as e:
                print("Error")

if __name__ == "__main__":
    main()
