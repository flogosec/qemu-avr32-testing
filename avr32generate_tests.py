#!/usr/bin/python3

import os
import shlex
import subprocess
import sys

import avr32elfdump

# Inserted at the start of every test s-file
preamble = """.section .text
.global main
main:
#Test start
"""

# Appended after every test into the s-file
postamble = """
# Postamble
bral end

end:
mov r0, 0x0
"""

currentTest = ""


def loadTest(testFile):
    """
    Loads a test definition file

    :param testFile: path to test file
    :return:
    """

    print("[avr32generate_tests] Loading test %s" % testFile)
    global currentTest
    # Dynamically import test definition file
    string = f'from tests import %s' % testFile
    exec(string)
    currentTest = ""
    # Dynamically get test code
    string = "global currentTest; currentTest = %s.TEST" % testFile
    exec(string)


def writeSFile(file):
    """
    Writes assembler code for test to s-file

    :param file: String: Output file
    :return:
    """

    global currentTest
    print("[avr32generate_tests] Writing sfile %s" % file)
    with open("%s.s" % file, "w") as fileOut:
        fileOut.write(preamble)
        testContent = currentTest.split("\n")
        for line in testContent:
            if line.lstrip().rstrip().startswith("#") or len(line) < 2:
                continue
            fileOut.writelines("%s\n" % line)
        fileOut.write(postamble)


def assembleTest(testName, elfDir):
    """
    Generates ELF-File from s-file

    :param testName: Name of test
    :param elfDir: path to dir with ELF files
    :return: Path to ELF file
    """

    if not os.path.isdir(elfDir):
        os.mkdir(elfDir)
    elfFile = "%s" % (elfDir + testName)
    command = "./avr32-as -o %s sfiles/%s.s" % (elfFile, testName)
    command = shlex.split(command)
    print("[avr32generate_tests] Assembling test %s: %s" % (testName, subprocess.list2cmdline(command)))
    process = subprocess.Popen(command, env=dict(LC_ALL='C', **os.environ))
    process.wait()
    # data = process.communicate()[0]
    result = process.returncode
    # Return code != 0 => error
    if result:
        print("[avr32generate_tests] ERROR: %d" % result)
        sys.exit(1)

    return elfFile


def exportTextSection(elfFile):
    """
    Exports the text section of an ELF file

    :param elfFile:
    :return:
    """

    if not os.path.isdir("binaries"):
        os.mkdir("binaries")
    avr32elfdump.exportSections(".text", elfFile)


def generateTest(testFile):
    """
    Generates a binary file for a test.

    :param testFile: Path to test file
    :return:
    """

    testName = testFile[:-3]
    loadTest(testName)
    if not os.path.isdir("sfiles"):
        os.mkdir("sfiles")
    writeSFile("sfiles/" + testName)
    elfFile = assembleTest(testName, "elf-files/")
    exportTextSection(elfFile)


def _generateTests(testDir):
    """
    Generates all tests in the specified folder.

    :param testDir: path to folder with tests
    :return:
    """
    for entry in os.scandir(testDir):
        if entry.is_file():
            generateTest(entry)


def _main():
    # If script is called on its own, generate all tests.
    for file in os.listdir("../qemu-avr32-testing_public/tests"):
        if os.path.isfile("tests/" + file):
            _generateTests("tests/")


if __name__ == '__main__':
    _main()
