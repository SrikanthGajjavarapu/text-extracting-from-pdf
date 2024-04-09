import re

#giving the text file path
text_path = 'text.txt'  

# Reading the text data from the file
with open(text_path, 'r', encoding='utf-8') as invoice_file:
    invoice_text = invoice_file.read()

# Defining regular expressions to extracting data
invoice_number_pattern = r"Invoice Number (.+)"
invoice_date_pattern = r"Invoice Date (.+)"
due_date_pattern = r"Due Date (.+)"
total_due_pattern = r"Total Due (\$\d+\.\d+)"
item_pattern = r"(\d+\.\d+)([^\d]+)(\$\d+\.\d+)\s(\d+\.\d+%)\s(\$\d+\.\d+)"

# Extracting data using regular expressions
invoice_number_match = re.search(invoice_number_pattern, invoice_text)
invoice_date_match = re.search(invoice_date_pattern, invoice_text)
due_date_match = re.search(due_date_pattern, invoice_text)
total_due_match = re.search(total_due_pattern, invoice_text)
line_item_matches = re.findall(item_pattern, invoice_text)

# Storing the extracted data in a dictionary
invoice_info = {}
if invoice_number_match:
    invoice_info['Invoice Number'] = invoice_number_match.group(1)
if invoice_date_match:
    invoice_info['Invoice Date'] = invoice_date_match.group(1)
if due_date_match:
    invoice_info['Due Date'] = due_date_match.group(1)
if total_due_match:
    invoice_info['Total Due'] = total_due_match.group(1)

# Storing items in a list of dictionaries
items = []
for match in line_item_matches:
    quantity, service, price, adjust, sub_total = match
    items.append({
        'Hrs/Qty': quantity.strip(),
        'Service': service.strip(),
        'Rate/Price': price.strip(),
        'Adjust' : adjust.strip(),
        'Sub Total' : sub_total.strip()
    })

# Printing the extracted data
print("Invoice Information:")
print(invoice_info)
print("\nItems:")
for item in items:
    print(item)
