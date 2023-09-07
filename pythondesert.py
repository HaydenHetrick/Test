def ask_dessert():
  dessert = input("Would you like the Dessert Menu? ")
  if dessert == "Yes" :
    print("Very well here is the dessert menu. ")
    print("Rose Water Rice Pudding, Tres Leches Cake, Kulfi, Bread Pudding, Beignets, ")
    dessert_choose = input("What dessert would you like? ")
    print(f"Great choice I will have the {dessert_choose} out right away ") 
  elif dessert == "No" :
    print("That's no problem here is the bill sir. ")
    
ask_dessert()
