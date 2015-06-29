import time
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
 
# Setup the document template ...
doc = SimpleDocTemplate("output.pdf", 
    rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
 
# ... and initialize the content block.
story=[]
 
# Add your logo to the page head. 
story.append(Image('itemize/logo.png', 2*cm, 2*cm))
 
# Fetch the document stylesheet ...
styles = getSampleStyleSheet()
 
# ... and add the justify style.
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
 
# Add the document title to the content block.
story.append(Spacer(0.1*cm, 2*cm))
story.append(Paragraph('<font size=16>My first Report</font>', styles["Center"]))
story.append(Spacer(0.1*cm, 0.5*cm))
 
# Fetch the current date ...
timeStr = '<font size=12>{time}</font>'.format(time = time.ctime())
 
# ... and append it to the content block followed by some space.
story.append(Paragraph(timeStr, styles["Center"]))
story.append(Spacer(0.1*cm, 1*cm))
 
# Setup some normal text ...
text = """This is my first PDF report generated with ReportLab. I think it looks really great 
for a quick and dirty solution. But this is just a first, quick example you could great 
more complex documents using this library.
"""
 
# ... and add it to the document.
story.append(Paragraph(text, styles["Normal"]))
story.append(Spacer(0.1*cm, 3*cm))
 
# And some greetings.
story.append(Paragraph("Best regards<br />LibreTees", styles["Normal"]))
 
# To generate the content and write it to 
# the *.pdf file (in this case firstDoc.pdf) 
# just call the build method.
doc.build(story)
