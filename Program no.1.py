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
resume.cell(50,10, str(data["Professional Summary"]), ln = True) 

# Experience
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Work Experience", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Former Work: ' + str(data["Work Experience"]["Former Work"]), ln = True) 
resume.cell(50,10, 'Company: ' + str(data["Work Experience"]["Company"]), ln = True)
resume.cell(50,10, 'Work Description: ' + str(data["Work Experience"]["Work Description"]), ln = True)


# Education
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Educational Background", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Course: ' + str(data["Educational Background"][0]["Course"]), ln = True) 
resume.cell(50,10, 'University: ' + str(data["Educational Background"][0]["University"]), ln = True)
resume.cell(50,10, 'Course: ' + str(data["Educational Background"][1]["Course"]), ln = True)
resume.cell(50,10, 'University: ' + str(data["Educational Background"][1]["University"]), ln = True)


# Projects
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Projects", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, 'Project Name: ' + str(data["Projects"]["Project Name"]), ln = True) 
resume.cell(50,10, 'Position: ' + str(data["Projects"]["Position"]), ln = True)
resume.cell(50,10, 'Project Description: ' + str(data["Projects"]["Project Description"]), ln = True)


# Skills
resume.set_font('Times', 'B', 18)
resume.cell(0,10 , "Skills", ln = True)
resume.set_font('Helvetica', '', 12)
resume.cell(50,10, str(data["Skills"][0]), ln = False) 
resume.cell(50,10, str(data["Skills"][1]), ln = True)
resume.cell(50,10, str(data["Skills"][2]), ln = False)
resume.cell(50,10, str(data["Skills"][3]), ln = True)
resume.cell(50,10, str(data["Skills"][4]), ln = False)
resume.cell(50,10, str(data["Skills"][5]), ln = True)

#Output
resume.output('MAGLANGIT,Wanjin P..pdf')