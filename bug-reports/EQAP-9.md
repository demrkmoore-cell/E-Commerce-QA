# EQAP-9 — Original Multi-Category Cart-Loss Observation

**Status:** Investigation / Non-reproducible  
**Classification:** Non-reproducible behavior  
**Test Type:** Functional / Cart / Multi-category

## Summary
An earlier execution appeared to lose a product from a three-category cart. Because the behavior did not reproduce in controlled follow-up testing, it is not currently classified as a consistently reproducible defect.

## Original Observation
The original scenario involved:

- Samsung Galaxy S6 — $360
- Apple monitor 24 — $400
- Sony Vaio i5 — $790
- Expected total: **$1,550**

## Follow-up Testing
The same combination and sequence was repeated and all three products remained in the cart with a total of **$1,550**.

Additional three-category combinations also passed, including:

- Nexus 6 — $650
- MacBook Pro — $1,100
- ASUS Full HD — $230
- Total: **$1,980**

Two-category combinations also passed for phone + laptop, phone + monitor, and laptop + monitor.

## Current Assessment
**Not reproducible.** The original behavior should remain documented for traceability, but the available follow-up evidence does not support describing the issue as a consistently reproducible product/cart defect.

## Recommended Next Step
If the issue reappears, capture the exact product-add sequence, timestamps, browser state, cart state before and after each addition, and screenshot evidence so the behavior can be compared against the successful retests.

## Evidence
See Jira **EQAP-9** and the execution record in `test-summary/execution-results.md`.
