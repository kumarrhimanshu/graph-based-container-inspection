# Algorithm

## Input

- Destination
- Goods
- Container Length
- Container Weight
- Shipping Company

## Output

- Risk Score (R)
- Inspection Decision

## Algorithm

1. Read the input attributes.
2. Compute the difference between the actual container weight and the standard container capacity.
3. Determine the weight factor according to the predefined thresholds.
4. Obtain the destination factor.
5. Obtain the goods factor.
6. Obtain the shipping company factor.
7. Compute

\[
R=\lambda_1w_1+\lambda_2w_2+\lambda_3w_3+\lambda_4w_4
\]

8. If \(R \le 0.30\), recommend **Store to ship**.
9. Otherwise, recommend **Proceed to further inspection**.
