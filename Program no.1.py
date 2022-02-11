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
# 	- Search how data is structured using JSON format
# 	- Search how to read JSON file
# 	- You will create the JSON file manually
# 	- Your code should be in github before Feb12

# Connect json file into .py program
with open('resume.json') as resumeJson:
    data = json.load(resumeJson.read())
# Create Page and supply format
resume = FPDF('P', 'mm', 'Letter')
resume.add_page()
resume.set_margin(12)
# Header
resume.set_font('Times', 'UB', 30)
resume.cell(130, 10, "Wanjin P. Maglangit", ln = True)
resume.set_font('Times', 'I', 20)
resume.cell(100, 10, "Full Stack Developer", ln = True)

# Personal info
resume.set_font('Times', 'UB', 18)
resume.cell(0,10 , "Personal Information", ln = True)
resume.set_font('He;vetica', '', 12)
# Summary

# Experience

# Education

# Projects

# Skills

resume.output('MAGLANGIT,Wanjin P..pdf')