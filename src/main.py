from import_file import *
import petron_loader as pet
import encodings

try:
    if __name__ == "__main__":
        print("begins")
        pet.main()
    else:
        raise RuntimeError
except RuntimeError:
    print("Program must be run by Main.")
