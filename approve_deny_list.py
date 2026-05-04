import datetime

def main():

    url = input("Enter a URL to access: ")

    # read lists
    with open("approve.txt", "r") as file:
        approve_list = [line.strip() for line in file]

    with open("deny.txt", "r") as file:
        deny_list = [line.strip() for line in file]

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print()

    if url in approve_list:
        print("ACCESS GRANTED")
        print("--------------------------------------------------")
        print(f"       CONTENT FROM: {url}")
        print("--------------------------------------------------")
        print("This website has been verified as safe by your organization.")
        print("Feel free to browse this content for business or educational purposes.")
        print("Remember to follow the organization's acceptable use policy.")
        print("--------------------------------------------------")
        status = "APPROVE"

    elif url in deny_list:
        print("ACCESS DENIED")
        print("--------------------------------------------------")
        print(f"       BLOCKED URL: {url}")
        print("--------------------------------------------------")
        print("This website has been blocked by your organization's web filter.")
        print("Reason: This URL is on the deny list.")
        print("If you believe this is an error, please contact IT support.")
        print("--------------------------------------------------")
        status = "DENY"

    else:
        print("URL UNDER REVIEW")
        print("--------------------------------------------------")
        print(f"       PENDING REVIEW: {url}")
        print("--------------------------------------------------")
        print("This website is not on the approve or deny lists.")
        print("It has been submitted for review by the security team.")
        print("Access is currently restricted until review is complete.")
        print("Please check back later or contact IT if urgent access is needed.")
        print("--------------------------------------------------")
        print()
        print("URL has been added to review.txt for security team review.")
        status = "REVIEW"

        # append review URL
        with open("review.txt", "a") as file:
            file.write(url + "\n")

    # log every request
    with open("log.txt", "a") as file:
        file.write(f"{timestamp} - URL: {url} - STATUS: {status}\n")

    print()
    print("This access attempt has been logged to log.txt")

main()
