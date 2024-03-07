import pdfplumber
import re

pdf_path = 'LN24-4482.pdf'
# Define a regular expression to match tables
keywords = ["Nr.", "Omschrijving", "Aantal", "Eenheid"]


def extract_tables():
    with pdfplumber.open(pdf_path) as pdf:
        # Extract text from the single page
        page = pdf.pages[0]
        text = page.extract_text()
        lines = text.split('\n')

        # Flag to indicate whether we are inside a table
        in_table = False
        table_lines = []

        # Iterate through each line in the text
        for line in lines:
            # Check if the line contains text
            if line.strip():
                # Check if the line starts with any whitespace characters, indicating it's inside a table
                if line[0].isspace():
                    # We found a table row, add it to the current table
                    table_lines.append(line)
                    in_table = True
                elif in_table:
                    # If the line is not inside a table but we were previously in a table, print the table
                    print('\n'.join(table_lines))
                    # Reset the table lines and in_table flag for the next table
                    table_lines = []
                    in_table = False
            elif in_table:
                # If the line is empty and we were previously in a table, print the table
                print('\n'.join(table_lines))
                # Reset the table lines and in_table flag for the next table
                table_lines = []
                in_table = False


extract_tables()


# import pdfplumber
# import re
# import pandas as pd
#
# pdf_path = 'LN24-4482.pdf'
# # Define a regular expression to match tables
# keywords = ["Nr.", "Omschrijving", "Aantal", "Eenheid"]
#
#
# def find_and_parse_table():
#     with pdfplumber.open(pdf_path) as pdf:
#         # Extract text from the single page
#         page = pdf.pages[0]
#         text = page.extract_text()
#         lines = text.split('\n')
#
#         # Initialize variables to track table rows and columns
#         table = []
#         in_table = False
#
#         # Iterate through each line in the text
#         for line in lines:
#             # Check if any of the specified keywords are present in the line
#             if any(keyword in line for keyword in keywords):
#                 in_table = True
#                 # Add the line to the table
#                 table.append(line)
#
#         # If we are in a table, parse and print the table
#         if in_table:
#             parse_table(table)
#         else:
#             print("No table containing the specified keywords was found.")
#
# def parse_table(table):
#     # Extract column names
#     column_names = table[0].split()
#
#     # Print column names
#     print("Columns:", column_names)
#
#     # Extract values for each row (excluding the first row)
#     for row in table[1:]:
#         row_values = row.split()
#         print("Values:", row_values)
#
#
#
# # def find_table_with_keywords():
# #     with pdfplumber.open(pdf_path) as pdf:
# #         # Extract text from the single page
# #         page = pdf.pages[0]
# #         text = page.extract_text()
# #         lines = text.split('\n')
# #
# #         # Initialize variables to track table rows
# #         table_rows = []
# #         in_table = False
# #
# #         # Iterate through each line in the text
# #         for line in lines:
# #             # Check if any of the specified keywords are present in the line
# #             if any(keyword in line for keyword in keywords):
# #                 in_table = True
# #                 # Add the line to the table rows
# #                 table_rows.append(line)
# #
# #         # If we are in a table, return the table rows as a single string
# #         if in_table:
# #             return '\n'.join(table_rows)
# #
# #     # Return None if no table containing the specified keywords is found
# #     return None
#
#
# def extract_order_nr():
#     # Regular expression pattern to match "Ordernr." followed by a number-like string
#     pattern = r'Ordernr.\s*(\w+-\d+)'
#
#     # Search for the pattern in the PDF text
#     match = re.search(pattern, pdf_text)
#
#     # If a match is found, extract the number, otherwise return None
#     if match:
#         ordernr = match.group(1)
#     else:
#         ordernr = None
#
#     return ordernr
#
#
def read_pdf(file_path):
    text = ''
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


#
#
# # Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_text = read_pdf(pdf_path)
print(pdf_text)
# print(find_and_parse_table())
# # print(extract_order_nr())
# # print(find_table_with_keywords())
#
