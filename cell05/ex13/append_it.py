import sys
def main():
    params = sys.argv[1:]
    if len(params) == 0:
        return
    for p in params:
        if p.endswith("ism"):
            continue
        print(p + "ism")
if __name__ == "__main__":
   main()