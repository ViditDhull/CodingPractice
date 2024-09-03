class Solution:
    def reformatDate(self, date: str) -> str:
        md = {
            'Jan': '01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'
        }
        result = ''
        dl = date.split()
        result += dl[2]
        result += '-'
        result += md[dl[1]]
        result += '-'
        if len(dl[0]) == 3:
            result += '0'
        result += dl[0][:-2]

        return result
