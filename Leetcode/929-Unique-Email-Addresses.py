class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        mails = set()

        for email in emails:
            local_name = email[:email.index("@")]
            domain = email[email.index("@"):]

            if "+" in local_name:
                first_plus = local_name.index("+")
                local_name = local_name[:first_plus]

            local_name = local_name.replace(".", "")
            mails.add(local_name + domain)

        return len(mails)
