import string

# ---------------------------------------------------------
# STEP 1: Preloaded Tickets Data
# ---------------------------------------------------------
ticket_data = {
    'Ticket_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Customer_Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Rakesh', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Issue_Description': [
        'Internet not working!!!', 'slow response, very poor service',
        'GREAT support! issue resolved.', ' okay... need help', 'not BAD but slow', 
        'Excellent guidance, Very Helpful!!', 'good support and good behaviour!', 
        'Poor handling of technical issue', 'Satisfied. Could be better.', 
        'Good service... quick response.'
    ],
    'Priority': ['High', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'High', 'Low', 'Medium']
}

print("=== STEP 1: Initial Ticket Data ===")
for i in range(len(ticket_data['Ticket_No'])):
    print(f"Ticket #{ticket_data['Ticket_No'][i]} | {ticket_data['Customer_Name'][i]} | Priority: {ticket_data['Priority'][i]} | Issue: {ticket_data['Issue_Description'][i]}")


# ---------------------------------------------------------
# STEP 2: Add New Tickets (Interactive Input)
# ---------------------------------------------------------
print("\n=== STEP 2: Add New Tickets ===")
try:
    num_new = int(input("How many new tickets do you want to add? (Enter 0 to skip): "))
except ValueError:
    num_new = 0

current_id = 11
for _ in range(num_new):
    name = input(f"\nEnter name for Ticket #{current_id}: ")
    issue = input("Enter issue description: ")
    
    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        if priority in ['High', 'Medium', 'Low']:
            break
        print("Invalid priority! Please enter High, Medium, or Low.")
        
    ticket_data['Ticket_No'].append(current_id)
    ticket_data['Customer_Name'].append(name)
    ticket_data['Issue_Description'].append(issue)
    ticket_data['Priority'].append(priority)
    current_id += 1


# ---------------------------------------------------------
# STEP 3: Text Cleaning
# ---------------------------------------------------------
print("\n=== STEP 3: Cleaning Text ===")
cleaned_descriptions = []
slang_dict = {"ok": "okay"}

for text in ticket_data['Issue_Description']:
    text_clean = text.lower()
    text_clean = text_clean.translate(str.maketrans('', '', string.punctuation))
    words = [slang_dict.get(w, w) for w in text_clean.split()]
    cleaned_descriptions.append(' '.join(words).strip())

ticket_data['Issue_Description'] = cleaned_descriptions
print("Text cleaning completed successfully!")


# ---------------------------------------------------------
# STEP 4: Keyword-Based Insights
# ---------------------------------------------------------
def count_tickets_with_word(word):
    word_lower = word.lower()
    return sum(1 for desc in ticket_data['Issue_Description'] if word_lower in desc.split())

print("\n=== STEP 4: Keyword Analysis ===")
for kw in ["poor", "good", "slow", "excellent"]:
    print(f"Number of tickets containing '{kw}': {count_tickets_with_word(kw)}")


# ---------------------------------------------------------
# STEP 5: Final Summary & Insights
# ---------------------------------------------------------
print("\n=== STEP 5: Final Analytics & Summary ===")

# 1. Cleaned Data Output
print("\n1. Cleaned Ticket Data Dictionary:")
print(ticket_data)

# 2. Priority Breakdown
print("\n2. Priority Breakdown:")
print(f"High Priority Tickets: {ticket_data['Priority'].count('High')}")
print(f"Medium Priority Tickets: {ticket_data['Priority'].count('Medium')}")
print(f"Low Priority Tickets: {ticket_data['Priority'].count('Low')}")

# 3. Longest Description Finder
word_counts = [len(desc.split()) for desc in ticket_data['Issue_Description']]
max_idx = word_counts.index(max(word_counts))

print("\n3. Ticket with Longest Issue Description:")
print(f"Ticket No: {ticket_data['Ticket_No'][max_idx]}")
print(f"Customer Name: {ticket_data['Customer_Name'][max_idx]}")
print(f"Cleaned Issue: {ticket_data['Issue_Description'][max_idx]}")
print(f"Word Count: {word_counts[max_idx]}")

# 4. Unique Words Extraction
all_words = set()
for desc in ticket_data['Issue_Description']:
    all_words.update(desc.split())

print("\n4. Unique Words Analysis:")
print(f"Count of Unique Words: {len(all_words)}")
print(f"Sorted Word List: {sorted(list(all_words))}")
