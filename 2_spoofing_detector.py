import dns.resolver
import email
import re

def check_email_spoofing(file_path):
    with open(file_path, 'r') as file:
        raw_email = file.read()

    # Parse the raw email
    msg = email.message_from_string(raw_email)

    # Extract the From and Return-Path headers
    from_header = msg.get("From")
    return_path_header = msg.get("Return-Path")

    # Extract the domain from the Return-Path header
    if return_path_header:
        match = re.search(r'@(.+)>', return_path_header)
        if match:
            return_path_domain = match.group(1)
        else:
            return_path_domain = None
    else:
        return_path_domain = None

    # Check SPF record
    if return_path_domain:
        try:
            spf_record = dns.resolver.resolve(return_path_domain, 'TXT')
            for txt_record in spf_record:
                if "v=spf1" in txt_record.to_text():
                    spf_pass = True
                    break
            else:
                spf_pass = False
        except:
            spf_pass = False
    else:
        spf_pass = False

    # Check DKIM signature
    dkim_signature = msg.get("DKIM-Signature")
    if dkim_signature:
        dkim_pass = True
    else:
        dkim_pass = False

    # Determine if the email is spoofed
    if spf_pass and dkim_pass:
        return "Email is not spoofed"
    else:
        return "Email appears to be spoofed"


def main():
    eml_file_path = input("Please provide the email.eml file path: ")
    result = check_email_spoofing(eml_file_path)
    print(result)
    

if __name__ == "__main__":
    main()
    
