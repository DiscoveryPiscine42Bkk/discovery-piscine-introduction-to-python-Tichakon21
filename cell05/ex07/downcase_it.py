import sys
def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("RTFM (Read the F-ing manual)")

if __name__ == "__main__":
    main()