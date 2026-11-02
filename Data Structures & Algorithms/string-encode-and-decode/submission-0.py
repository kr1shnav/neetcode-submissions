class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += f"{len(s)}#{s}"
        return en

    def decode(self, s: str) -> List[str]:
        de = []
        fst = 0
        while fst < len(s):
            i = s.find("#", fst)
            strlen = int(s[fst:i])
            de.append(s[i + 1 : i + 1 + strlen])
            fst = i + 1 + strlen
        return de
