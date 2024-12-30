from flask import Flask, render_template, request, send_file
from fpdf import FPDF  # PDF generation for certificates
import os

app = Flask(__name__)

# Ensure the 'generated_certificates' folder exists
if not os.path.exists('generated_certificates'):
    os.makedirs('generated_certificates')

# Home route to display the form
@app.route('/')
def home():
    return render_template('index.html')  # HTML form page

# Route to handle certificate generation
@app.route('/generate', methods=['POST'])
def generate_certificate():
    # Get the name entered by the user
    name = request.form['name']
    
    # Check if the name is provided
    if not name:
        return "Error: Name is required!"
    
    # Define the filename for the generated certificate
    certificate_filename = f"generated_certificates/{name}_certificate.pdf"
    
    # Create PDF for the certificate
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Add content to the certificate (e.g., title and user name)
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 10, txt="Certificate of Completion", ln=True, align="C")
    pdf.ln(20)
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=f"Certificate awarded to {name}", ln=True, align="C")
    
    # Save the generated PDF
    pdf.output(certificate_filename)

    # Return the generated PDF as an attachment for download
    return send_file(certificate_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
