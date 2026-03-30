from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'StudyHours': ['High','Low','Medium','High','Low','Medium','High','Low'],
    'Attendance': ['Good','Poor','Good','Good','Poor','Good','Poor','Poor'],
    'PreviousGrades': ['A','C','B','A','C','B','B','C'],
    'Performance': ['Good','Poor','Good','Good','Poor','Good','Good','Poor']
})

model = DiscreteBayesianNetwork([
    ('StudyHours', 'Performance'),
    ('Attendance', 'Performance'),
    ('PreviousGrades', 'Performance')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)

print("CPDs:\n")
for cpd in model.get_cpds():
    print(cpd)
    print("-"*50)

inference = VariableElimination(model)

result = inference.query(
    variables=['Performance'],
    evidence={'StudyHours': 'Low', 'Attendance': 'Poor'}
)

print("\nInference Result:\n", result)
