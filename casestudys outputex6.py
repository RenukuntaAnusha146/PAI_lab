Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
====================== RESTART: C:/088/casestudy2 exp6.py ======================
Microsoft Visual C++ Redistributable is not installed, this may lead to the DLL load failure.
It can be downloaded at https://aka.ms/vs/17/release/vc_redist.x64.exe
INFO:pgmpy: Datatype (N=numerical, C=Categorical Unordered, O=Categorical Ordered) inferred from data: 
 {'StudyHours': 'C', 'Attendance': 'C', 'PreviousGrades': 'C', 'Performance': 'C'}
CPDs:

+--------------------+-------+
| StudyHours(High)   | 0.375 |
+--------------------+-------+
| StudyHours(Low)    | 0.375 |
+--------------------+-------+
| StudyHours(Medium) | 0.25  |
+--------------------+-------+
--------------------------------------------------
+-------------------+-----+--------------------+
| Attendance        | ... | Attendance(Poor)   |
+-------------------+-----+--------------------+
| PreviousGrades    | ... | PreviousGrades(C)  |
+-------------------+-----+--------------------+
| StudyHours        | ... | StudyHours(Medium) |
+-------------------+-----+--------------------+
| Performance(Good) | ... | 0.5                |
+-------------------+-----+--------------------+
| Performance(Poor) | ... | 0.5                |
+-------------------+-----+--------------------+
--------------------------------------------------
+------------------+-----+
| Attendance(Good) | 0.5 |
+------------------+-----+
| Attendance(Poor) | 0.5 |
+------------------+-----+
--------------------------------------------------
+-------------------+-------+
| PreviousGrades(A) | 0.25  |
+-------------------+-------+
| PreviousGrades(B) | 0.375 |
+-------------------+-------+
| PreviousGrades(C) | 0.375 |
+-------------------+-------+
--------------------------------------------------

Inference Result:
 +-------------------+--------------------+
| Performance       |   phi(Performance) |
+===================+====================+
| Performance(Good) |             0.3125 |
+-------------------+--------------------+
| Performance(Poor) |             0.6875 |
+-------------------+--------------------+

====================== RESTART: C:/088/case study1 exp6.py =====================
Microsoft Visual C++ Redistributable is not installed, this may lead to the DLL load failure.
It can be downloaded at https://aka.ms/vs/17/release/vc_redist.x64.exe
INFO:pgmpy: Datatype (N=numerical, C=Categorical Unordered, O=Categorical Ordered) inferred from data: 
 {'IncomeStability': 'C', 'CreditHistory': 'C', 'EmploymentType': 'C', 'DefaultRisk': 'C'}
CPDs:

+-------------------------+-------+
| IncomeStability(High)   | 0.375 |
+-------------------------+-------+
| IncomeStability(Low)    | 0.375 |
+-------------------------+-------+
| IncomeStability(Medium) | 0.25  |
+-------------------------+-------+
--------------------------------------------------
+------------------+-----+-------------------------+
| CreditHistory    | ... | CreditHistory(Poor)     |
+------------------+-----+-------------------------+
| EmploymentType   | ... | EmploymentType(Self)    |
+------------------+-----+-------------------------+
| IncomeStability  | ... | IncomeStability(Medium) |
+------------------+-----+-------------------------+
| DefaultRisk(No)  | ... | 0.5                     |
+------------------+-----+-------------------------+
| DefaultRisk(Yes) | ... | 0.5                     |
+------------------+-----+-------------------------+
--------------------------------------------------
+---------------------+-----+
| CreditHistory(Good) | 0.5 |
+---------------------+-----+
| CreditHistory(Poor) | 0.5 |
+---------------------+-----+
--------------------------------------------------
+--------------------------+-----+
| EmploymentType(Salaried) | 0.5 |
+--------------------------+-----+
| EmploymentType(Self)     | 0.5 |
+--------------------------+-----+
--------------------------------------------------

Inference Result:
 +------------------+--------------------+
| DefaultRisk      |   phi(DefaultRisk) |
+==================+====================+
| DefaultRisk(No)  |             0.2500 |
+------------------+--------------------+
| DefaultRisk(Yes) |             0.7500 |
+------------------+--------------------+
