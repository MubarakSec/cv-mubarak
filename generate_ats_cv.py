# generate_ats_cv.py - Generate a highly parsable ATS-friendly PDF CV using ReportLab

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

class HRLine(Flowable):
    """A clean horizontal rule flowable for section separation."""
    def __init__(self, width, thickness=0.75, color=colors.HexColor('#111111'), space_after=8):
        super().__init__()
        self.width = width
        self.thickness = thickness
        self.color = color
        self.space_after = space_after

    def wrap(self, availWidth, availHeight):
        return availWidth, self.thickness + self.space_after

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.space_after, self.width, self.space_after)
        self.canv.restoreState()

def create_ats_pdf(output_path):
    # Setup document with standard margins (0.75 in = 54 pt)
    margin = 54
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=margin,
        bottomMargin=margin
    )
    
    # Text width = Letter width (612) - leftMargin (54) - rightMargin (54) = 504 pt
    width = 504
    
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Define standard clean typography (using Helvetica for ATS safety)
    style_name = ParagraphStyle(
        'CV_Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#000000'),
        spaceAfter=4
    )
    
    style_contact = ParagraphStyle(
        'CV_Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12
    )
    
    style_h1 = ParagraphStyle(
        'CV_H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#000000'),
        spaceBefore=8,
        spaceAfter=2
    )
    
    style_body = ParagraphStyle(
        'CV_Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=4
    )
    
    style_bullet = ParagraphStyle(
        'CV_Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        leftIndent=15,
        firstLineIndent=-10,
        textColor=colors.HexColor('#222222'),
        spaceAfter=3
    )
    
    style_project_title = ParagraphStyle(
        'CV_ProjTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#000000'),
        spaceAfter=2
    )
    
    style_edu_title = ParagraphStyle(
        'CV_EduTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#000000'),
        spaceAfter=1
    )

    # 1. HEADER SECTION
    story.append(Paragraph("MUBARAK WALID AL-HAMMADI", style_name))
    
    contact_info = (
        "Sana'a, Yemen  |  +967 730059208  |  xmobta@gmail.com<br/>"
        "LinkedIn: linkedin.com/in/mobta-x-6289193ab  |  GitHub: github.com/MubarakSec  |  TryHackMe: tryhackme.com/p/mobarkm919"
    )
    story.append(Paragraph(contact_info, style_contact))
    
    # Helper function to add sections
    def add_section_header(title):
        story.append(Paragraph(title, style_h1))
        story.append(HRLine(width=width))
        
    # 2. PROFESSIONAL SUMMARY
    add_section_header("PROFESSIONAL SUMMARY")
    summary_text = (
        "Analytical and driven 3rd-year Cybersecurity student with hands-on experience in developing "
        "custom security tools, vulnerability discovery, and application analysis. Proven ability to "
        "build CLI-first tools for web and Android environments. Seeking to leverage strong programming "
        "skills and penetration testing knowledge to contribute to DeepSafer as a Cybersecurity Specialist / "
        "Penetration Tester."
    )
    story.append(Paragraph(summary_text, style_body))
    story.append(Spacer(1, 6))
    
    # 3. EDUCATION
    add_section_header("EDUCATION")
    story.append(Paragraph("Bachelor of Science in Cybersecurity", style_edu_title))
    story.append(Paragraph("Emirates International University  |  Expected Graduation: 2028", style_body))
    story.append(Spacer(1, 6))
    
    # 4. TECHNICAL SKILLS
    add_section_header("TECHNICAL SKILLS")
    skills = [
        "<b>Security Tools:</b> Burp Suite, Nmap, Metasploit, Netcat, Playwright.",
        "<b>Programming & Scripting:</b> Python, TypeScript, C++, Bash, JavaScript, Node.js, HTML/CSS, PHP.",
        "<b>Core Competencies:</b> Vulnerability Discovery, Dynamic Instrumentation, Static Analysis, Web/Mobile Security, Penetration Testing.",
        "<b>Languages:</b> Arabic (Native), English (B2 Level)."
    ]
    for skill in skills:
        story.append(Paragraph(f"&bull; {skill}", style_bullet))
    story.append(Spacer(1, 6))
    
    # 5. PROJECTS & TOOL DEVELOPMENT
    add_section_header("PROJECTS & TOOL DEVELOPMENT")
    
    # Project 1
    story.append(Paragraph("reconnV2 | Web Vulnerability Discovery Tool", style_project_title))
    story.append(Paragraph(
        "&bull; Engineered an autonomous, CLI-first web vulnerability discovery tool that acts as a "
        "junior analyst by mapping targets and executing multi-step validation loops.",
        style_bullet
    ))
    story.append(Paragraph(
        "&bull; Implemented rigorous validation mechanisms requiring cryptographic or differential "
        "proof before declaring a log, significantly reducing false positives.",
        style_bullet
    ))
    story.append(Spacer(1, 4))
    
    # Project 2
    story.append(Paragraph("Aegis Mobile | Android Application Security Toolkit", style_project_title))
    story.append(Paragraph(
        "&bull; Developed a CLI-first Android application security analysis toolkit combining deep "
        "semantic static analysis with bypass-assisted dynamic instrumentation for high-signal evidence.",
        style_bullet
    ))
    story.append(Spacer(1, 4))
    
    # Project 3
    story.append(Paragraph("CodeRooms | Real-Time Collaborative Coding", style_project_title))
    story.append(Paragraph(
        "&bull; Built a Node.js WebSocket server and a VS Code extension to enable real-time "
        "collaborative coding, shared buffers, and team chat within the editor environment.",
        style_bullet
    ))
    story.append(Spacer(1, 4))
    
    # Project 4
    story.append(Paragraph("Find The Five & Web to PDF Toolkit", style_project_title))
    story.append(Paragraph(
        "&bull; <b>Find The Five:</b> Created PHP front-end labs demonstrating five core web "
        "vulnerabilities with stubbed backend hooks for educational integration.",
        style_bullet
    ))
    story.append(Paragraph(
        "&bull; <b>Web to PDF & Monitor Bot:</b> Developed a high-performance desktop app using Playwright "
        "to extract links from SPAs, and an asynchronous Telegram bot for real-time website monitoring.",
        style_bullet
    ))
    story.append(Spacer(1, 6))
    
    # 6. CERTIFICATIONS & CONTINUOUS LEARNING
    add_section_header("CERTIFICATIONS & CONTINUOUS LEARNING")
    certs = [
        "<b>Cisco Certifications:</b> Certified Support Technician (CCST) Cybersecurity, Introduction to Cybersecurity.",
        "<b>TryHackMe Completed Paths:</b> Jr Penetration Tester, Web Fundamentals, Pre Security, Cyber Security 101.",
        "<b>English Proficiency:</b> B2 Level Certificate &ndash; E-ONE Institute."
    ]
    for cert in certs:
        story.append(Paragraph(f"&bull; {cert}", style_bullet))
        
    # Build Document
    doc.build(story)
    print(f"ATS PDF successfully generated at: {output_path}")

if __name__ == "__main__":
    output_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Mubarak_Walid_Al_Hammadi_CV_ATS.pdf")
    create_ats_pdf(output_pdf)
