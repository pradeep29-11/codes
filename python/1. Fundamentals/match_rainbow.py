colour=input("Enter the colour : ")

colour=colour.lower()

match colour:
		case "red" | "orange" | "yellow" | "green" | "blue" | "indigo" | "voilet" :
			print(colour,"is the Rainbow colour ")
		case _:
			print(colour,"is not a Rainbow colour ")
			