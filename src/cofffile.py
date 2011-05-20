
__author__ = 'Bartlomiej Piekarski'
__version__ = '1.0.0'
__contact__ = 'bartlomiej.piekarski@gmail.com'


from xml.dom import minidom
import pefile
import time


class COFF:
    __IMAGE_SYMBOL_TABLE_format__ = ('IMAGE_SYMBOL_TABLE', (
                                                            '8s,Name',
                                                            'I,Value',
                                                            'H,SectionNumber',
                                                            'H,Type',
                                                            'c,StorageClass',
                                                            'c,NumberOfAuxSymbols'))
    
    __IMAGE_RELOCATION_format__ = ('IMAGE_RELOCATION', (
                                                       'I,RVA',
                                                       'I,SymbolTableIndex',
                                                       'H,Type'))
    
    def __init__(self, coff_xml=None, nr=0):
        
        if coff_xml is None:
            return
        
        self.image_section_headers = []
        self.image_sections = []
        self.image_relocations = []
        self.image_symbol_table = []
        
        self.__parse__(coff_xml, nr)
        self.__automatic_addresses__()
        
    def __parse__(self, file_name, nr=0):
        print "__parser__", "begin"
        xmldoc = minidom.parse(file_name)
        cofffile = xmldoc.getElementsByTagName("cofffile")[nr]
        
        # Image File Header
        image_file_header = cofffile.getElementsByTagName("image_file_header")[0]
        
        self.image_file_header = pefile.Structure(pefile.PE.__IMAGE_FILE_HEADER_format__)
        self.image_file_header.__unpacked_data_elms__ = (0, 0, 0, 0, 0, 0, 0)
        
        self.image_file_header.Machine = self.__parse_machine_type__(image_file_header.attributes['Machine'].value)
        self.image_file_header.NumberOfSections = int(image_file_header.attributes['NumberOfSections'].value, 0) 
        self.image_file_header.TimeDateStamp = int(image_file_header.attributes['TimeDateStamp'].value, 0)
        self.image_file_header.PointerToSymbolTable = int(image_file_header.attributes['PointerToSymbolTable'].value, 0) 
        self.image_file_header.NumberOfSymbols = int(image_file_header.attributes['NumberOfSymbols'].value, 0)
        self.image_file_header.SizeOfOptionalHeader = int(image_file_header.attributes['SizeOfOptionalHeader'].value, 0) 
        self.image_file_header.Characteristics = int(image_file_header.attributes['Characteristics'].value, 0)
        
        # Image Section Header
        image_section_headers = cofffile.getElementsByTagName("image_section_header")
        for image_section_header in image_section_headers:
            new_image_section_header = pefile.Structure(pefile.PE.__IMAGE_SECTION_HEADER_format__)
            new_image_section_header.__unpacked_data_elms__ = ('', 0, 0, 0, 0, 0, 0, 0, 0, 0)
        
            new_image_section_header.Name = str(image_section_header.attributes['Name'].value)
            new_image_section_header.Misc = int(image_section_header.attributes['Misc'].value, 0)
            new_image_section_header.Misc_PhysicalAddress = int(image_section_header.attributes['Misc_PhysicalAddress'].value, 0)
            new_image_section_header.Misc_VirtualSize = int(image_section_header.attributes['Misc_VirtualSize'].value, 0)
            new_image_section_header.VirtualAddress = int(image_section_header.attributes['VirtualAddress'].value, 0)
            new_image_section_header.SizeOfRawData = int(image_section_header.attributes['SizeOfRawData'].value, 0)
            new_image_section_header.PointerToRawData = int(image_section_header.attributes['PointerToRawData'].value, 0)
            new_image_section_header.PointerToRelocations = int(image_section_header.attributes['PointerToRelocations'].value, 0)
            new_image_section_header.PointerToLinenumbers = int(image_section_header.attributes['PointerToLinenumbers'].value, 0)
            new_image_section_header.NumberOfRelocations = int(image_section_header.attributes['NumberOfRelocations'].value, 0)
            new_image_section_header.NumberOfLinenumbers = int(image_section_header.attributes['NumberOfLinenumbers'].value, 0)
            new_image_section_header.Characteristics = int(image_section_header.attributes['Characteristics'].value, 0)
            
            self.image_section_headers.append(new_image_section_header)
        
        # Image sections
        image_sections = cofffile.getElementsByTagName("image_section")
        for image_section in image_sections:
            if(image_section.attributes['Type'].value.upper() == "FILE"):
                with open(image_section.attributes['Filename'].value, "rb") as f:
                    section_body = f.read()
                    self.image_sections.append(section_body)
                    
        # Image Relocation
        image_relocations = cofffile.getElementsByTagName("image_relocation")
        for image_relocation in image_relocations:
            new_image_relocation = pefile.Structure(self.__IMAGE_RELOCATION_format__)
            new_image_relocation.__unpacked_data_elms__ = (0, 0, 0)
            
            new_image_relocation.RVA = int(image_relocation.attributes['RVA'].value, 0)
            new_image_relocation.SymbolTableIndex = int(image_relocation.attributes['SymbolTableIndex'].value, 0)
            new_image_relocation.Type = int(image_relocation.attributes['Type'].value, 0)
            
            self.image_relocations.append(new_image_relocation)
        
        # Image Symbol Table
        image_symbol_table = cofffile.getElementsByTagName("image_symbol_table_item")
        for image_symbol_table_item in image_symbol_table:
            new_image_symbol_table_item = pefile.Structure(self.__IMAGE_SYMBOL_TABLE_format__)
            new_image_symbol_table_item.__unpacked_data_elms__ = ('', 0, 0, 0, 0, 0)
            
            new_image_symbol_table_item.Name = str(image_symbol_table_item.attributes['Name'].value)
            new_image_symbol_table_item.Value = int(image_symbol_table_item.attributes['Value'].value, 0)
            new_image_symbol_table_item.SectionNumber = int(image_symbol_table_item.attributes['SectionNumber'].value, 0)
            new_image_symbol_table_item.Type = int(image_symbol_table_item.attributes['Type'].value, 0)
            new_image_symbol_table_item.StorageClass = chr(int(image_symbol_table_item.attributes['StorageClass'].value, 0))
            new_image_symbol_table_item.NumberOfAuxSymbols = chr(int(image_symbol_table_item.attributes['NumberOfAuxSymbols'].value, 0))
            
            self.image_symbol_table.append(new_image_symbol_table_item)
            
        
        # Image Symbol String Table
        image_symbol_string_table = cofffile.getElementsByTagName("image_symbol_string_table")[0]
        
        self.image_symbol_string_table = pefile.Structure(pefile.PE.__StringTable_format__)
        self.image_symbol_string_table.__unpacked_data_elms__ = (0, 0, 0)
         
        self.image_symbol_string_table.Length = int(image_symbol_string_table.attributes['Length'].value, 0)
        self.image_symbol_string_table.ValueLength = int(image_symbol_string_table.attributes['ValueLength'].value, 0) 
        self.image_symbol_string_table.Type = int(image_symbol_string_table.attributes['Type'].value, 0) 
                    
        print "__parser__", "end"
        
    def __automatic_addresses__(self):
        print '__automatic_addresses__', 'begin'
        
        #Image File Header - Number Of Sections 
        if(self.image_file_header.NumberOfSections == -1):
            if(len(self.image_sections) != len(self.image_section_headers)):
                print "Automatic Addresses [WARN]: diffrent sizes of Image_Sections and Image_Section_Headers ( %d != %d )" % (len(self.image_sections), len(self.image_section_headers)) 
                
            self.image_file_header.NumberOfSections = len(self.image_section_headers)
            print "Automatic Addresses: Setted IMAGE_FILE_HEADER.NumberOfSections to %d (0x%X)" % (self.image_file_header.NumberOfSections, self.image_file_header.NumberOfSections)
            
        #Image File Header - Time Date Stamp
        if(self.image_file_header.TimeDateStamp == -1):
            self.image_file_header.TimeDateStamp = int(time.time())
            print "Automatic Addresses: Setted IMAGE_FILE_HEADER.TimeDateStamp to %d (0x%X)" % (self.image_file_header.TimeDateStamp, self.image_file_header.TimeDateStamp)
            
            # struct_image_file_header.sizeof() + struct_image_section_header.sizeof()
            
        #Image File Header - Pointer to Symbol Table (size of Image File Header + X * Image Section Header + Y * Section + Z * Relocations)
        if(self.image_file_header.PointerToSymbolTable == -1):
            self.image_file_header.PointerToSymbolTable = self.image_file_header.sizeof() + sum([item.sizeof() for item in self.image_section_headers]) + sum([len(item) for item in self.image_sections]) + sum([item.sizeof() for item in self.image_relocations])
            print "Automatic Addresses: Setted IMAGE_FILE_HEADER.PointerToSymbolTable to %d (0x%X)" % (self.image_file_header.PointerToSymbolTable, self.image_file_header.PointerToSymbolTable)
            
        #Image File Header - Number of Symbols
        if(self.image_file_header.NumberOfSymbols == -1):
            self.image_file_header.NumberOfSymbols = len(self.image_symbol_table)
            print "Automatic Addresses: Setted IMAGE_FILE_HEADER.NumberOfSymbols to %d (0x%X)" % (self.image_file_header.NumberOfSymbols, self.image_file_header.NumberOfSymbols)
        
        
        for section in range(len(self.image_section_headers)):
            #Image Section Header - Size Of Raw Data
            if(self.image_section_headers[section].SizeOfRawData == -1):
                self.image_section_headers[section].SizeOfRawData = len(self.image_sections[section])
                print "Automatic Addresses: Setted IMAGE_SECTION_HEADER[%d].SizeOfRawData to %d (0x%X)" % (section, self.image_section_headers[section].SizeOfRawData, self.image_section_headers[section].SizeOfRawData)
            
            #Image Section Header - Pointer to Raw Data (size of Image File Header + X * Image Section Header + len(Image Sections[:section])
            if(self.image_section_headers[section].PointerToRawData == -1):
                self.image_section_headers[section].PointerToRawData = self.image_file_header.sizeof() + sum([item.sizeof() for item in self.image_section_headers]) + sum([len(item) for item in self.image_sections[:section]])
                print "Automatic Addresses: Setted IMAGE_SECTION_HEADER[%d].PointerToRawData to %d (0x%X)" % (section, self.image_section_headers[section].PointerToRawData, self.image_section_headers[section].PointerToRawData)
            
            #Image Section Header - Pointer to Relocations (size of Image File Header + X * Image Section Header + len(Image Sections)
            if(self.image_section_headers[section].PointerToRelocations == -1):
                self.image_section_headers[section].PointerToRelocations = self.image_file_header.sizeof() + sum([item.sizeof() for item in self.image_section_headers]) + sum([len(item) for item in self.image_sections])
                print "Automatic Addresses: Setted IMAGE_SECTION_HEADER[%d].PointerToRelocations to %d (0x%X)" % (section, self.image_section_headers[section].PointerToRelocations, self.image_section_headers[section].PointerToRelocations)
                
            #Image Section Header - Pointer to Line Numbers - NOT YET
            # TODO
            
            #Image Section Header - Number of Relocations
            if(self.image_section_headers[section].NumberOfRelocations == -1):
                self.image_section_headers[section].NumberOfRelocations = len(self.image_relocations)
                print "Automatic Addresses: Setted IMAGE_SECTION_HEADER[%d].NumberOfRelocations to %d (0x%X)" % (section, self.image_section_headers[section].NumberOfRelocations, self.image_section_headers[section].NumberOfRelocations)
                
            #Image Section Header - Number of Line Numbers - NOT YET
            # TODO
        
        print '__automatic_addresses__', 'end'
        
    def __parse_machine_type__(self, value):
        if value in pefile.MACHINE_TYPE: 
            return pefile.MACHINE_TYPE[value]
        else:
            return int(value, 0)
        
    def write(self, filename):
        
        with open(filename, "wb") as f:
            f.write(self.image_file_header.__pack__())
            for image_section_header in self.image_section_headers:
                f.write(image_section_header.__pack__())
            for image_section in self.image_sections:
                f.write(image_section)
            for image_relocation in self.image_relocations:
                f.write(image_relocation.__pack__())
            for image_symbol_table_item in self.image_symbol_table:
                f.write(image_symbol_table_item.__pack__())
            f.write(self.image_symbol_string_table.__pack__())    
            
        
        
        
        
        
