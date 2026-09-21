# Financial Chatbot — Documentation

## Overview
A rule-based financial chatbot that responds to predefined queries about 
Microsoft, Tesla, and Apple using data analyzed in Task 1 (2023–2025).

## How It Works
- Uses `if-elif-else` statements to match user input to canned responses
- Input is normalized (lowercased and stripped of whitespace) for forgiving matching
- Runs as a command-line loop via Python's `input()` function
- Exits when the user types `exit`, `quit`, or `bye`
- Falls back to a help message for unrecognized queries

## Predefined Queries Supported
1. What is Microsoft's total revenue?
2. How has net income changed over the last year?
3. What is Tesla's net income?
4. What is Apple's total revenue?
5. Which company had the highest revenue growth?

## Test Results
All 5 predefined queries returned correct responses based on the analyzed 
financial data. The fallback response was verified using an out-of-scope 
query ("What is Google's revenue?"). See `test_results.txt` for the full 
terminal session.

## Limitations
- Only responds to the 5 predefined queries via exact match (case-insensitive)
- Does not understand synonyms, paraphrases, or free-form questions
- Responses are hardcoded from the analyzed data; not loaded dynamically
- No memory between queries; no multi-turn conversation
- No predictions, sentiment analysis, or open-ended reasoning

## Potential Improvements
- Load `forage_data.csv` dynamically and generate responses from the DataFrame
- Use keyword matching or fuzzy matching for more natural input handling
- Extend to a Flask web interface for browser-based interaction
- Integrate an LLM for open-ended financial questions

## File Inventory
- `financial_chatbot.py` — the chatbot script
- `test_results.txt` — terminal output from the test session
- `documentation.md` — this file