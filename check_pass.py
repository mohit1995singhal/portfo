import requests
import hashlib
import sys


def request_api_data(quarry_char):
    url = 'https://api.pwnedpasswords.com/range/' + quarry_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching {res.status_code} unsupported api data please check your password')
    return res

def get_pass_leak_count(all_hashes,hash_to_check):
	all_hashes=(line.split(':') for line in all_hashes.text.splitlines())
	for h,count in all_hashes:
		if h==hash_to_check:
			return count
	return 0


def pawned_api_check(password):
    hash_pass =hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_char,tail=hash_pass[:5],hash_pass[5:]
    response=request_api_data(first_5_char)
    return get_pass_leak_count(response,tail)


def main(args):
	for password in args:
		count=pawned_api_check(password)
		if count:
			 print(f'{password} found {count} many times you should probabily change it')
		else:
			print(f'{password} was NotFound {count} you can go with this password')
		return "done!"
   
   

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))






