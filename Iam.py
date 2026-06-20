# sets employee details
employee = ["John", "Cloud Engineer", "Full time"]
# sets default access groups
access_groups = ["email", "slack", "company_wiki"]

# gets employee name
emp_name = employee[0]
# gets employee department
emp_dept = employee[1]
# gets employee status
emp_status = employee[2]

# checks if cloud engineer
if emp_dept == "Cloud Engineer":
    print("Cloud engineer profile detected, adding dev tools.")
    # adds dev tools
    access_groups = access_groups + ["aws", "github", "jira"]
# checks if cyber specialist
elif emp_dept == "Cyber Specialist":
    print("Cyber profile detected, adding networking tools.")
    # adds networking tools
    access_groups = access_groups + ["wireshark"]
else:
    print("Standard profile. No department tools added.")

# checks for cloud engineer contractor
if emp_status == "Contractor" and emp_dept == "Cloud Engineer":
    print("Security Alert: Contractor profile detected, adjusting permissions")
    # removes wiki access
    access_groups.remove("company_wiki")
    # adds vpn access
    access_groups.insert(0, "vpn_restricted")

# prints total groups
print(len(access_groups))
# sorts groups alphabetically
access_groups.sort()
# prints final groups
print(access_groups)
