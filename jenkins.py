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


class PanicMonitor:
    def __init__(self, server_ip):
        self.job_names = []
        self.failed_jobs = []
        self.succeed_jobs = []
        self.failed_progress_job = []
        self.succeed_progress_job = []
        self.server_ip = server_ip
        self.job_count = 0
        self.job_url = []
        self.sno = []
        self.job_status = {}

    def get_url_json(self, get_url):
        get_url += '/api/json'
        json_response = urllib.urlopen(get_url)
        json_data = json.loads(json_response.read())
        json_response.close()
        return json_data

    def get_jobs_details(self):
        get_url = 'http://' + self.server_ip + ':' + JENKINS_PORT + '/view/' + PANIC_MONITOR
        json_data = self.get_url_json(get_url)

        monitor_jobs = json_data['jobs']
        self.job_count = 0
        # parse the jobs array
        for each_job in monitor_jobs:
            self.job_count += 1
            self.sno.append(self.job_count)
            job_name = each_job['name']
            self.job_names.append(job_name)
            self.job_url.append(each_job['url'])
            status = each_job['color']

            if status == 'blue' or status == 'blue_anime':
                self.succeed_jobs.append(job_name)
                self.job_status[job_name] = "SUCCESS"
            elif status == 'red':
                self.failed_jobs.append(job_name)
                self.job_status[job_name] = "FAILED"
            elif status == "red_anime":
                self.failed_progress_job(job_name)
                self.job_status[job_name] = "FAILED"

    def get_last_build(self, job_url):
        json_data = self.get_url_json(job_url)
        last_build_url = json_data['lastBuild']['url']
        return last_build_url

    def get_jenkins_server_uri(self):

        jenkins_url = 'http://' + self.server_ip + ':' + JENKINS_PORT
        print("Jenkins server url..." + jenkins_url)

    def create_table(self):
        # TODO: Get last build url, console log attachment

        html_table = '<style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, ' \
                     'th {border: 1px solid #dddddd;text-align: left;padding: 8px;}</style><table><tr><th>S. No</th>' \
                     '<th>Job Name</th><th>Build Status</th><th>Jenkins URL</th></tr>'
        index = 0

        print (self.job_status)

        for each_job in self.job_names:
            if self.job_status[each_job] == "SUCCESS":
                color = "green"
            else:
                color = "red"

            html_table += '<tr style="color: %s;"><td>' %(color) \
                          + str(self.sno[index]) \
                          + '</td><td>' \
                          + each_job \
                          + '</td><td>%s</td><td><a href="%s"> Jenkins URL </a></tr>' \
                          % (self.job_status[each_job], self.get_last_build(self.job_url[index]) + "console")
            index += 1

        html_table += '</table>'

        return html_table










