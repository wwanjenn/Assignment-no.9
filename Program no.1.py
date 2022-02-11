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
with open('Resume.json') as resumeJson:
    data = json.load(resumeJson.read())
# Create Page and supply format
resume = FPDF('P', 'cm', 'Letter')
resume.add_page()
resume.set_margin(1.27)
# Header
def headerInfo(header):
    header.font('Times', 'UB', 3)
    header.cell(13, 1, "Wanjin P. Maglangit", ln = True)
    header.font('Times', 'I', 2)
    header.cell(100, 1, "Full Stack Developer", ln = True)


# Personal info

# Summary

# Experience

# Education

# Projects

# Skills

resume.output('MAGLANGIT,Wanjin P..pdf')