# LIBRARIES USED
# numpy      -> stores the observed data as a numerical array.
# pandas     -> displays the observed/expected data as tables.
# scipy.stats -> provides the Chi-Square statistical test.
# These are libraries, not our dataset.
#
# DATASET
# The dataset is a 2 x 2 frequency table.
# Rows represent Young and Old.
# Columns represent Apple and Orange.
# The numbers are observed frequencies (counts).
#
# HOW IT WORKS
# 1. Store the observed frequencies.
# 2. Calculate expected frequencies.
# 3. Apply the Chi-Square formula using scipy.
# 4. Display the result and observation.

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# 1. Create the data matrix
# Rows = Young, Old
# Columns = Apple, Orange
data = np.array([[50, 10], [20, 40]])

# 2. Display the observed table
df = pd.DataFrame(
    data,
    index=["Young", "Old"],
    columns=["Apple", "Orange"]
)

print("--- Observed Data Table ---")
print(df)
print("\n" + "=" * 50)

# 3. Perform Chi-Square Test
# correction=False gives the classic textbook calculation.
chi2, p_value, degrees, expected = chi2_contingency(
    data,
    correction=False
)

# 4. Display the results
print("--- Chi-Square Test Results ---")
print("Calculated Chi-Square Value: %.4f" % chi2)
print("P-Value: %.6f" % p_value)
print("Degrees of Freedom:", degrees)

print("\n--- Expected Frequencies Table ---")
expected_df = pd.DataFrame(
    expected,
    index=["Young", "Old"],
    columns=["Apple", "Orange"]
)
print(expected_df.round(2))

# 5. Observation
print("\nObservation:")
if p_value < 0.05:
    print("The variables are significantly associated.")
else:
    print("There is no significant association.")
