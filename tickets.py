def tickets(people):
    cash_register = {25:0, 50:0}
    for person in people:
        if person == 25:
            cash_register[25] += 1
        if person == 50:
            cash_register[50] += 1
            cash_register[25] -= 1
        if person == 100:
            if cash_register[50] > 0:
                cash_register[50] -= 1
                cash_register[25] -= 1
            else:
                cash_register[25] -= 3
    if cash_register[25] >= 0 and cash_register[50] >= 0:
        return "YES"
    return "NO"

if __name__=='__main__':
    print(tickets([25,25,50]))
    print(tickets([25,100]))
