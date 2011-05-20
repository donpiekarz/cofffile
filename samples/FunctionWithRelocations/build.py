
import sys
sys.path.append('../../src/')


import cofffile

def main():
    input_file = "foo.xml"
    output_file = "foo.o"
    coff = cofffile.COFF(input_file)
    coff.write(output_file)
   

if __name__ == "__main__":
    main()
    print "__done__"