string=input("Enter the Alphabet : ")

string=string.lower();

match string:
			case "a" | "e" | "i" | "o" | "u" :
				print("Given Alphabet is Owel !!")

			case _:
				print("Given Alphabet is no Owel !!")
			