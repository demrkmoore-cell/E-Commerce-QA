# Demoblaze QA Execution Results

## Project

**Application:** Demoblaze Product Store  
**Repository:** `demrkmoore-cell/E-Commerce-QA`  
**Jira Project:** EQAP  
**Execution type:** Manual functional / regression-oriented testing  
**Environment:** Desktop Chrome  
**Execution scope:** Product catalog, navigation, categories, product details, shopping cart, checkout, negative/boundary validation, persistence and browser refresh behavior.

## Important distinction

This file records the **executed testing performed during the project session**. The existing `test-cases/functional-test-cases.md` remains the **planned functional test suite** and should not be rewritten to claim execution that was not explicitly mapped back to those planned IDs.

## Execution Summary

| Result | Count |
|---|---:|
| Passed | 92 |
| Failed | 13 |
| Blocked | 1 |
| **Total Executions** | **106** |

## Coverage Demonstrated

- Registration and login behavior
- Product navigation and category filtering
- Product detail pages
- Product names, prices, descriptions and images
- Add-to-cart and delete behavior
- Single-item and multi-item cart calculations
- Duplicate cart items
- Cart persistence across refresh/navigation/category changes
- Browser Back/refresh behavior
- Checkout totals and cart-state transitions
- Checkout validation for credit-card, expiration-month and expiration-year inputs
- Empty-cart behavior
- Positive and negative boundary checks

## Confirmed Jira Defects

| Jira | Defect | Classification |
|---|---|---|
| EQAP-3 | Registered user cannot log in after successful registration | Confirmed defect |
| EQAP-4 | Empty shopping cart displays a blank total | Confirmed defect |
| EQAP-5 | Checkout accepts invalid credit-card input | Confirmed defect |
| EQAP-6 | Checkout accepts invalid expiration month | Confirmed defect |
| EQAP-7 | Checkout accepts invalid/expired expiration year | Confirmed defect |
| EQAP-8 | Checkout can be initiated with an empty cart | Confirmed defect |
| EQAP-9 | Original multi-category cart-loss scenario was observed once, then not reproduced in follow-up | Non-reproducible / investigate |

## Key Evidence From Execution

### Checkout validation

- Month `00` was accepted incorrectly → EQAP-6
- Month `13` was accepted incorrectly → EQAP-6
- Month `01` was accepted correctly
- Month `12` was accepted correctly
- Year `0000` was accepted incorrectly → EQAP-7
- Expired year `2020` was accepted incorrectly → EQAP-7
- Valid year `2026` was accepted correctly
- Invalid card value `123` was accepted → EQAP-5
- Alphabetic card value `ABCDEF` was accepted → EQAP-5
- Mixed-format value `1234-ABCD` was accepted → EQAP-5

### Cart / product behavior

- Product/category price consistency verified across product detail and cart
- Duplicate product entries were accepted and totals recalculated correctly
- Individual duplicate deletion recalculated totals correctly
- Empty-cart total repeatedly appeared blank → EQAP-4
- Cart persistence through refresh and category navigation was repeatedly validated
- Three-category carts passed in later runs, so EQAP-9 was not treated as a consistently reproducible defect

## Evidence Handling

Checkout screenshots should use redacted card-number evidence such as `**** **** **** 1111` before being committed to GitHub or attached to Jira. Do not publish screenshots containing a full payment-card number.

## Portfolio Interpretation

The execution demonstrates a practical manual QA workflow: create a planned suite, execute risk-based scenarios, capture evidence, report defects in Jira, retest defect boundaries, and distinguish confirmed defects from non-reproducible behavior.

## Source of Truth

The numeric execution summary above reflects the completed project execution session. Individual planned test cases remain in `test-cases/functional-test-cases.md`; future work should map executed cases to those planned IDs where a one-to-one mapping is required.
