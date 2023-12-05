#!/usr/bin/python3
import os
import os.path
import sys


def _readHeader(file):
    """
    Reads the header of an AVR32 ELF file

    :param file: Path to file
    :return: Raw header data
    """
    with open(file, "rb") as fileIn:
        data = fileIn.read(52)
        return data


def _getSectionTableMeta(header):
    """
    Loads the section table metadata fron an ELF file.

    Table content according to:
    - https://refspecs.linuxbase.org/elf/gabi4+/ch4.sheader.html
    - https://wiki.osdev.org/ELF

    :param header: Raw header data
    :return: Section table metadata
    """
    data = header[32:36]
    start = int.from_bytes(data, byteorder="big")
    data = header[46:48]
    size = int.from_bytes(data, byteorder="big")
    data = header[48:50]
    number = int.from_bytes(data, byteorder="big")
    data = header[51:]
    nameEntry = int.from_bytes(data, byteorder="big")

    return {"offset": start, "entrySize": size, "entryCount": number, "nameEntry": nameEntry}


def _readSectionTable(file, offset, count, entrySize):
    """
    Reads a section table from an ELF file.

    :param entrySize: int
    :param count: int
    :param offset: int
    :param file: Path to file
    :type file: str
    """
    with open(file, "rb") as fileIn:
        fileIn.seek(offset, 0)
        data = fileIn.read(count * entrySize)

    return data


def _buildTable(rawTable, metadata):
    """
    Builds a section table data structure from the raw table data.

    Table content according to
    - https://refspecs.linuxbase.org/elf/gabi4+/ch4.sheader.html
    :param rawTable:
    :param metadata:
    :return:
    """
    table = []

    for i in range(0, metadata['entryCount']):
        entry = {}
        entryRaw = rawTable[i * metadata['entrySize']:i * metadata['entrySize'] + metadata['entrySize']]

        nameIndex = entryRaw[0:4]
        entry['nameIndex'] = int.from_bytes(nameIndex, byteorder="big")

        address = entryRaw[12:16]
        entry['address'] = int.from_bytes(address, byteorder="big")

        offset = entryRaw[16:20]
        entry['offset'] = int.from_bytes(offset, byteorder="big")

        size = entryRaw[20:24]
        entry['size'] = int.from_bytes(size, byteorder="big")

        table.append(entry)
    return table


def _readData(file, start, size):
    """
    Reads binary data from a file.

    :param file: str: Path to file to read
    :param start: int: Start offset
    :param size: int: Number of bytes to read
    :return: byte[]: Binary data
    """
    with open(file, "rb") as fileIn:
        fileIn.seek(start, 0)
        data = fileIn.read(size)
        return data


def _setSectionNames(table, file, nameSectionIndex):
    """
    Sets the name of a section table entry.

    :param table:
    :param file:
    :param nameSectionIndex:
    :return:
    """
    nameEntry = table[nameSectionIndex]
    data = _readData(file, nameEntry['offset'], nameEntry['size'])

    for entry in table:
        if entry['nameIndex'] == 0:
            continue
        index = entry['nameIndex']
        name = _readString(data, index)[0]
        entry['name'] = name


def _readString(data, index):
    """
    Reads a string from a binary array.

    :param data:
    :param index:
    :return:
    """
    string = b""
    while True:
        if index >= len(data):
            return -1
        newByte = data[index].to_bytes(1, "big")
        if newByte == b"\x00":
            string = str(string, "utf-8")
            return string, index
        string += newByte
        index += 1


def _getSectionTable(header, file):
    """
    Gets the section table from the binary file data.

    :param header:
    :param file:
    :return:
    """
    tableMeta = _getSectionTableMeta(header)
    rawTable = _readSectionTable(file, tableMeta['offset'], tableMeta['entryCount'], tableMeta['entrySize'])
    table = _buildTable(rawTable, tableMeta)
    _setSectionNames(table, file, tableMeta['nameEntry'])
    return table


def exportSections(sections, file):
    """
    Exports a section to a separate file.

    :param sections:
    :param file:
    :return:
    """
    headerData = _readHeader(file)
    sectionTable = _getSectionTable(headerData, file)
    sections = sections.split(",")
    for sec in sectionTable:
        if "name" in sec and sec['name'] in sections:
            print("[avr32elfdump] Exporting section '%s'" % sec['name'])
            if len(sections) > 1:
                suffix = True
            else:
                suffix = False
            _extractSection(sec, file, suffix)


def _extractSection(section, file, suffix):
    if suffix:
        outName = "binaries/%s_%s" % (os.path.basename(file), section['name'])
    else:
        outName = "binaries/%s" % (os.path.basename(file))

    data = _readData(file, section['address'] + section['offset'], section['size'])
    with open(outName, "wb") as fileOut:
        fileOut.write(data)


def _readSymboleTable(secTable, file):
    """
    Reads the symbol table from an ELF file

    :param secTable:
    :param file:
    :return:
    """

    symtabMeta = {}
    for sec in secTable:
        if "name" in sec and sec['name'] == ".symtab":
            symtabMeta = sec
            break

    data = _readData(file, symtabMeta['address'] + symtabMeta['offset'], symtabMeta['size'])

    symtab = []
    index = 0
    while index < symtabMeta['size']:
        symEntry = {}
        namePtr = data[index:index + 4]
        symEntry['namePtr'] = int.from_bytes(namePtr, byteorder="big")
        index += 4

        value = data[index:index +4]
        symEntry['address'] = int.from_bytes(value, byteorder="big")
        index += 4

        size = data[index:index + 4]
        symEntry['size'] = int.from_bytes(size, byteorder="big")
        index += 4

        info = data[index:index + 1]
        symEntry['info'] = int.from_bytes(info, byteorder="big")
        symEntry['type'] = int.from_bytes(info, byteorder="big")
        symEntry['type'] &= 0xf
        index += 1

        other = data[index:index + 1]
        symEntry['other'] = int.from_bytes(other, byteorder="big")
        index += 1

        st_shndx = data[index:index + 2]
        symEntry['st_shndx'] = int.from_bytes(st_shndx, byteorder="big")
        index += 2

        symtab.append(symEntry)

    return symtab


def _setSymboleNames(secTable, symTable, file):
    """
    Sets the symbole names in the section table object.

    :param secTable:
    :param symTable:
    :param file:
    :return:
    """
    strSec = {}
    for sec in secTable:
        if "name" in sec and sec['name'] == ".strtab":
            strSec = sec
            break

    data = _readData(file, strSec['address'] + strSec['offset'], strSec['size'])
    for entry in symTable:
        if entry['namePtr'] == 0:
            entry['name'] = ""
            continue
        string = _readString(data, entry['namePtr'])
        if string == -1:
            entry['name'] = ""
        else:
            entry['name'] = string[0]


def getSymbolTable(file):
    """
    Reads the symbole table from an AVR32 ELF file
    :param file: Path to ELF file
    :return: Symbole table
    """

    headerData = _readHeader(file)
    secTable = _getSectionTable(headerData, file)
    symTable = _readSymboleTable(secTable, file)
    _setSymboleNames(secTable, symTable, file)
    return symTable


def _main():
    # Export section that is given after the '-e' switch
    if "-e" in sys.argv:
        exportSections(sys.argv[-1], sys.argv[-2])
    # List symbols in ELF file
    elif "-s" in sys.argv:
        syms = getSymbolTable(sys.argv[-1])
        for sym in syms:
            print(f"0x%08x: %s" % (sym['address'], sym['name']))


if __name__ == '__main__':
    _main()
