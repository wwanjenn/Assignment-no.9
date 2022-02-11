# Assignment 9
import json
from fpdf import FPDF

# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

# Note:
# 	- Search for available PDF library that you can use
# 	- Search how data is++ structured using JSON format
# 	- Search how to read JSON file
# 	- You will create the JSON file manually
# 	- Your code should be in github before Feb12

# Connect json file into .py program
with open('resume.json') as resumeJson:
    data = json.loads(resumeJson.read())
# Create Page and supply format
resume = FPDF('P', 'mm', 'Letter')
resume.add_page()
resume.set_margin(12.5)
# Header
resume.set_font('Times', 'UB', 30)
resume.cell(130, 10, "Wanjin P. Maglangit", ln = True)
resume.set_font('Times', 'I', 20)
resume.cell(100, 10, "Full Stack Developer", ln = True)

# Personal info
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Personal Information", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Sex: ' + str(data["Personal Info"][0]["Sex"]), ln = True) 
resume.cell(50,10, 'Age: ' + str(data["Personal Info"][0]["Age"]), ln = True)
resume.cell(50,10, 'Address: ' + str(data["Personal Info"][0]["Address"]), ln = True)
resume.cell(50,10, 'Contact#: ' + str(data["Personal Info"][0]["Contact Number"]), ln = True)
resume.cell(50,10, 'Email Address: ' + str(data["Personal Info"][0]["Email Address"]), ln = True)
resume.cell(50,10, 'Github: ' + str(data["Personal Info"][0]["Github Account"]), ln = True)

# Summary
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Professional Summary", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Sex: ' + str(data["Personal Info"][0]["Sex"]), ln = True) 
resume.cell(50,10, 'Age: ' + str(data["Personal Info"][0]["Age"]), ln = True)
resume.cell(50,10, 'Address: ' + str(data["Personal Info"][0]["Address"]), ln = True)
resume.cell(50,10, 'Contact#: ' + str(data["Personal Info"][0]["Contact Number"]), ln = True)
resume.cell(50,10, 'Email Address: ' + str(data["Personal Info"][0]["Email Address"]), ln = True)
resume.cell(50,10, 'Github: ' + str(data["Personal Info"][0]["Github Account"]), ln = True)

# Experience
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Personal Information", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Sex: ' + str(data["Personal Info"][0]["Sex"]), ln = True) 
resume.cell(50,10, 'Age: ' + str(data["Personal Info"][0]["Age"]), ln = True)
resume.cell(50,10, 'Address: ' + str(data["Personal Info"][0]["Address"]), ln = True)
resume.cell(50,10, 'Contact#: ' + str(data["Personal Info"][0]["Contact Number"]), ln = True)
resume.cell(50,10, 'Email Address: ' + str(data["Personal Info"][0]["Email Address"]), ln = True)
resume.cell(50,10, 'Github: ' + str(data["Personal Info"][0]["Github Account"]), ln = True)

# Education
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Personal Information", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Sex: ' + str(data["Personal Info"][0]["Sex"]), ln = True) 
resume.cell(50,10, 'Age: ' + str(data["Personal Info"][0]["Age"]), ln = True)
resume.cell(50,10, 'Address: ' + str(data["Personal Info"][0]["Address"]), ln = True)
resume.cell(50,10, 'Contact#: ' + str(data["Personal Info"][0]["Contact Number"]), ln = True)
resume.cell(50,10, 'Email Address: ' + str(data["Personal Info"][0]["Email Address"]), ln = True)
resume.cell(50,10, 'Github: ' + str(data["Personal Info"][0]["Github Account"]), ln = True)

# Projects
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Personal Information", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Sex: ' + str(data["Personal Info"][0]["Sex"]), ln = True) 
resume.cell(50,10, 'Age: ' + str(data["Personal Info"][0]["Age"]), ln = True)
resume.cell(50,10, 'Address: ' + str(data["Personal Info"][0]["Address"]), ln = True)
resume.cell(50,10, 'Contact#: ' + str(data["Personal Info"][0]["Contact Number"]), ln = True)
resume.cell(50,10, 'Email Address: ' + str(data["Personal Info"][0]["Email Address"]), ln = True)
resume.cell(50,10, 'Github: ' + str(data["Personal Info"][0]["Github Account"]), ln = True)

# Skills
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Personal Information", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Sex: ' + str(data["Personal Info"][0]["Sex"]), ln = True) 
resume.cell(50,10, 'Age: ' + str(data["Personal Info"][0]["Age"]), ln = True)
resume.cell(50,10, 'Address: ' + str(data["Personal Info"][0]["Address"]), ln = True)
resume.cell(50,10, 'Contact#: ' + str(data["Personal Info"][0]["Contact Number"]), ln = True)
resume.cell(50,10, 'Email Address: ' + str(data["Personal Info"][0]["Email Address"]), ln = True)
resume.cell(50,10, 'Github: ' + str(data["Personal Info"][0]["Github Account"]), ln = True)

#Output
resume.output('MAGLANGIT,Wanjin P..pdf')