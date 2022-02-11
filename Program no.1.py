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
resume.set_margin(13)

# Header
resume.image('2x2.jpg', 150, 10, 50)
resume.set_font('Times', 'UB', 30)
resume.cell(130, 10, "Wanjin P. Maglangit", ln = True)
resume.set_font('Times', 'I', 20)
resume.cell(100, 10, "Full Stack Developer", ln = True)
resume.ln(5)

# Personal info
resume.set_font('Times', 'B', 18)
resume.set_draw_color(000,000,000)
resume.set_fill_color(221,221,221)
resume.cell(130,8, "Personal Information", fill = True, border = True, ln = True, align = 'C')
resume.ln(2)
resume.set_font('Helvetica', '', 12)
resume.cell(50,7, 'Sex         : ' + str(data["Personal Info"][0]["Sex"]), ln = True) 
resume.cell(50,7, 'Age         : ' + str(data["Personal Info"][0]["Age"]), ln = True)
resume.cell(50,7, 'Address  : ' + str(data["Personal Info"][0]["Address"]), ln = True)
resume.cell(50,7, 'Contact# : ' + str(data["Personal Info"][0]["Contact Number"]), ln = True)
resume.cell(50,7, 'Email      : ' + str(data["Personal Info"][0]["Email Address"]), ln = True)
resume.cell(50,7, 'Github    : ' + str(data["Personal Info"][0]["Github Account"]), ln = True)
resume.ln(2)

# Summary
resume.set_font('Times', 'B', 18)
resume.set_draw_color(000,000,000)
resume.set_fill_color(221,221,221)
resume.cell(0,7 , "Professional Summary", fill = True, border = True, ln = True, align = 'C')
resume.ln(2)
resume.set_font('Helvetica', '', 12)
resume.cell(50,7, str(data["Professional Summary"][0]), ln = True)
resume.cell(50,7, str(data["Professional Summary"][1]), ln = True) 
resume.ln(2)

# Experience
resume.set_font('Times', 'B', 18)
resume.set_draw_color(000,000,000)
resume.set_fill_color(221,221,221)
resume.cell(0,7 , "Work Experience", fill = True, border = True, ln = True, align = 'C')
resume.ln(2)
resume.set_font('Helvetica', '', 12)
resume.cell(50,7, 'Former Work       : ' + str(data["Work Experience"]["Former Work"]), ln = True) 
resume.cell(50,7, 'Company            : ' + str(data["Work Experience"]["Company"]), ln = True)
resume.cell(50,7, 'Work Description: ' + str(data["Work Experience"]["Work Description"][0]), ln = True)
resume.cell(50,7,  str(data["Work Experience"]["Work Description"][1]), ln = True)
resume.ln(2)

# Education
resume.set_font('Times', 'B', 18)
resume.set_draw_color(000,000,000)
resume.set_fill_color(221,221,221)
resume.cell(0,7 , "Educational Background", fill = True, border = True, ln = True, align = 'C')
resume.ln(2)
resume.set_font('Helvetica', '', 12)
resume.cell(50,7, 'Course    : ' + str(data["Educational Background"][0]["Course"]), ln = True) 
resume.cell(50,7, 'University: ' + str(data["Educational Background"][0]["University"]), ln = True)
resume.cell(50,7, 'Course    :  ' + str(data["Educational Background"][1]["Course"]), ln = True)
resume.cell(50,7, 'University: ' + str(data["Educational Background"][1]["University"]), ln = True)
resume.ln(2)

# Projects
resume.set_font('Times', 'B', 18)
resume.set_draw_color(000,000,000)
resume.set_fill_color(221,221,221)
resume.cell(0,7 , "Projects", fill = True, border = True, ln = True, align = 'C')
resume.ln(2)
resume.set_font('Helvetica', '', 12)
resume.cell(50,7, 'Project Name        : ' + str(data["Projects"]["Project Name"]), ln = True) 
resume.cell(50,7, 'Position                 : ' + str(data["Projects"]["Position"]), ln = True)
resume.cell(50,7, 'Project Description: ' + str(data["Projects"]["Project Description"]), ln = True)

resume.ln(2)

# Skills
resume.set_font('Times', 'B', 18)
resume.set_draw_color(000,000,000)
resume.set_fill_color(221,221,221)
resume.cell(0,7 , "Skills", fill = True, border = True, ln = True, align = 'C')
resume.ln(2)
resume.set_font('Helvetica', '', 12)
resume.cell(75,7, str(data["Skills"][0]), ln = False) 
resume.cell(75,7, str(data["Skills"][1]), ln = True)
resume.cell(75,7, str(data["Skills"][2]), ln = False)
resume.cell(75,7, str(data["Skills"][3]), ln = True)
resume.cell(75,7, str(data["Skills"][4]), ln = False)
resume.cell(75,7, str(data["Skills"][5]), ln = True)
resume.ln(2)

#Output
resume.output('MAGLANGIT,Wanjin P..pdf')