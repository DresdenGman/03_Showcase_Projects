#!/usr/bin/env python3
"""Convert Jupyter HTML export to PDF"""

from playwright.sync_api import sync_playwright


def html_to_pdf(input_path: str, output_path: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto(f"file://{input_path}")
        page.wait_for_load_state("networkidle")
        
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            margin={"top": "0.5in", "bottom": "0.5in", "left": "0.5in", "right": "0.5in"}
        )
        
        browser.close()
        print(f"PDF saved to: {output_path}")


if __name__ == "__main__":
    html_file = "airline_customer_value_analysis.html"
    pdf_file = "airline_customer_value_analysis.pdf"
    html_to_pdf(html_file, pdf_file)