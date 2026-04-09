class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for e in emails:
            local, domain = e.split("@")
            newLocal = ""
            for l in local:
                if l == ".":
                    continue
                elif l == "+":
                    break
                else:
                    newLocal += l
            email = [newLocal, domain]
            if email not in res:
                res.append(email)
        return len(res)