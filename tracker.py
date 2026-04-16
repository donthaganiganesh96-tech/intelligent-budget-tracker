import json

def analyze_expenses(file_path, budget):
    try:
        with open(file_path, 'r') as f:
            expenses = json.load(f)
        
        total_spent = sum(item['amount'] for item in expenses)
        print(f"--- Budget Report ---")
        print(f"Total Spent: ${total_spent}")
        print(f"Budget Limit: ${budget}")

        if total_spent > budget:
            print("⚠️ ALERT: You have exceeded your budget!")
        else:
            print("✅ Status: You are within your budget.")
            
    except FileNotFoundError:
        print("Error: expenses.json not found.")

if __name__ == "__main__":
    # Example budget of $500
    analyze_expenses('expenses.json', 500)
