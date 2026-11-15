# Week 2: Anatomy of Code - Variables, Data Types & Memory

engineer_name = "Rey Navarro"        # str (String)
program_weeks = 24                   # int (Integer)
completion_rate = 4.16               # float (Floating-point)
is_remote_ready = True               # bool (Boolean)

# f-strings let us inject variables directly into text
print(f"Engineer: {engineer_name}")
print(f"Curriculum Length: {program_weeks} weeks ({completion_rate}% complete)")

# Inspecting the exact data type and RAM memory address
print("Data type of program_weeks:", type(program_weeks))
print("Memory address in RAM:", id(engineer_name))
# --- Part 2: Memory Rebinding & Logical Operators ---

# Rebinding a variable points the name tag to a NEW RAM address
weeks_completed = 1
print("\nInitial weeks_completed RAM address:", id(weeks_completed))

weeks_completed = weeks_completed + 1
print("Updated weeks_completed RAM address:", id(weeks_completed))

# Comparison & Logical Operators (Boolean Algebra)
has_github_repo = True
hours_studied = 3

ready_for_week_3 = (weeks_completed >= 2) and has_github_repo and (hours_studied > 1)
print(f"\nWeeks completed: {weeks_completed} | Ready for Week 3? {ready_for_week_3}")
print("Data type of ready_for_week_3:", type(ready_for_week_3))
