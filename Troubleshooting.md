# Introduction #

Basic problems with COFF files.

This XMLs are from [SampleFunctionWithRelocation](SampleFunctionWithRelocation.md)

### Machine="IMAGE\_FILE\_MACHINE\_I386\_qwe" ###

XML:
```
<image_file_header Machine="IMAGE_FILE_MACHINE_I386_qwe" NumberOfSections="-1" TimeDateStamp="-1" PointerToSymbolTable="-1" NumberOfSymbols = "-1" SizeOfOptionalHeader="0" Characteristics="0x104" />
```
build.py output:
```
ValueError: invalid literal for int() with base 0: 'IMAGE_FILE_MACHINE_I386_qwe'
```

### Name\_qwe=".file" ###

XML:
```
<image_symbol_table_item Name_qwe=".file" Value="0" SectionNumber = "0xFFFE" Type = "0" StorageClass = "0x67" NumberOfAuxSymbols = "1" />
```
build.py output:
```
KeyError: 'Name'
```

### Filename="foo\_qwe.bin" (There is no such file) ###

XML
```
<image_section Type="file" Filename="foo_qwe.bin" />
```
build.py output:
```
IOError: [Errno 2] No such file or directory: u'foo_qwe.bin'
```

### SymbolTableIndex = "10" (out of range) ###

XML
```
<image_relocation RVA = "0x0D" SymbolTableIndex = "10" Type = "0x14" />
```
Compilation:
```
>gcc -o main main.c foo.o
C:\Dev-Cpp\bin\..\lib\gcc\mingw32\3.4.2\..\..\..\..\mingw32\bin\ld.exe: foo.o: illegal symbol index 10 in relocs
collect2: ld returned 1 exit status
```

### Type = "0x24" (possible 0x14 or 0x06) ###

XML
```
<image_relocation RVA = "0x0D" SymbolTableIndex = "7" Type = "0x24" />
```
Compilation:
```
>gcc -o main main.c foo.o
C:\Dev-Cpp\bin\..\lib\gcc\mingw32\3.4.2\..\..\..\..\mingw32\bin\ld.exe: final link failed: Bad value
collect2: ld returned 1 exit status
```

### SectionNumber = "2"  (In this sample is only one section) ###

XML:
```
<image_symbol_table_item Name="_foo" Value="0" SectionNumber = "2" Type = "0x20" StorageClass = "2" NumberOfAuxSymbols = "0" />
```
Compilation:
```
>gcc -o main main.c foo.o
C:\DOCUME~1\User\USTAWI~1\Temp/ccmUaaaa.o(.text+0x64):main.c: undefined reference to `foo'
collect2: ld returned 1 exit status
```




