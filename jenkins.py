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

import json
import urllib

JENKINS_PORT = "8080"
PANIC_MONITOR = "Panic%20Monitor"


def get_last_build(changeset):

    build_number = changeset
    print("Getting last build - number ...")
    return build_number


def get_jenkins_server_uri(server_ip):

    jenkins_url = 'http://' + server_ip + ':' + JENKINS_PORT
    print("Jenkins server url..." + jenkins_url)


def get_panic_monitor_job(server_ip):

    panic_url = 'http://' + server_ip + ':' + JENKINS_PORT + '/view/' + PANIC_MONITOR + '/api/json'
    print(panic_url)
    json_response = urllib.urlopen(panic_url)
    json_data = json.loads(json_response.read())
    json_response.close()

    monitor_jobs = json_data['jobs']

    for each_job in monitor_jobs:
        build_number = each_job['name']
        print(build_number)


