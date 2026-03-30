from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'IncomeStability': ['High','Low','Medium','High','Low','Medium','High','Low'],
    'CreditHistory': ['Good','Poor','Good','Good','Poor','Good','Poor','Poor'],
    'EmploymentType': ['Salaried','Self','Salaried','Self','Self','Salaried','Salaried','Self'],
    'DefaultRisk': ['No','Yes','No','No','Yes','No','Yes','Yes']
})

model = DiscreteBayesianNetwork([
    ('IncomeStability', 'DefaultRisk'),
    ('CreditHistory', 'DefaultRisk'),
    ('EmploymentType', 'DefaultRisk')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)

print("CPDs:\n")
for cpd in model.get_cpds():
    print(cpd)
    print("-"*50)

inference = VariableElimination(model)

result = inference.query(
    variables=['DefaultRisk'],
    evidence={'IncomeStability': 'Low', 'CreditHistory': 'Poor'}
)

print("\nInference Result:\n", result)
