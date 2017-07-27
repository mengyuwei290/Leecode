class Solution(object):
    def validIPAddress(self, IP):
        num = set('0123456789abcdefABCDEF')
        if len(IP.split('.')) == 4:
            s = IP.split('.')
            for i in s:
                if not i.isdigit() or int(i) > 255 or (len(i) > 1 and i[0] == '0'):
                    return 'Neither'
            return 'IPv4'
        elif len(IP.split(':')) == 8:
            s = IP.split(':')
            for i in s:
                if len(i) == 0 or len(i) > 4 or not set(i) <= num:
                    return 'Neither'
            return 'IPv6'
        else: return 'Neither'
