import re

r = re.compile(r'\d+\.?\d*')

print(bool(r.match('1.1')))
print(bool(r.match('1')))
print(bool(r.match('a')))
print(bool(r.match('')))

r2 = re.compile(r'abc-([a-z]{3})')
m = r2.findall("abc-xyz-some text")
print(m)
print(r2.sub("some", "abc-xyz"))

print(re.findall(r'abc-([a-z]{3})', "abc-xyz-some text"))

def validate_ip(s):
	if re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s):
		return all(int(x) < 256 for x in s.split('.'))
	return False

print(validate_ip('192.168.1.1'))
print(validate_ip('192.168.1'))
print(validate_ip('a.b.c.d'))

print(validate_ip('255.255.255.255'))
print(validate_ip('280.255.255.255'))