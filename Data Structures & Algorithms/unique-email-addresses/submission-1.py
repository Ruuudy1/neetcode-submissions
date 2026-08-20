class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        local_name, domain = '', ''
        for string in emails:
            local_name = string.split("@")[0]
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            domain = string.split("@")[1]
            result.append(local_name + domain)
        return len(set(result))
