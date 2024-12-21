
def hide():
    cn = str(input("enter 16 digit num: "))
    if 16 < len(cn) < 16:
        print("wrong lenght")
    else:    
        hcn = cn.replace(cn[3:13],"**********")
        print(hcn)
  