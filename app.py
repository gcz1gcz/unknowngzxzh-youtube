print("Title of program: Youtube channel promotion")
print()
while True:
  description = input("Could you describe have you subscribed to @unknowngczxzh in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "yes":
      feelings_list.append("yes")
      encouragement_list.append("tomorrow will be a better day as there will be more subs")
      counter += 1
    if each_word == "no":
      feelings_list.append("no")
      encouragement_list.append("susbcribe now")
      counter += 1
    if each_word == "i don't know":
      feelings_list.append("i don't know")
      encouragement_list.append("it's okay, you can search up")
      counter += 1

  if counter == 0:
    
      output = "speak to chenzhang"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
