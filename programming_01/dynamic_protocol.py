"""
File   :  dynamic_protocol.py
Instruct user how to prepare a solution of
NaCl and MgCl2, given stock solutions
of NaCl and MgCl2.
 """

def main():
    """Business logic"""
    final_vol = float(input("Please enter the final volume of the solution (ml): "))

    # NaCl
    nacl_stock = float(input("Please enter the Nacl stock (mM): "))
    nacl_final = float(input("Please enter the Nacl final (mM): "))

    # concatenation
    step1 = f"Add {str(final_vol * (nacl_final / nacl_stock))} ml NaCl\n"

    # MgCl2
    mg_stock = float(input("Please enter MgCl2 stock (mM): "))
    mg_final = float(input("Please enter the Mgcl2 final (mM): "))

    step2 = f"Add {str(final_vol * (mg_final / mg_stock))} ml MgCl2\n"

    # Water
    step3 = f"Add water to a final volume of {str(final_vol)} ml and mix"

    # Protocol, we can then just print things out b/c they have been formatted earlier
    print(step1 + step2 + step3)

if __name__ == '__main__':
    main()
