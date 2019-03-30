def to_binary():
    pass


class MipsAssembler:
    def __init__(self,reg_map):
        self.reg_map=dict(reg_map)
        self.map_instructions = dict()


    def read_file(self):
        pass

    def write_file(self):
        pass

    def labels_mapping(self):
        pass

    def registers_mapping(self):
        reg_map = {
          "$zero": "00000",
          "$at": "00001",
          "$v0": "00010",
          "$v1": "00011",
          "$a0": "00100",
          "$a1": "00101",
          "$a2": "00110",
          "$a3": "00111",
          "$t0": "01000",
          "$t1": "01001",
          "$t2": "01010",
          "$t3": "01011",
          "$t4": "01100",
          "$t5": "01101",
          "$t6": "01110",
          "$t7": "01111",
          "$t8": "11000",
          "$t9": "11001",
          "$s0": "10000",
          "$s1": "10001",
          "$s2": "10010",
          "$s3": "10011",
          "$s4": "10100",
          "$s5": "10101",
          "$s6": "10110",
          "$s7": "10111",
          "$k0": "11010",
          "$k1": "11011",
          "$gp": "11100",
          "$sp": "11101",
          "fp": "11110",
          "$ra": "11111"
        }

    def instructions_mapping(self):
        self.map_instructions = {
         "add": ["000000", "100000", "R"],
         "and": ["000000", "10100", "R"],
         "sub": ["000000", "100010", "R"],
         "nor": ["000000", "100111", "R"],
         "or": ["000000", "100101", "R"],
         "slt": ["000000", "101010", "R"],
         "addi": ["001000", "none", "I"],
         "lw": ["100011", "none", "I"],
         "sw": ["101011", "none", "I"],
         "beq": ["000100", "none", "I"],
         "bne": ["000101", "none", "I"],
         "j": ["000010", "none", "J"]}

    def assembler(self):
        pass


