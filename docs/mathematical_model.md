# Mathematical Model

The Graph-Theoretic Algorithmic Inspection (GTA) framework models the container inspection process as a weighted graph

\[
G=(V,E)
\]

where:

- **Vertices** represent:
  - Container
  - Goods
  - Destination
  - Shipping Company

- **Edges** represent relationships among these entities.

Each edge is assigned a weight based on operational characteristics.

The overall inspection score is computed using

\[
R=\sum_{i=1}^{4}\lambda_iw_i
\]

where

- \(w_i\) is the weight of an inspection attribute.
- \(\lambda_i\) is the corresponding priority factor.

The decision rule is

- If \(R \le 0.30\): **Store to ship**
- Otherwise: **Proceed to further inspection**
