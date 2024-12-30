from flask import Flask, render_template, request, send_file
from fpdf import FPDF  # PDF generation ke liye

app = Flask(__name__)

# Home route to display the form
@app.route('/')
def home():
    return render_template('index.html')  # HTML form page

# Route to handle certificate generation
@app.route('/generate', methods=['POST'])
def generate_certificate():
    name = request.form['name']  # User se naam input lete hain
    
    # PDF certificate generate karne ki logic
    certificate_filename = f"generated_certificates/{name}_certificate.pdf"  # PDF file name with .pdf extension
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # PDF styling (font size, type, etc.)
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 10, txt="Certificate of Completion", ln=True, align="C")
    pdf.ln(20)
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=f"Certificate awarded to {name}", ln=True, align="C")
    
    # Saving the generated PDF with .pdf extension in the generated_certificates folder
    pdf.output(certificate_filename)
    
    # Certificate file ko user ko download ke liye bhejna
    return send_file(certificate_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
