class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        local_name = ""
        domain = ''
        for string in emails:
            local_name = string.split("+")[0]
            domain = string.split("@")[1]
            local_name = local_name.replace(".", "")
            local_name += domain
            result.append(local_name)
            print(result)
        return len(set(result))
