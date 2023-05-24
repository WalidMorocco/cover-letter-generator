from docxtpl import DocxTemplate
import datetime
import os

company_name = input("Enter name of the Company: ")
position_name = input("Enter name of the Position: ")

today_date = datetime.datetime.today().strftime('%B %d, %Y')

context = {'today_date': today_date,
           'company_name': company_name,
           'position_name': position_name}

# Open master template
doc = DocxTemplate("template/template.docx")
doc.render(context)

# Remove spaces
position_name_formatted = position_name.replace(" ", "")
company_name_formatted = company_name.replace(" ", "")

# Save the file with personalized filename
output_filename = f'Walid_Amar_CoverLetter_{position_name_formatted}_{company_name_formatted}.docx'
directory = 'letters/'

# Check if the directory exists, and create it if it does not
if not os.path.exists(directory):
    os.makedirs(directory)

full_path = f'{directory}{output_filename}'
doc.save(full_path)

print(
    f'Cover letter for a {position_name} at {company_name} has been created!')
