def int_to_romans(num):
    """
        Function converting a number to Roman Number

        int_to_romans(int->number)
    """
    numbers=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romans= ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    inttoromandict = {}
    for i in range(len(numbers)):
        inttoromandict[numbers[i]]=romans[i]

    if num in inttoromandict:
        return inttoromandict[num]
    else:
        roman = ''
        while(num>0):
            myvalues  = [key for key in inttoromandict.keys() if key <= num]
            if num >= myvalues[-1]:
                roman+=inttoromandict[myvalues[-1]]
                # print(num)
                num-=myvalues[-1]
        return roman


def romans_to_int(rom):
    """
        Function converting a Roman Number to Number
        
        romans_to_int(int->number)
    """
    numbers=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romans= ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    roman_to_int_dict = {}
    for i in range(len(numbers)):
        roman_to_int_dict[romans[i]]=numbers[i]
    # return roman_to_int_dict
    if rom.upper() in roman_to_int_dict:
        return roman_to_int_dict[rom]
    else:
        int_ans=0
        rom=rom.upper()
        for k in range(len(rom)-1):
            if roman_to_int_dict[rom[k]]<roman_to_int_dict[rom[k+1]]:
                int_ans+=roman_to_int_dict[rom[k+1]]-roman_to_int_dict[rom[k]]
            else:
                int_ans+=roman_to_int_dict[rom[k]]
        return int_ans


print(int_to_romans(3304))
print(romans_to_int('MMMCCCIV'))
