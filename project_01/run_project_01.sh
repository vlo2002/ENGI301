#!/bin/bash
# --------------------------------------------------------------------------
# Taylor vs. Shakespeare Trivia Run Script
# --------------------------------------------------------------------------
# License:   
# Copyright 2023 Valentina Ortega
# 
# Redistribution and use in source and binary forms, with or without modification, # are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this 
# list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
# this list of conditions and the following disclaimer in the documentation and/or # other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors 
# may be used to endorse or promote products derived from this software without 
# specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND # ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR # ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# --------------------------------------------------------------------------
# Auto-run script
#
# Add to crontab:
#   - In code directory <code>
#     1) mkdir logs
#     2) sudo crontab -e
#     3) @reboot /bin/nano /var/lib/cloud9/ENGI301/project_01/run_project_01.sh > /var/lib/cloud9/logs/cronlog 2>&1
#
# Reboot the PocketBeagle to then auto-run the program
#
# --------------------------------------------------------------------------

cd /var/lib/cloud9/ENGI301/project_01

PYTHONPATH=/var/lib/cloud9/ENGI301/project_01 python3 project_01.py 