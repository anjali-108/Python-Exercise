print("************ Smart-Home Climate Monitoring System ************")

status = input("Enter Atmospheric status: ").lower()

if status == "hot":
    print("Atmospheric Status: Hot")
    print("Hardware Recommendation: Turn on AC")

elif status == "cold":
    print("Atmospheric Status: Cold")
    print("Hardware Recommendation: Activate heater")

elif status == "comfortable":
    print("Atmospheric Status: Comfortable")
    print("Hardware Recommendation: Idle")

else:
    print("Invalid status! Enter Hot, Cold, or Comfortable.")
