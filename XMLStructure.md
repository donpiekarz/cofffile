# Introduction #
Describes XML structure (members and attributes)


# Details #
COFF class is built from XML file. This XML fully describes output binary file, so you should note in what order are members or there are correct indexes etc. It is a literal translation, so be careful.


# Members #
Note: Value -1 means automatic calculations.

All samples are from [SampleFunctionWithRelocation](SampleFunctionWithRelocation.md)

## COFF ##
Definition of one COFF file. Parent for other members.

Member name: **cofffile**

Sample:
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


## IMAGE FILE HEADER ##
Member name: **image\_file\_header**

Attributes:
  * Machine (key in dict, int in hexadecimal, int in decimal)
    * IMAGE\_FILE\_MACHINE\_UNKNOWN
    * IMAGE\_FILE\_MACHINE\_AM33
    * IMAGE\_FILE\_MACHINE\_AMD64
    * IMAGE\_FILE\_MACHINE\_ARM
    * IMAGE\_FILE\_MACHINE\_EBC
    * IMAGE\_FILE\_MACHINE\_I386
    * IMAGE\_FILE\_MACHINE\_IA64
    * IMAGE\_FILE\_MACHINE\_MR32
    * IMAGE\_FILE\_MACHINE\_MIPS16
    * IMAGE\_FILE\_MACHINE\_MIPSFPU
    * IMAGE\_FILE\_MACHINE\_MIPSFPU16
    * IMAGE\_FILE\_MACHINE\_POWERPC
    * IMAGE\_FILE\_MACHINE\_POWERPCFP
    * IMAGE\_FILE\_MACHINE\_R4000
    * IMAGE\_FILE\_MACHINE\_SH3
    * IMAGE\_FILE\_MACHINE\_SH3DSP
    * IMAGE\_FILE\_MACHINE\_SH4
    * IMAGE\_FILE\_MACHINE\_SH5
    * IMAGE\_FILE\_MACHINE\_THUMB
    * IMAGE\_FILE\_MACHINE\_WCEMIPSV2
  * NumberOfSections (-1, value in hexadecimal, value in decimal)
  * TimeDateStamp (-1 (current date), value in hexadecimal, value in decimal)
  * PointerToSymbolTable (-1, value in hexadecimal, value in decimal)
  * NumberOfSymbols (-1, value in hexadecimal, value in decimal)
  * SizeOfOptionalHeader (not supported, must be 0)
  * Characteristics (value in hexadecimal, value in decimal)

Sample:
```
<image_file_header 
  Machine="IMAGE_FILE_MACHINE_I386" 
  NumberOfSections="1" 
  TimeDateStamp="-1"
  PointerToSymbolTable="-1"
  NumberOfSymbols = "-1"
  SizeOfOptionalHeader="0"
  Characteristics="0x104"
/>
```

## IMAGE SECTION HEADER ##
Member name: **image\_section\_header**

Attributes:
  * Name (max eight-character string)
  * Misc (value in hexadecimal, value in decimal)
  * Misc\_PhysicalAddress (value in hexadecimal, value in decimal)
  * Misc\_VirtualSize (value in hexadecimal, value in decimal)
  * VirtualAddress (value in hexadecimal, value in decimal)
  * SizeOfRawData (-1, value in hexadecimal, value in decimal)
  * PointerToRawData (-1, value in hexadecimal, value in decimal)
  * PointerToRelocations (-1, value in hexadecimal, value in decimal)
  * PointerToLinenumbers (not supported, 0)
  * NumberOfRelocations (-1, value in hexadecimal, value in decimal)
  * NumberOfLinenumbers (not supported, 0)
  * Characteristics (value in hexadecimal, value in decimal)

Sample:
```
<image_section_header
  Name=".text"
  Misc="0"
  Misc_PhysicalAddress = "0"
  Misc_VirtualSize = "0"
  VirtualAddress = "0"
  SizeOfRawData = "-1"
  PointerToRawData = "-1"
  PointerToRelocations = "-1"
  PointerToLinenumbers = "0"
  NumberOfRelocations = "-1"
  NumberOfLinenumbers = "0"
  Characteristics = "0x60000020" 
/>
```

## IMAGE SECTION ##
Member name: **image\_section**
  * Type ("file")
  * Filename (path to file)

Sample:
```
<image_section
  Type="file"
  Filename="foo.bin" 
/>
```

## IMAGE RELOCATION ##
Note: All addresses should point to value 0x0000 (in IMAGE SECTION)

Member name: **image\_relocation**

Attributes:
  * RVA (value in hexadecimal, value in decimal; addres to be corrected)
  * SymbolTableIndex (value in hexadecimal, value in decimal)
  * Type = (value in hexadecimal, value in decimal; two possible: 0x14 and 0x06)

Sample:
```
<image_relocation
  RVA = "0x0D"
  SymbolTableIndex = "7"
  Type = "0x14" 
/>
```

## IMAGE SYMBOL TABLE ##
Member name: **image\_symbol\_table\_item**

Attributes:
  * Name (max eight-character string)
  * Value (value in hexadecimal, value in decimal)
  * SectionNumber (value in hexadecimal, value in decimal)
  * Type (value in hexadecimal, value in decimal)
  * StorageClass (value in hexadecimal, value in decimal)
  * NumberOfAuxSymbols (value in hexadecimal, value in decimal)

Sample:
```
<image_symbol_table_item
  Name=".file"
  Value="0"
  SectionNumber = "0xFFFE"
  Type = "0"
  StorageClass = "0x67"
  NumberOfAuxSymbols = "1" 
/>
```


## IMAGE SYMBOL TABLE ##
**Removed!**






