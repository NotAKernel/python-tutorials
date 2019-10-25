ask = input("How old are you? ")
cost = ""
while True:
    cost = ""
    ticket_cost = int(ask)
    
    if ticket_cost < 3:
        cost = 'free'
    if ticket_cost < 12:
        cost = '$10'
    if ticket_cost >= 12:
        cost = '$15'

    print("Your ticket is .")
    break
        