import pandas as pd
import string
import StudentDetails as SD

readfaq = pd.read_excel('school.xlsx', sheet_name = 'FAQ')

question = readfaq['Question'].tolist()
response = readfaq['Response'].tolist()

readconversation = pd.read_excel('school.xlsx', sheet_name = 'Conversation')

greeting = readconversation['Greeting'].tolist()
praising = readconversation['Praising'].tolist()
ending = readconversation['Ending'].tolist()
cquestion = readconversation['Question'].tolist()
canswer = readconversation['Answer'].tolist()

def inCquestion(uinput):
    for i in range(len(cquestion)):
        if str(cquestion[i]) in uinput:
            return canswer[i]
    return False

def inFAQ(uinput):
    for i in range(len(question)):
        if question[i] in uinput:
            return response[i]
    return False

def inGreeting(uinput):          
    for phrase in greeting:
        if str(phrase) in uinput:
            res = str(phrase).capitalize() + ", how may I assist you?"
            return res
    return False

def inPraising(uinput):
    for phrase in praising:
        if str(phrase) in uinput:
            res = "Thanks a lot, always happy to help"
            return res
    return False

def  Chatbot(uinput, res):
	if res == "Please enter your admission number":
		if uinput.isdigit():
			check = SD.showdetails(int(uinput))
			if check is not False:
				return check
			else:
				return("Wrong admission number. Please enter again.")
		else:
			return ("Wrong admission number. Please enter again.")

	if  any(phrase in uinput for phrase in ending):
		return 'Bye bye! Hope I could help you out.'

	check = inCquestion(uinput)
	if check is not False:
		return check

	check = inFAQ(uinput)
	if check is not False:
		return check

	check = inGreeting(uinput)
	if check is not False:
		return check
	
	check = inPraising(uinput)
	if check is not False:
		return check

	file = open("questions.txt", 'a')
	file.write(uinput + '\n')
	file.close()
	return "Sorry couldn't able to get that, contact the reception for info regarding that"