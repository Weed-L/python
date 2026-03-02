def main():
    subject = input("Enter the email subject line: ")
    result = security_assessment(subject)
    
    print("\nSECURITY ASSESSMENT:")
    print(result)
    print("------------------------")
    print(f'Analyzed subject: "{subject}"')

def security_assessment(subject):
    subject_lower = subject.lower()

    if "urgent" in subject_lower or "immediate action required" in subject_lower:
        result = "HIGH RISK: Possible phishing attempt."
    elif "win" in subject_lower or "free" in subject_lower:
        result = "MEDIUM RISK: Suspicious offer detected."
    elif "password reset" in subject_lower:
        result = "LOW RISK: Verify legitimacy with sender."
    else:
        result = "No phishing indicators detected."

    return result

main()