from import_file import *
import petron_loader as pet

try:
    if __name__ == "__main__":
        print("begins")
        pet.main()
    else:
        raise RuntimeError
except RuntimeError:
    print("Program must be run by Main.")
