# **SUMMARY**


This project analyses the statistical significance of a marketing A/B test results using conversion data. It performs a two-sample proportion z-test to determine whether the difference in conversion rates between two groups is likely to be real or due to chance.

<br>

## **DATA ANALYSIS**


An A/B test was run where visitors were randomly split between two landing page variations:

- Group A (Landing page A): 50 conversions out of 1000 visitors

- Group B (Landing page B): 65 conversions out of 1000 visitors



The results from  running the script were as follows:

- Z-statistic: -1.440

- P-value: 0.150

Interpretation: No statistically significant difference


Although Group B had more conversions (65 vs 50), the difference is not statistically significant. This suggests that the observed increase could have happened by chance and is not a reliable indicator of performance improvement. Since the difference is not significant, scaling Campaign B may not lead to a measurable increase in conversions.

<br>

## **RECCOMENDATIONS**


- Continue running A/B tests with a larger sample size to increase confidence in the results.
- Consider testing other variables, such as different creatives, headlines, or call-to-actions, to identify what drives conversions.
- Avoid making major marketing decisions based on this small, non-significant difference.
<br>


## **USAGE**

1. Clone this repository:

```bash
git clone https://github.com/yourusername/AB_Test_Analysis.git


Make sure you have Python installed along with numpy and statsmodels:
pip install numpy statsmodels


Run the script:
python ab_test_analysis.py


Update the conversions and sample_sizes arrays with your own campaign data to test different A/B experiments.
