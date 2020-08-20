import os
import pyttsx3

pyttsx3.speak("WELCOME TO IIEC RISE")
print("\n ..................WELCOME TO IIEC RISE................ \n \n PLEASE CHECK THE DETAILS BELOW AND TELL US YOUR REQUIREMENTS")
pyttsx3.speak("WHAT CAN WE DO FOR YOU")
#x = [["run","open","play","execute","start","launch"],["quit","exit","dont","never"]]

while True:
	print("\n DETAILS :: \n 1. CHAT OR TYPE YOUR REQUIREMENTS \n 2. DISPLAY THE LIST AND SELECT REQUIREMENTS SUITABLE FOR YOU \n 3. EXIT \n")
	oneinp = int(input(">>>>> \t"))

	if oneinp==1:
		while True:
			print("\n Hi...PLEASE CAN YOU SPECIFY YOUR REQUIREMENTS \n IF YOU WANT TO EXIT ....PLEASE TYPE QUIT OR EXIT \n")
			toinp = input(">>>> \t")
			toinp = toinp.lower()
			if ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("chrome" in toinp)or ("google" in toinp) or ("browser" in toinp))):
				print("\n ........OPENING CHROME........")
				os.system("start chrome")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("firefox" in toinp) or ("fox" in toinp)or ("browser" in toinp))):
				print("\n ........OPENING FIREFOX........")
				os.system("start firefox")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and ("notepad" in toinp)):
				print("\n ........OPENING NOTEPAD........")
				os.system("start notepad")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("player" in toinp) or ("media" in toinp) or("wmp" in toinp)or("windowsplayer" in toinp))):
				print("\n ........OPENING MEDIA PLAYER........")
				os.system("start wmplayer")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("calculator" in toinp) or ("calci" in toinp) or ("calcu" in toinp))):
				print("\n ........OPENING CALCULATOR........")
				os.system("start calc")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("powerpoint" in toinp) or ("po" in toinp) or ("power" in toinp))):
				print("\n ........OPENING MICROSOFT POWERPOINT........")
				os.system("start POWERPNT")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("excel" in toinp) or ("ex" in toinp))):
				print("\n ........OPENING MICROSOFT EXCEL........")
				os.system("start EXCEL")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("word" in toinp) or ("ms word" in toinp) or ("microsoft" in toinp))):
				print("\n ........OPENING MICROSOFT WORD........")
				os.system("start WINWORD")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("python" in toinp) or ("py" in toinp))):
				print("\n ........OPENING PYTHON INTERPRETER........")
				os.system("start python")
			elif ((("run" in toinp) or ("start" in toinp) or ("open" in toinp )or ("execute" in toinp) or ("launch" in toinp) or (" " in toinp)) and ("dont" not in toinp) and (("cmd" in toinp) or ("prompt" in toinp) or ("command" in toinp))):
				print("\n ........OPENING COMMAND PROMPT........")
				os.system("start cmd")
			elif (("dont" in toinp) or ("never" in toinp) or ("no" in toinp)):
				print("SORRY...REQUEST DENIED BY YOU")
			elif (("exit" in toinp ) or ("quit" in toinp)):
				print(".........THANKS FOR YOUR PRECIOUS TIME..........")
				break
			else:
				print("YOUR SYSTEM DOESNT SUPPORT")
		
			
	
	elif oneinp==2:
		while True:
			print("\n 1. OPEN BROWSER (CHROME/ FIREFOX) \n 2. OPEN MEDIA PLAYER FOR YOU \n 3. OPEN NOTEPAD FOR YOU \n 4. OPEN COMMAND PROMPT FOR YOU")
			print(" 5. OPEN PYTHON INTERPRETER FOR YOU \n 6. OPEN MICROSOFT (WORD/EXCEL/POWERPOINT) FOR YOU \n 7. EXIT \n")
			thinp = int(input(">>>>> \t"))
			if thinp==1:
				print("\t\t PRESS 1. FOR CHROME \n\t\t PRESS 2. FOR FIREFOX")
				finp = int(input(">>>>> \t"))
				if finp==1:
					print("\n ........OPENING CHROME........")
					os.system("start chrome")
				elif finp==2:
					print("\n ........OPENING FIREFOX........")
					os.system("start firefox")
				else:
					print(" \n Invalid Input")
			elif thinp==2:
				print("\n ........OPENING MEDIA PLAYER........")
				os.system("start wmplayer")
			elif thinp==3:
				print("\n ........OPENING NOTEPAD........")
				os.system("start notepad")
			elif thinp==4:
				print("\n ........OPENING COMMAND PROMPT........")
				os.system("start cmd")
			elif thinp==5:
				print("\n ........OPENING PYTHON INTERPRETER........")
				os.system("start python")
			elif thinp==6:
				print("\t\t PRESS 1. FOR MICROSOFT WORD \n\t\t PRESS 2. FOR MICROSOFT EXCEL \n\t\t PRESS 3. FOR MICROSOFT POWERPOINT")
				fiinp = int(input(">>>>> \t"))
				if fiinp==1:
					print("\n ........OPENING MICROSOFT WORD........")
					os.system("start WINWORD")
				elif fiinp==2:
					print("\n ........OPENING MICROSOFT EXCEL........")
					os.system("start EXCEL")
				elif fiinp==3:
					print("\n ........OPENING MICROSOFT POWERPOINT........")
					os.system("start POWERPNT")
				else:
					print("\n INVALID INPUT")
		
			elif thinp==7:
				print("\n EXITING")
				break
			else:
				print("Invalid Input")

	elif oneinp==3:
		print("THANKS FOR YOUR PRECIOUS TIME")
		pyttsx3.speak("Thank you for visiting")
		break;
		
	else:
		print("\n Invalid Input.....Please try again")