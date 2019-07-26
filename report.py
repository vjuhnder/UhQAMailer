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


def create_table():
    # TODO: Get Job names, Build status and Jenkins URL
    # no = 1
    html_table = '<style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, ' \
                 'th {border: 1px solid #dddddd;text-align: left;padding: 8px;}</style><table><tr><th>S. No</th>' \
                 '<th>Job Name</th><th>Build Status</th><th>Jenkins URL</th></tr>'
#    for job_name in bad_job:
#        html_table += '<tr style="color: red;"><td>'+str(no)+'</td><td>'+job_name+'</td><td>FAILED</td><td>
#        <a href="%s/job/%s/%s/console"> Jenkins URL </a></tr>' %(jenkins_url, job_name,
#        job_details[job_name]['build_number'])
#        no += 1
#    for job_name in job_names:
#        if not job_name in bad_job:
#            html_table += '<tr><td>'+str(no)+'</td><td>'+job_name+'</td><td>SUCCESS</td><td>
#            <a href="%s/job/%s/%s/console"> Jenkins URL </a></tr>' %(jenkins_url, job_name,
#            job_details[job_name]['build_number'])
#            no += 1
    html_table += '</table>'
    return html_table
