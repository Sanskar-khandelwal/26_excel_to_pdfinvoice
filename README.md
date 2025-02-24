# Excel to Invoice Converter

This project is a Python-based tool that converts Excel spreadsheets into professional invoice PDFs using the `FPDF` library.

## Features
- Reads invoice data from an Excel file.
- Converts the data into a structured table format.
- Generates a well-formatted invoice PDF.
- Lightweight and easy to use.

## Installation

Ensure you have Python installed (>=3.6), then install the required dependencies:

```sh
pip install fpdf pandas openpyxl
```

## Usage

1. Place your Excel file (e.g., `invoice_data.xlsx`) in the invoices directory.
2. Run the script:
```sh
python main.py
```

3. The generated invoice PDF will be saved in the PDFs directory.

## Example
Given an Excel file like this:

| Item      | Quantity | Price | Total |
|-----------|----------|-------|-------|
| Product A | 2        | 500   | 1000  |
| Product B | 1        | 700   | 700   |
|           |          |       | 1700  |

The script will generate an invoice PDF with a structured table format.

## Dependencies
- `fpdf`: For PDF generation.
- `pandas`: For reading Excel files.
- `openpyxl`: For handling `.xlsx` files.

## Contributing
Feel free to contribute by improving the table formatting, adding new features, or optimizing the PDF generation process.

## License
This project is open-source and available under the MIT License.

---
Made with ❤️ by Sanskar

