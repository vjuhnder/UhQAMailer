#!/usr/bin/env python
# START_SOFTWARE_LICENSE_NOTICE
# -------------------------------------------------------------------------------------------------------------------
# Copyright (C) 2016-2017 Uhnder, Inc. All rights reserved.
# This Software is the property of Uhnder, Inc. (Uhnder) and is Proprietary and Confidential.  It has been provided
# under license for solely use in evaluating and/or developing code for Uhnder products.  Any use of the Software to
# develop code for a product not manufactured by or for Uhnder is prohibited.  Unauthorized use of this Software is
# strictly prohibited.
# Restricted Rights Legend:  Use, Duplication, or Disclosure by the Government is Subject to Restrictions as Set
# Forth in Paragraph (c)(1)(ii) of the Rights in Technical Data and Computer Software Clause at DFARS 252.227-7013.
# THIS PROGRAM IS PROVIDED UNDER THE TERMS OF THE UHNDER END-USER LICENSE AGREEMENT (EULA). THE PROGRAM MAY ONLY
# BE USED IN A MANNER EXPLICITLY SPECIFIED IN THE EULA, WHICH INCLUDES LIMITATIONS ON COPYING, MODIFYING,
# REDISTRIBUTION AND WARRANTIES. PROVIDING AFFIRMATIVE CLICK-THROUGH CONSENT TO THE EULA IS A REQUIRED PRECONDITION
# TO YOUR USE OF THE PROGRAM. YOU MAY OBTAIN A COPY OF THE EULA FROM WWW.UHNDER.COM. UNAUTHORIZED USE OF THIS
# PROGRAM IS STRICTLY PROHIBITED.
# THIS SOFTWARE IS PROVIDED "AS IS".  NO WARRANTIES ARE GIVEN, WHETHER EXPRESS, IMPLIED OR STATUTORY, INCLUDING
# WARRANTIES OR MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT AND TITLE.  RECIPIENT SHALL HAVE
# THE SOLE RESPONSIBILITY FOR THE ADEQUATE PROTECTION AND BACK-UP OF ITS DATA USED IN CONNECTION WITH THIS SOFTWARE.
# IN NO EVENT WILL UHNDER BE LIABLE FOR ANY CONSEQUENTIAL DAMAGES WHATSOEVER, INCLUDING LOSS OF DATA OR USE, LOST
# PROFITS OR ANY INCIDENTAL OR SPECIAL DAMAGES, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE, WHETHER IN ACTION OF CONTRACT OR TORT, INCLUDING NEGLIGENCE.  UHNDER FURTHER DISCLAIMS ANY LIABILITY
# WHATSOEVER FOR INFRINGEMENT OF ANY INTELLECTUAL PROPERTY RIGHTS OF ANY THIRD PARTY.
# -------------------------------------------------------------------------------------------------------------------
# END_SOFTWARE_LICENSE_NOTICE

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import report


def send_email(job_names, job_url, html_table):
    addressto = "All"
    changeset = "abcdefgh"
    commit_msg = "This is commit message"

    # TODO: Get addressto
    # TODO: Get Changeset
    # TODO: Get commit message

    message = 'Hi ' \
              + addressto + ','

    message += '<br><br>&nbsp;&nbsp;&nbsp;&nbsp;Your commit with <b>changeset:&nbsp;' \
               + changeset \
               + '</b>, with changes (<b>' \
               + commit_msg \
               + '</b>) is breaking the build.<br><br>'

    message += '<br><br>&nbsp;&nbsp;&nbsp;&nbsp;<b>Panic Board Summary<b><br><br>' \
               + html_table \
               + '<br><br><br>Thanks & Regards, <br> <b>UhDC QA Team</b>'

    msg = MIMEMultipart()
    msg['From'] = 'jenkins@uhnder.com'
    # TODO: Get names to send email
    msg['To'] = 'vigneswaran@uhnder.com'

    msg['Subject'] = "DO NOT REPLY***PANIC***NOTIFICATION "

    msg.attach(MIMEText(message, 'html'))

    # TODO: attach log file
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # TODO: Store password in a file or get from a file
    server.login('jenkins@uhnder.com', "fcnsslpffwpchlkq")
    text = msg.as_string()
    server.sendmail('jenkins@uhnder.com', "vigneswaran@uhnder.com", text)
    server.quit()

    print("Sending Email.....")
