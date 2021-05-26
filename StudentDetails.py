import pandas as pd
import string

readatabase = pd.read_excel('school.xlsx', sheet_name = 'Student Database')

Adno = readatabase['Adm No'].tolist()
Adno = Adno[len(Adno)- 1] - 1
Name = readatabase['Name'].tolist()
Class = readatabase['Class'].tolist()
Section = readatabase['Section'].tolist()
House = readatabase['House'].tolist()
Mname = readatabase['Mother Name'].tolist()
Fname = readatabase['Father Name'].tolist()
Contact = readatabase['Contact No'].tolist()
Mainsub = readatabase['Main Sub'].tolist()
Faddsub = readatabase['1st Add Sub'].tolist()
Saddsub = readatabase['2nd Add Sub'].tolist()
Transport = readatabase['Transport'].tolist()
Fees = readatabase['Fees'].tolist()
Message = readatabase['Messages'].tolist()
Assignment = readatabase['Assignments Pending'].tolist()
Progressreport = readatabase['Progress Report'].tolist()

def showdetails(num):
	if num > 0 and num < Adno + 2:
		num -= 1
		ans = []
		ans.append('Student Details')
		ans.append('Name: ' + Name[num])
		#print("Bot: \tStudent Details\n\n" )
		#print("\tName: " + Name[num])
		ans.append('Class: '+ str(Class[num]))
		#print("\tClass: ", Class[num])
		ans.append('Section: ' + Section[num])
		#print("\tSection: " + Section[num])
		ans.append("House: " + House[num])
		#print("\tHouse: " + House[num])
		ans.append("Mother Name " + Mname[num])
		#print("\tMother Name " + Mname[num])
		ans.append("Father Name: " + Fname[num])
		#print("\tFather Name: " + Fname[num])
		ans.append("Contact Number: " + str(Contact[num]))
		#print("\tContact Number: ", Contact[num], end = "\n\n")
		ans.append("Main Subjects: " + Mainsub[num])
		ans.append("First Additional Subject: " + Faddsub[num])
		ans.append("Second Additional Subject: "+ str(Saddsub[num]))
		ans.append("Transport availed: " + Transport[num])
		ans.append("Fees: "+ str(Fees[num]))
		ans.append("New Mesages: " + Message[num])
		ans.append("New Assignments: " + Assignment[num])
		ans.append("Progress Report for first term: ")
		subjects = Mainsub[num].split(' ')
		subjects.append(Faddsub[num])
		subjects.append(Saddsub[num])
		grades = Progressreport[num].split(' ')

		for i in range(len(grades)):
			ans.append(subjects[i] + ' - ' + grades[i])
		return ans
	else: return False
		#print("\tMain Subjects: ", end = ' ')
		#print(*Mainsub[num].split(' '), sep = ', ')
		#print("\tFirst Additional Subject: " + Faddsub[num])
		#print("\tSecond Additional Subject: ", Saddsub[num], end = "\n\n")
		#print("\tTransport availed: " + Transport[num])
		#print("\tFees: ", Fees[num])
		#print("\tNew Mesages: " + Message[num])
		#print("\tNew Assignments: " + Assignment[num], end = "\n\n")
		#print("\tProgress Report for first term: ")
        #for i in range(len(grades)):
        #    print("\t\t", subjects[i], ' - ', grades[i])