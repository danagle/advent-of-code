from math import prod


def read_input_file():
    modules_list = []  # [(name, type, [destinations])]
    for line in open('input.txt'):
        module_source, destinations = line.split(" -> ")
        module_type, module_name = (module_source[0], module_source[1:]) if module_source[0] in "%&" else ("", module_source)
        modules_list.append((module_name, module_type, destinations.strip().split(", ")))
    return modules_list


class Module:
    def __init__(self, module_tuple):
        module_name, module_type, destinations = module_tuple
        self.name = module_name
        self.type = module_type
        self.state = False
        self.destinations = destinations
        self.inputs = {}


class Network:
    def __init__(self, modules_list):
        self.modules = {m.name: m for m in map(Module, modules_list)}
        # Add 'rx' module to network
        self.modules["rx"] = Module(("rx", "", []))
        for module in self.modules.values():
            for destination in module.destinations:
                self.modules[destination].inputs[module.name] = False
        self.pulses = [0, 0]
        self.button_presses = 0
        self.queue = []
        # Additional properties for Part 2
        self.rx_parent = "".join(self.modules["rx"].inputs.keys())
        self.rx_inputs = {name: 0 for name in self.modules[self.rx_parent].inputs.keys()}

    def button_press(self):
        self.button_presses += 1
        self.queue = [("button", "broadcaster", False)]
        while self.queue:
            self.process_signal(*self.queue.pop(0))

    def process_signal(self, input_source, module_name, signal_level):
        module = self.modules[module_name]
        self.pulses[signal_level] += 1
        if "%" == module.type:
            if signal_level:
                return
            module.state = not module.state
        elif "&" == module.type:
            module.inputs[input_source] = signal_level
            module.state = not all(module.inputs.values())
            if module_name == self.rx_parent:
                for name, button_presses in self.rx_inputs.items():
                    if button_presses == 0 and name == input_source and signal_level:
                        self.rx_inputs[name] = self.button_presses
        for destination in module.destinations:
            self.queue.append((module_name, destination, module.state))

    def part_one_answer(self):
        return prod(self.pulses)

    def part_two_answer(self):
        return prod(self.rx_inputs.values())


def part_one(network):
    # Simulate 1,000 button presses
    for _ in range(1000):
        network.button_press()
    return network.part_one_answer()


def part_two(network):
    # Simulate button presses until all 'rx' input modules have sent a pulse
    while 0 in network.rx_inputs.values():
        network.button_press()
    return network.part_two_answer()


if __name__ == '__main__':
    from time import time

    modules = read_input_file()
    modules_network = Network(modules)

    st = time()
    p1 = part_one(modules_network)
    p2 = part_two(modules_network)
    print(f"Execution Time : {time() - st}")
    print(f"Part 1 : {p1}")
    print(f"Part 2 : {p2}")