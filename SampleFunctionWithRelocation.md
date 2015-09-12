# Introduction #
This sample shows function which need a relocations.

# Function With Relocation #
Folder with source: samples/FunctionWithRelocation

## foo function ##
In file foo.bin is binary data with definition of function called foo.
Hexadecimal values from **foo.bin**:
```
55 89 E5 83 EC 08 8B 45  08 89 04 24 E8 00 00 00  
00 89 45 FC 8B 45 08 89  04 24 E8 00 00 00 00 89
C2 8D 45 FC 01 10 8B 45  FC C9 C3 90 90 90 90 90
```
The foo function is also defined in **foo.c** and it is in C syntax.
```
int foo(char* str){
	int var;
	var = bar(str);
	var += strlen(str);
	return var;
}
```
You can see two calls (E8 00 00 00 00) and they need to be relocated (bar and strlen).

## foo xml ##
In file **foo.xml** is defined all structure of output COFF file.
```
<cofffile>
	<image_file_header Machine="IMAGE_FILE_MACHINE_I386" NumberOfSections="-1" TimeDateStamp="-1" PointerToSymbolTable="-1" NumberOfSymbols = "-1" SizeOfOptionalHeader="0" Characteristics="0x104" />
	<image_section_header Name=".text" Misc="0" Misc_PhysicalAddress = "0" Misc_VirtualSize = "0" VirtualAddress = "0"	SizeOfRawData = "-1" PointerToRawData = "-1" PointerToRelocations = "-1" PointerToLinenumbers = "0" NumberOfRelocations = "-1" NumberOfLinenumbers = "0" Characteristics = "0x60000020" />
	<image_section Type="file" Filename="foo.bin" />
	<image_relocation RVA = "0x0D" SymbolTableIndex = "2" Type = "0x14" />
	<image_relocation RVA = "0x1B" SymbolTableIndex = "1" Type = "0x14" />
	<image_symbol_table_item Name="_foo" Value="0" SectionNumber = "1" Type = "0x20" StorageClass = "2" NumberOfAuxSymbols = "0" />
	<image_symbol_table_item Name="_strlen" Value="0" SectionNumber = "0" Type = "0x20" StorageClass = "2" NumberOfAuxSymbols = "0" />
	<image_symbol_table_item Name="_bar" Value="0" SectionNumber = "0" Type = "0x20" StorageClass = "2" NumberOfAuxSymbols = "0" />
</cofffile>


```

There is two members image\_relocation, where you define address (in binary file) these call, which need to be updated.

All description of members and attributes are in [XMLStructure](XMLStructure.md).

## main function ##
In file **main.c** are definitions of includes, extern functions (foo) and main function.

Here is **main.c**:
```
#include <stdio.h>

extern int foo(char*);

int bar(char* str){
	char* pos = strchr(str,'a');
	return pos - str;
}

int main(){
	puts("begin");
	printf("foo result: %d\n", foo("bar"));
	printf("bar result: %d\n", bar("bar"));
	puts("end");
	return 0;
}
```

## build script ##
To build COFF file you have to create XML file with needed headers, create object of COFF and write data.

sample builder (**build.py**):
```
import cofffile

def main():
    input_file = "foo.xml"
    output_file = "foo.o"
    coff = cofffile.COFF(input_file)
    coff.write(output_file)
   

if __name__ == "__main__":
    main()
    print "__done__"
```

## almost done ##
Now just run gcc to compile all files (notice: **foo.o**):
```
gcc -o main.exe main.c foo.o
```

## testing ##
When the compilation and linking proceeded without errors, it is time to run **main.exe**

You should see somthing like this:
```
>main.exe
begin
foo result: 4
bar result: 1
end
```

## troubleshooting ##
Troubleshooting is moved here: [Troubleshooting](Troubleshooting.md)