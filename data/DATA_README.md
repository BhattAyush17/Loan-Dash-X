# Loan Approval Dataset: Field Documentation

| Column          | Description                      | Example Values         |
|-----------------|----------------------------------|-----------------------|
| income          | Annual income (in thousands)     | 45, 120, 80           |
| credit_score    | Credit score (0–1000 scale)      | 680, 820, 900         |
| loans_ongoing   | Number of current loans          | 0, 1, 2, 3            |
| age             | Applicant age (years, 18–75)     | 23, 44, 52            |
| gender          | Applicant gender                 | 'M', 'F', 'Other'     |
| loan_approved   | Target: 1=Approved, 0=Not        | 1, 0                  |

**All entries should be realistic and positive.**
- `income`: Use values between 20 and 150 (in thousands).
- `credit_score`: Use values between 400 and 1000.
- `loans_ongoing`: 0 for no loans, up to 4 for multiple loans.
- `age`: Between 18 and 75.
- `gender`: Use 'M', 'F', or 'Other'.
- `loan_approved`: Use 1 for approved, 0 for not approved.

Example entry:
`80,900,0,52,M,1`