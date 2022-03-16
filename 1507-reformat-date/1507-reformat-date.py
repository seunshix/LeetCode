class Solution:
    def reformatDate(self, date: str) -> str:
        d = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        x = len(date)
        s = date[x-4:] + '-'
        if x == 13:
            s += d[date[5:8]] + '-' + date[0:2]
        else:
            s += d[date[4:7]] + '-' + '0' + date[0:1]
        return s