
print("Match is like Switch in other languages.")

day = 4

match day :
    case 1:
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6: 
        print("Saturday")
    case 7: 
        print("Sunday")

print("Default value _")

match day :
    case 6 :
        print("Today is Saturday")
    case 7 :
        print("Today is Sunday")
    case _ :
        print("Look forward to the weekend")

print("Match multiple values")

match day :
    case 1 | 2 | 3 | 4 | 5 :
        print("Working for the weekend!")
    case 6 | 7 :
        print("Yay weekend!")

print("Additional 'if' checks.")

month = 5
day = 4
match day :
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("April weekday")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("May weekday")
        