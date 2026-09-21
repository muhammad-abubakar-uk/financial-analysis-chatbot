# Financial Analysis & AI Chatbot

A two-part project completed as part of the **BCG GenAI Job Simulation on Forage**. It analyses FY2023–2025 10-K financial data for Microsoft, Tesla, and Apple, and surfaces the insights through an interactive rule-based chatbot.

## Project Overview

| Task | Description | Tech Stack |
|------|-------------|------------|
| **Task 1 — Data Analysis** | Extracted, cleaned, and analysed revenue and net income trends across three companies | Python, pandas, Jupyter |
| **Task 2 — Financial Chatbot** | Built a rule-based chatbot that answers predefined financial queries | Python, CLI (`input()`) |

## Key Findings

- **Microsoft** delivered the most consistent growth: **+15.30%** average revenue growth and **+18.67%** average net income growth across FY2023–2025.
- **Apple** showed a V-shaped recovery: a small net income dip in 2024 (**-3.36%**) followed by a strong **+19.50%** rebound in 2025.
- **Tesla** experienced the sharpest decline: revenue was essentially flat (**-0.99%** average growth), while net income collapsed by **-49.17%** on average per year.

## Repository Structure

```
financial-analysis-chatbot/
├── README.md
├── requirements.txt
├── task1-analysis/
│   ├── forage_analysis_v2.ipynb     # Jupyter notebook with full analysis
│   └── forage_data.csv              # Clean dataset (long format)
└── task2-chatbot/
    ├── financial_chatbot.py         # The chatbot script
    ├── test_results.txt             # Terminal output from testing
    └── documentation.md             # Chatbot documentation
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/muhammad-abubakar-uk/financial-analysis-chatbot.git
cd financial-analysis-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis notebook

```bash
jupyter notebook task1-analysis/forage_analysis_v2.ipynb
```

### 4. Run the chatbot

```bash
python task2-chatbot/financial_chatbot.py
```

## Predefined Chatbot Queries

The chatbot responds to the following queries:

1. What is Microsoft's total revenue?
2. How has net income changed over the last year?
3. What is Tesla's net income?
4. What is Apple's total revenue?
5. Which company had the highest revenue growth?

**Example interaction:**

```
You: What is Microsoft's total revenue?
Bot: Microsoft's total revenue in 2025 was $281,724 million, up from
     $245,122M in 2024 and $211,915M in 2023.
```

## Skills Demonstrated

- **Data analysis:** pandas, `groupby`, time-series growth calculations
- **Data cleaning:** type conversion, string normalisation, wide-to-long reshaping
- **Jupyter workflow:** markdown documentation, Restart & Run All validation
- **Python scripting:** functions, loops, conditional logic, CLI input/output
- **Documentation:** methodology write-ups, test results, limitations analysis

## Limitations & Future Work

- The chatbot responds only to exact-match predefined queries — no NLP or LLM integration
- Data is hardcoded; it could be loaded dynamically from the CSV
- A Flask web interface would improve usability
- Adding matplotlib visualisations would strengthen the analysis

## Acknowledgements

This project was completed as part of the **BCG GenAI Job Simulation on Forage**. The simulation is a self-paced learning experience, not an employment relationship with BCG.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
