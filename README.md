# SETIA – Self-Evolving Topic Intelligence Agent

SETIA is an agentic AI-based review analysis system that processes Google Play Store
reviews to identify user issues, consolidate similar topics, and generate
time-based trend reports.

The system is designed to help product teams understand what users are complaining
about and how those issues evolve over time.

---

## Problem Statement
User reviews often describe the same issue using different wording.
Traditional topic modeling techniques fail to group these accurately,
leading to fragmented trends.

---

## Solution Overview
SETIA follows an agentic architecture where each step of the pipeline
is handled by a dedicated agent:

- Review Fetching Agent – fetches real user reviews from Google Play Store
- Issue Extraction Agent – extracts user issues with high recall
- Deduplication & Counting Agent – consolidates issues and counts them per day
- Trend Generator – produces date-wise trend reports

---

## Agentic Architecture

