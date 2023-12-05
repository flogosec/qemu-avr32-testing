# QEMU AVR32 Testing Framework
This framework can be used to test the implementation of AVR32 CPU instructions in [QEMU-AVR32](https://github.com/flogosec/qemu-avr32).

## Installation
Clone the repo.
```shell
git clone https://github.com/flogosec/qemu-avr32-testing.git
```

Download the AVR32 assembler from the [Atmel website](https://www.microchip.com/en-us/tools-resources/develop/microchip-studio/gcc-compilers).
Place the *avr32-as* file in the project directory.

## Usage
The testing script provides the following options.

### Execute a single test
```shell
./avr32test.py -p [path to QEMU-AVR32 binary] --build -t [name of test file]
```
The *--build* option is needed to first assemble the test binary.

### Execute multiple tests
```shell
./avr32test.py -p [path to QEMU-AVR32 binary] --build -t [substring]
```
The *substring* can be replaced with the start of a test name. All tests startring with this substring will be executed.

### Execute all tests
```shell
./avr32test.py -p [path to QEMU-AVR32 binary] --build --all
```

### Show debug output
```shell
./avr32test.py -p [path to QEMU-AVR32 binary] --build --all -d
```
This shows the registers contents after each test, next to the expected results.

## Add ing new tests
I posted an article on my blog that describes how new tests can be added.
[See here](https://fgoehler.com/blog/adding-a-new-architecture-to-qemu-05/).

