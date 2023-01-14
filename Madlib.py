print("Madlib Project by Muhammad\n\n")
print("Theres V1 and V2 of this Madlib, Pick one.")
VWhat = input("Whch version of Madlib do you want?\n")



if VWhat.lower() == "v1" or VWhat.lower() == "first" or VWhat.lower() == "1":
    name = input("Enter a name\n")
    hobby = input("Enter a Hobby\n")

    print("My name is " + name + ", and my hobby is " + hobby + ".")

if VWhat.lower() == "v2" or VWhat.lower() == "second" or VWhat.lower() == "2":
    name2 = input("Enter name\n")
    wake_in = input("Enter a place\n")
    srrounders = input("Enter Something that will Surrounding you\n")

    print(name2.title() + " woke up in " + wake_in + " with " + srrounders + " Surrounding " + name2 + ".")

