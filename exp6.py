from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame(data={
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})


model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)

print("Conditional Probability Distributions (CPDs):\n")
for cpd in model.get_cpds():
    print(cpd)
    print("-" * 50)

inference = VariableElimination(model)
query_result = inference.query(variables=['ArriveLate'], evidence={'Rain': 'Yes'})
print("\nInference Result:\n", query_result)
