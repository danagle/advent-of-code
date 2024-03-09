"""
Advent of Code 2019
Day 7: Amplification Circuit
https://adventofcode.com/2019/day/7
"""
from collections import deque
from itertools import permutations


class InputInterrupt(Exception):
    pass


class OutputInterrupt(Exception):
    pass


class IntCode:

    def mode_get(self, mode, operand):
        return operand if mode else self.memory[operand]

    def add_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = a + b
        self.instruction_ptr += 4

    def multiply_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = a * b
        self.instruction_ptr += 4

    def input_func(self, modes, operands):
        try:
            self.memory[operands[0]] = self.input_queue.popleft()
        except IndexError:
            raise InputInterrupt
        else:
            self.instruction_ptr += 2

    def output_func(self, modes, operands):
        self.output_queue.append(self.mode_get(modes[0], operands[0]))
        self.instruction_ptr += 2
        raise OutputInterrupt

    def jmp_true_func(self, modes, operands):
        if self.mode_get(modes[0], operands[0]):
            self.instruction_ptr = self.mode_get(modes[1], operands[1])
        else:
            self.instruction_ptr += 3

    def jmp_false_func(self, modes, operands):
        if not self.mode_get(modes[0], operands[0]):
            self.instruction_ptr = self.mode_get(modes[1], operands[1])
        else:
            self.instruction_ptr += 3

    def lt_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = int(a < b)
        self.instruction_ptr += 4

    def eq_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = int(a == b)
        self.instruction_ptr += 4

    def __init__(self, input_code):
        self.instructions = {
            1: self.add_func,
            2: self.multiply_func,
            3: self.input_func,
            4: self.output_func,
            5: self.jmp_true_func,
            6: self.jmp_false_func,
            7: self.lt_func,
            8: self.eq_func,
        }
        self.memory = input_code
        self.instruction_ptr = 0
        self.input_queue = deque()
        self.output_queue = deque()
        self.halted = False

    @staticmethod
    def instruction_parse(num, inputs):
        opcode = [num % 100]
        num //= 100
        for _ in range(inputs):
            opcode.append(num % 10)
            num //= 10
        return tuple(opcode)

    def run(self):
        while not self.halted:
            if (curr := self.memory[self.instruction_ptr]) % 100 == 99:
                self.halted = True
                break
            instruction = self.instructions[(curr % 100)]
            opcode = IntCode.instruction_parse(curr, 4)
            instruction(opcode[1:], self.memory[self.instruction_ptr+1:self.instruction_ptr+5])


def read_input_file():
    return list(map(int, open("input.txt", "r").read().strip().split(",")))


def part_one(amplifier_code):
    highest_signal = 0
    for phase_settings in permutations(range(5), 5):
        # Reset the input signal to zero
        signal = 0
        # Execute possible combination of phase settings
        for phase in phase_settings:
            amplifier = IntCode(amplifier_code[:])
            amplifier.input_queue = deque([phase, signal])
            while not amplifier.halted:
                try:
                    amplifier.run()
                except OutputInterrupt:
                    pass
            signal = amplifier.output_queue.popleft()
        # Keep the highest output signal
        highest_signal = max(highest_signal, signal)
    print(f"part_one: {highest_signal}")


def run_with_phase_settings(amplifier_code, phase_settings):
    amplifiers, index = list(), -1
    for phase in phase_settings:
        # Each amplifier gets its own copy of the code to run
        amplifiers.append(IntCode(amplifier_code[:]))
        # Provide the phase setting for the amplifier
        amplifiers[index].input_queue.append(phase)
    # Provide the input signal to the first amplifier
    amplifiers[0].input_queue.append(0)
    while True:
        # Next amplifier in the feedback loop
        index = (index + 1) % 5
        while not amplifiers[index].halted:
            try:
                amplifiers[index].run()
            except OutputInterrupt:
                # Feed amplifier's output signal to next amplifier's input
                amplifiers[(index + 1) % 5].input_queue.append(amplifiers[index].output_queue[-1])
                continue
            except InputInterrupt:
                break
        if all(map(lambda amp: amp.halted, amplifiers)):
            # All the amplifiers have halted
            break
    # The last output signal from amplifier E is sent to the thrusters
    return amplifiers[0].input_queue[-1]


def part_two(amplifier_code):
    max_thruster_signal = 0
    for phase_sequence in permutations(range(5, 10)):
        max_thruster_signal = max(max_thruster_signal, run_with_phase_settings(amplifier_code, phase_sequence))
    print(f"part_two: {max_thruster_signal}")


if __name__ == "__main__":
    int_code = read_input_file()
    part_one(int_code)
    part_two(int_code)
