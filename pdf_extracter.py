import PyPDF2
import pandas as pd
import re


def extract_info_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def extract_glass_info(text):
    # You can customize this based on your actual PDF structure
    event_index = text.find("In the event")
    event_info = text[event_index:].split(',')

    event_name = event_info[0].split(" ")[-1].strip()
    sold_glasses = int(re.search(r'\b\d+\b', event_info[1]).group())
    glasses_we_have = int(re.search(r'\b\d+\b', event_info[2]).group())
    glasses_we_do_not_have = int(re.search(r'\b\d+\b', event_info[3]).group())
    # glasses_we_do_not_have = None
    return event_name, sold_glasses, glasses_we_have, glasses_we_do_not_have


def main(pdf_path, excel_path):
    text = extract_info_from_pdf(pdf_path)
    event_name, sold_glasses, glasses_we_have, glasses_we_do_not_have = extract_glass_info(text)

    data = {
        'event_name': [event_name],
        'sold_glasses': [sold_glasses],
        'glasses_we_have': [glasses_we_have],
        'glasses_we_do_not_have': [glasses_we_do_not_have]
    }

    df = pd.DataFrame(data)
    print(df)
    df.to_excel(excel_path, index=False)
    print("Data has been written to Excel successfully.")




if __name__ == "__main__":
    pdf_file_path = 'nando.pdf'
    excel_file_path = 'nando_storage.xlsx'
    main(pdf_file_path, excel_file_path)
