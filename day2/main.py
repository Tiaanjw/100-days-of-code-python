print("Welcome to the tip calculator")

bill = int(input("What is the total? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to add? "))
per_person_total = bill / people * (tip/100 + 1)
per_person_total = "{:.2f}".format(per_person_total)

print(f"Total per person: ${per_person_total}")