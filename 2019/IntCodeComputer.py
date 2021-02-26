class IntCodeComputer:
    def __init__(self):
       self.program = list()
       self.pos = 0 

    
    def __get_param(self, mode_bits, num):
        """
        Utility method. 
        For the specified parameter (1, 2, or 3) given by `num`,
            use the corresponding mode bit to get the correct value. 

            * 1 corresponds to "immedaite mode"
            * 0 corresponds to "position mode"
        """

        if num==1 and mode_bits[-1] == '1':
            return self.program[self.pos+1]
        if num==1 and mode_bits[-1] == '0':
            return self.program[self.program[self.pos+1]]

        if num==2 and mode_bits[-2] == '1':
            return self.program[self.pos+2]
        if num==2 and mode_bits[-2] == '0':
            return self.program[self.program[self.pos+2]]

        if num==3 and mode_bits[-3] == '1':
            return self.program[self.pos+3]
        if num==3 and mode_bits[-3] == '0':
            return self.program[self.program[self.pos+3]]

    def run_program(self):
        """
        Actually executes the program
        """

        while self.program[self.pos] != 99:
            opcode = self.program[self.pos]
            mode_bits = "000"
            # print(f"Operation: {opcode}")

            if opcode > 99: # handle modes
                mode_bits = str(opcode)[:-2]
                mode_bits = mode_bits.rjust(3,'0')
                opcode = int(str(opcode)[-2:])
                # print(opcode, mode_bits)

            if opcode == 1: # addition            
                val = self.__get_param(mode_bits, 1) + self.__get_param(mode_bits, 2)
                store = self.program[self.pos+3]
                self.program[store] = val
                # print(f"stored {val} into position {store}")
                self.pos += 4

            elif opcode == 2: # multiplication
                val = self.__get_param(mode_bits, 1) * self.__get_param(mode_bits, 2)
                store = self.program[self.pos+3]
                self.program[store] = val
                # print(f"stored {val} into position {store}")
                self.pos += 4

            elif opcode == 3: # input
                val = int(input('>'))
                store = self.program[self.pos+1]
                self.program[store] = val
                self.pos += 2

            elif opcode == 4: # output
                val = self.__get_param(mode_bits, 1)
                print(val)
                self.pos += 2
            
            elif opcode == 5: # jump if true
                val = self.__get_param(mode_bits,1)
                if val != 0:
                    self.pos = self.__get_param(mode_bits,2)
                else: 
                    self.pos += 3
            
            elif opcode == 6: # jump if false
                val = self.__get_param(mode_bits,1)
                if val == 0:
                    self.pos = self.__get_param(mode_bits,2)
                else: 
                    self.pos += 3

            elif opcode == 7: # less than
                val1 = self.__get_param(mode_bits, 1)
                val2 = self.__get_param(mode_bits, 2)
                loc = self.program[self.pos+3]
                if val1 < val2:
                    self.program[loc] = 1
                else: 
                    self.program[loc] = 0
                self.pos += 4
            
            elif opcode == 8: # equals
                val1 = self.__get_param(mode_bits, 1)
                val2 = self.__get_param(mode_bits, 2)
                loc = self.program[self.pos+3]
                if val1 == val2:
                    self.program[loc] = 1
                else: 
                    self.program[loc] = 0
                self.pos += 4