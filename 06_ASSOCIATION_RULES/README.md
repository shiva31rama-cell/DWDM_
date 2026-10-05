# 06. Association Rules and Knowledge Flow

## Aim
Find strong rules with Apriori/FP-Growth and configure a Knowledge Flow experiment.

## Association procedure
1. Load transactional data.
2. Run Apriori with selected support/confidence.
3. Run FP-Growth where available.
4. Compare strong rules.

## Knowledge Flow
Loader → Preprocess/Filter → J48 → Cross-validation → Performance Evaluation → ROC/Visualization.

For comparison, connect J48 and RandomForest to the evaluation/visualization path supported by the installed WEKA version.

## Result
Strong association rules and classifier performance comparisons are obtained.