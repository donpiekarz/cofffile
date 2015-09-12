Python module for manipulating on the [COFF](http://en.wikipedia.org/wiki/COFF) file.

Why?

To [easily](BasicSample.md) build your binary code (from x86 assembly without headers, IDA Pro, PE files) with other high level code.

Main features:
  * Build the COFF file from XML file.
  * Automatic calculations pointers and sizes.
  * Support for relocations

In the future:
  * Possibility creating XMLs from binary COFF files.
  * New members in XML (String Table, Optional Header, Line Numbers)



It needs [pefile](http://code.google.com/p/pefile/) module.

This is tested on Windows XP (win32) and gcc (gcc version 3.4.2 (mingw-special))