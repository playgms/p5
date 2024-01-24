
def mc_pits(i1,i2,logic_gate):
    if logic_gate =="AND":
        return i1 and i2
    if logic_gate=="OR":
        return i1 or i2
    if logic_gate=="XOR":
        return i1!=i2
    if logic_gate=="ANDNOT":
        return i1 and not i2
    else:
        print("Invalid")
        return None
    
i1=int(input("Enter input1(0 or 1):"))
i2=int(input("Enter input2(0 or 1):"))

and_result=mc_pits(i1,i2,"AND")
or_result=mc_pits(i1,i2,"OR")
xor_result=mc_pits(i1,i2,"XOR")
andnot_result=mc_pits(i1,i2,"ANDNOT")

print(f"AND {and_result}")
print(f"OR {or_result}")
print(f"XOR {xor_result}")
print(f"ANDNOT {andnot_result}")
