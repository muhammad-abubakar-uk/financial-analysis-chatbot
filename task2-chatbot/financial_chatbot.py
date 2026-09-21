# financial_chatbot.py
# AI-Powered Financial Chatbot - Task 2
# Analyzes Microsoft, Tesla, and Apple financial data (2023-2025)

def simple_chatbot(user_query):
    """Return a canned response for predefined financial queries."""
    
    # Normalize input: lowercase + strip whitespace for forgiving matching
    query = user_query.lower().strip()
    
    # Query 1: Microsoft total revenue
    if query == "what is microsoft's total revenue?":
        return ("Microsoft's total revenue in 2025 was $281,724 million, "
                "up from $245,122M in 2024 and $211,915M in 2023.")
    
    # Query 2: Net income change over the last year
    elif query == "how has net income changed over the last year?":
        return ("Microsoft's net income increased by 15.54% from $88,136M (2024) "
                "to $101,832M (2025). Apple's net income increased by 19.50%, "
                "while Tesla's net income decreased by 46.11%.")
    
    # Query 3: Tesla net income
    elif query == "what is tesla's net income?":
        return ("Tesla's net income in 2025 was $3,855 million, down sharply "
                "from $7,153M in 2024 and $14,974M in 2023.")
    
    # Query 4: Apple total revenue
    elif query == "what is apple's total revenue?":
        return ("Apple's total revenue in 2025 was $416,161 million, "
                "up from $391,035M in 2024 and $383,285M in 2023.")
    
    # Query 5: Highest revenue growth
    elif query == "which company had the highest revenue growth?":
        return ("Microsoft had the highest average revenue growth at 15.30% per year, "
                "followed by Apple at 4.22% and Tesla at -0.99%.")
    
    # Fallback
    else:
        return ("Sorry, I can only provide information on predefined queries. "
                "Try asking about revenue, net income, or growth for "
                "Microsoft, Tesla, or Apple.")


def main():
    """Command-line interface loop."""
    print("=" * 60)
    print("Financial Chatbot — Microsoft, Tesla, Apple (2023-2025)")
    print("=" * 60)
    print("\nPredefined queries you can ask:")
    print("  1. What is Microsoft's total revenue?")
    print("  2. How has net income changed over the last year?")
    print("  3. What is Tesla's net income?")
    print("  4. What is Apple's total revenue?")
    print("  5. Which company had the highest revenue growth?")
    print("\nType 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit", "bye"):
            print("Bot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()