#!/usr/bin/python3
import datetime
import os
import shlex
import subprocess
import sys
from colorama import Fore, Style
import avr32generate_tests

expectedResults = {}
DEBUG = False
QEMU_COMMAND = "-M avr32example-board -d cpu -nographic -bios binaries/%s"
QEMU_PATH = ""


def loadExpectedResults(name):
    """
    Loads the expected results for a test from an s-file.

    :param name: String: Test name
    :return: Array with expected register values
    """

    global expectedResults
    # Dynamically import the expected result dict
    string = f'from tests import %s' % name
    exec(string)
    # Dynamically get expected result dict from imported file
    string = "global expectedResults; expectedResults = %s.EXPECTED_RESULTS" % name
    exec(string)
    return expectedResults


def stopTest(process):
    process.kill()


def startTest(name):
    """
    Starts QEMU with the specified test

    :param name: String: Testname
    :return:
    """
    if not os.path.isfile("binaries/%s" % name):
        print("ERROR: test %s does not exist!" % name)
        sys.exit(1)

    command = QEMU_PATH + QEMU_COMMAND % name
    command = shlex.split(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process


def parseTestResult(resultText):
    """
    Parses the raw QEMU output into a result array
    :param resultText: String[]
        Raw output lines from QEMU
    :return: Result array
    """

    lines = resultText.split("\n")
    result = {}
    for line in lines:
        line = line.lstrip().rstrip()
        line = line.replace(" ", "")
        if ":" in line and "qemu" not in line:
            parts = line.split(":")
            result[parts[0]] = int(parts[1], base=16)
    return result


def compareResults(result, expected, name):
    """
    Copares the result of a test with the expected values.

    :param result: Array
        The QEMU output for a test
    :param expected: Array
        The expected register values for a test.
    :param name: String
        The name of the test
    :return: Bool
        True, if comparison is true, false otherwise.
    """

    global DEBUG
    passed = True
    # Only print PC, LR and SP reg values if in debug mode.
    try:
        if DEBUG and "PC" not in expected.keys():
            print("%-08s 0x%08x - 0x%08x" % ("PC" + ":", 0, result["PC"]))
        if DEBUG and "SP" not in expected.keys():
            print("%-08s 0x%08x - 0x%08x" % ("SP" + ":", 0, result["SP"]))
        if DEBUG and "LR" not in expected.keys():
            print("%-08s 0x%08x - 0x%08x" % ("LR" + ":", 0, result["LR"]))
    except KeyError:
        print("Key Error!")
        pass
    print()
    for key, value in expected.items():
        # If expected register is not in results there must be an error, exit.
        if key not in result:
            print("ERROR: missing register '%s' in %s!" % (key, name))
            print(result)
            sys.exit(1)
        # Value mismatch, test failed.
        if result[key] != expected[key]:
            passed = False
            if DEBUG:
                print(Fore.RED + f"%-08s 0x%08x - 0x%08x{Style.RESET_ALL}" % (key + ":", expected[key], result[key]))
        else:
            # Print values only if in debug mode.
            if DEBUG and expected[key] != 0x0:
                print(Fore.GREEN + f"%-08s 0x%08x - 0x%08x{Style.RESET_ALL}" % (key + ":", expected[key], result[key]))
            elif DEBUG:
                print("%-08s 0x%08x - 0x%08x" % (key + ":", expected[key], result[key]))

    return passed


def performTest(testName):
    """
    Handles test execution and result evaluation.

    :param testName: String
        Name of test to perform
    :return: True if test was successful, False otherwise
    """

    global expectedResults
    loadExpectedResults(testName)
    testProcess = startTest(testName)
    # Wait for QEMU to end test execution
    try:
        testProcess.wait(5)
    except:
        testProcess.kill()
        print("[ERROR] Emulator killed!")

    # Read stdio output form QMEU
    data = testProcess.communicate()[1].decode()
    testProcess.kill()
    result = parseTestResult(data)
    successful = compareResults(result, expectedResults, testName)
    return successful


def _main():
    global DEBUG, QEMU_PATH

    # Verify that QEMU path is set
    if "-p" in sys.argv:
        QEMU_PATH = sys.argv[sys.argv.index("-p") + 1]
        if not QEMU_PATH.endswith(" "):
            QEMU_PATH += " "
    else:
        print("Specify QEMU path with '-p'")
        sys.exit(1)

    # Set debug flag. This enables the printing of all result values, including colored output.
    if "-d" in sys.argv:
        DEBUG = True

    tests = sorted(os.listdir("tests/"))

    # Check what test should be executed
    # Execute all tests
    if "--all" in sys.argv:
        specificTests = False
    # A specific (group of) test(s) was given
    elif "-t" in sys.argv:
        specificTests = sys.argv[sys.argv.index("-t") + 1]
    # No argument was set, exit
    else:
        print("Specify test name with '-t' or set '--all'")
        sys.exit(1)

    buildTests = "--build" in sys.argv

    starteTime = datetime.datetime.now()
    print("Starting execution at %s" % '{0:%Y-%m-%d %H:%M:%S}'.format(starteTime))
    for file in tests:
        if os.path.isfile("tests/" + file):
            testName = (os.path.basename(file)[:-3])
            # Skip non-matching tests, if a test name was given
            if specificTests and specificTests not in testName:
                continue

            # Generate tests, if --build was set
            if buildTests:
                if DEBUG:
                    print("[avr32test] Preparing test %s" % testName)
                avr32generate_tests.generateTest(file)
            if DEBUG:
                print("[avr32test] Starting test %s" % testName)

            # Execute tests
            testResult = performTest(testName)
            if testResult:
                print(Fore.GREEN + f"%-08s %s{Style.RESET_ALL}" % ("[%s]" % testName, Style.BRIGHT + "PASSED"))
            else:
                print(Fore.RED + f"%-08s %s{Style.RESET_ALL}" % ("[%s]" % testName, Style.BRIGHT + "FAILED"))

    endTime = datetime.datetime.now()
    print("Execution ended at %s" % '{0:%Y-%m-%d %H:%M:%S}'.format(endTime))
    print("Duration: %d seconds" % (endTime-starteTime).total_seconds())


if __name__ == '__main__':
    _main()
