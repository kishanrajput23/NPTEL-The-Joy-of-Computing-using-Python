def findLongestPalindrome(s):
	count = [0]*256
	for i in range(len(s)):
		count[ord(s[i])] += 1
	beg = ""
	mid = ""
	end = ""
	ch = ord('a')
	while ch <= ord('z'):
		if (count[ch] & 1):
			mid = ch
			count[ch] -= 1
			ch -= 1
		else:
			for i in range(count[ch]//2):
				beg += chr(ch)
		ch += 1
	end = beg
	end = end[::-1]
	return beg + chr(mid) + end
  
n=int(input())
nums = []

for i in range(n):
      nums.append(len(findLongestPalindrome(input())))
for j in nums:
      print(j)
