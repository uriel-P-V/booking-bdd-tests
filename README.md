# booking-bdd-tests
 
![CI](https://github.com/uriel-P-V/booking-bdd-tests/actions/workflows/tests.yml/badge.svg)
 
A BDD-based test suite for the RestfulBooker API —
demonstrates multi-feature Gherkin organization, dynamic test data,
token-based authentication, and tag-driven execution for smoke and regression suites.
 
---
 
## Project Structure
 
```
booking-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml                  ← GitHub Actions CI
├── features/
│   ├── steps/
│   │   ├── common_steps.py            ← Shared steps across features
│   │   ├── search_steps.py            ← Search feature steps
│   │   ├── booking_steps.py           ← Booking feature steps
│   │   └── cancellation_steps.py      ← Cancellation feature steps
│   ├── search.feature                 ← List and get reservations
│   ├── booking.feature                ← Create reservations
│   └── cancellation.feature           ← Cancel reservations
└── requirements.txt
```
 
---

## Reports

  After each CI run, an Allure HTML report is generated and available
  as a downloadable artifact in the GitHub Actions summary page.

  To generate locally:
  ```bash
  behave --no-capture --tags=regression \
    -f allure_behave.formatter:AllureFormatter \
    -o allure-results
  allure generate allure-results --clean -o allure-report
  allure open allure-report
  ```

## Features
 
- **Multi-feature BDD** — three independent Gherkin feature files by domain
- **Shared steps** — common_steps.py reused across all features
- **Dynamic test data** — booking IDs created at runtime, no hardcoded IDs
- **Token authentication** — DELETE endpoint tested with auth token
- **Tag-driven execution** — `@smoke` for critical path, `@regression` for full suite
- **GitHub Actions CI** — smoke runs first, regression only if smoke passes
---
 
## BDD Example
 
```gherkin
Feature: Cancellation API
 
  Background:
    Given the booking API is available
    And a valid auth token is obtained
    And a reservation has been created
 
  @smoke
  Scenario: Cancel an existing reservation
    When I cancel the existing reservation
    Then the response status code should be 201
```
 
---
 
## Setup
 
```bash
git clone https://github.com/uriel-P-V/booking-bdd-tests.git
cd booking-bdd-tests
pip install -r requirements.txt
behave
```
 
---
 
## Running Tests
 
```bash
# All scenarios
behave
 
# Smoke only — critical path, hits real API
behave --tags=smoke
 
# Regression only — full suite
behave --tags=regression
 
# Single feature
behave features/search.feature
behave features/booking.feature
behave features/cancellation.feature
```
 
---
 
## CI/CD Pipeline
 
Two dependent jobs run on every push and pull request to `main`:
 
```
push / PR → smoke (3 scenarios) → regression (3 scenarios)
```
 
If `smoke` fails, `regression` is skipped automatically.
 
---
 
## API Under Test
 
**RestfulBooker** — `https://restful-booker.herokuapp.com`  
Public REST API designed for testing practice. Supports full CRUD for hotel bookings with token-based authentication for destructive operations.
 
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ping` | GET | Health check |
| `/booking` | GET | List all bookings |
| `/booking/{id}` | GET | Get booking by ID |
| `/booking` | POST | Create booking |
| `/booking/{id}` | DELETE | Cancel booking (auth required) |
| `/auth` | POST | Get auth token |
 
---
 
## Tech Stack
 
- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **GitHub Actions** — CI/CD pipeline
---
 
## Author
 
**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)