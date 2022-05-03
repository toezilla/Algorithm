if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        object_code = ''
        operand = {"ADD":0, "ADDC":1, "SUB":2, "SUBC":3, "MOV":4, "MOVC":5, "AND":6, "ANDC":7, "OR":8, "ORC":9, "NOT":10, "MULT":12, "MULTC":13, "LSFTL":14, "LSFTLC":15, "LSFTR":16, "LSFTRC":17, "ASFTR":18, "ASFTRC":19, "RL":20, "RLC":21, "RR":22, "RRC":23}
        rA_except = ["MOV", "NOT"]

        assembly_code = list(input().split())

        tmp = bin(operand[assembly_code[0]])[2:]
        while len(tmp)<5:
            tmp = '0'+tmp
        object_code = object_code+tmp

        object_code = object_code+'0'

        tmp = bin(int(assembly_code[1]))[2:]
        while len(tmp)<3:
            tmp = '0'+tmp
        object_code = object_code + tmp
        if assembly_code[0] in rA_except:
            object_code = object_code+'000'
        else:
            tmp = bin(int(assembly_code[2]))[2:]
            while len(tmp)<3:
                tmp = '0'+tmp
            object_code = object_code+tmp
        if operand[assembly_code[0]]%2 == 0:
            tmp = bin(int(assembly_code[3]))[2:]+'0'
            while len(tmp)<4:
                tmp = '0'+tmp
            object_code = object_code + tmp
        else:
            tmp = bin(int(assembly_code[3]))[2:]
            while len(tmp)<4:
                tmp = '0'+tmp
            object_code = object_code + tmp
        print(object_code)