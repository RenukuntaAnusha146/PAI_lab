Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=========================== RESTART: C:/088/bayes.py ===========================
Microsoft Visual C++ Redistributable is not installed, this may lead to the DLL load failure.
It can be downloaded at https://aka.ms/vs/17/release/vc_redist.x64.exe
INFO:pgmpy: Datatype (N=numerical, C=Categorical Unordered, O=Categorical Ordered) inferred from data: 
 {'Rain': 'C', 'TrafficJam': 'C', 'ArriveLate': 'C'}
Conditional Probability Distributions (CPDs):

+-----------+-----+
| Rain(No)  | 0.5 |
+-----------+-----+
| Rain(Yes) | 0.5 |
+-----------+-----+
--------------------------------------------------
+-----------------+----------+-----------+
| Rain            | Rain(No) | Rain(Yes) |
+-----------------+----------+-----------+
| TrafficJam(No)  | 0.5      | 0.5       |
+-----------------+----------+-----------+
| TrafficJam(Yes) | 0.5      | 0.5       |
+-----------------+----------+-----------+
--------------------------------------------------
+-----------------+----------------+-----------------+
| TrafficJam      | TrafficJam(No) | TrafficJam(Yes) |
+-----------------+----------------+-----------------+
| ArriveLate(No)  | 0.75           | 0.25            |
+-----------------+----------------+-----------------+
| ArriveLate(Yes) | 0.25           | 0.75            |
+-----------------+----------------+-----------------+
--------------------------------------------------

Inference Result:
 +-----------------+-------------------+
| ArriveLate      |   phi(ArriveLate) |
+=================+===================+
| ArriveLate(No)  |            0.5000 |
+-----------------+-------------------+
| ArriveLate(Yes) |            0.5000 |
+-----------------+-------------------+
