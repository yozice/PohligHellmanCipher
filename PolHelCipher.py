import secrets
from labmath import xgcd
import re

def enc(m, e, p):
    return pow(m, e, p)

def dec(c, d, p):
    return pow(c, d, p)

def keygen(p):
    while True:
        e = secrets.randbelow(p)
        gcd, x, y = xgcd(e, p-1)
        if gcd != 1: continue
        d = x % (p-1)
        break
    return e, d

def main():
	try:
	    with open('Message.txt', 'r') as fr:
	    	s1 = fr.read().encode()
	    #fr = open('Message.txt', 'r+')
	    #s1 = fr.read().encode()
	    #fr.close()
	    m = int.from_bytes(s1, 'big')
		#m = int(''.join(str(ord(c)) for c in s1))
	    #print(m)
	    #safe prime from RFC 7919 (ffdhe2048)
	    p = 0xFFFFFFFFFFFFFFFFADF85458A2BB4A9AAFDC5620273D3CF1D8B9C583CE2D3695A9E13641146433FBCC939DCE249B3EF97D2FE363630C75D8F681B202AEC4617AD3DF1ED5D5FD65612433F51F5F066ED0856365553DED1AF3B557135E7F57C935984F0C70E0E68B77E2A689DAF3EFE8721DF158A136ADE73530ACCA4F483A797ABC0AB182B324FB61D108A94BB2C8E3FBB96ADAB760D7F4681D4F42A3DE394DF4AE56EDE76372BB190B07A7C8EE0A6D709E02FCE1CDF7E2ECC03404CD28342F619172FE9CE98583FF8E4F1232EEF28183C3FE3B1B4C6FAD733BB5FCBC2EC22005C58EF1837D1683B2C6F34A26C1B2EFFA886B4238611FCFDCDE355B3B6519035BBC34F4DEF99C023861B46FC9D6E6C9077AD91D2691F7F7EE598CB0FAC186D91CAEFE130985139270B4130C93BC437944F4FD4452E2D74DD364F2E21E71F54BFF5CAE82AB9C9DF69EE86D2BC522363A0DABC521979B0DEADA1DBF9A42D5C4484E0ABCD06BFA53DDEF3C1B20EE3FD59D7C25E41D2B66C62E37FFFFFFFFFFFFFFFF

	    e, d = keygen(p)
	    c = enc(m, e, p)

	    assert m == dec(c, d, p)

	    s2 = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
	    #items = re.findall(r'.{3}', str(m))
	    #s2 = ''.join(str(chr(int(c))) for c in items)
	    #print(s2)
	    fw = open('CryptedMessage.txt', 'w')
	    fw.write(str(c) + '\n')
	    fw.close()

	    fw = open('DecryptedMessage.txt', 'w')
	    fw.write(s2 + '\n')
	    fw.close()

	    fw = open('Parameters.txt', 'w')
	    fw.write("Ключи:\n" + 
	    	"e = " + str(e) + '\n' +
	    	"d = " + str(d) + '\n' +
	    	"Простое число p = " + str(p))
	    fw.close()
	    print("Шифрование прошло успешно!")
	except IOError:
		with open('Message.txt', 'w') as fr:
			print("Нет входного сообщения для шифрования!\nПожалуйста введите его в файл Message.txt!")


if __name__ == '__main__':
    main()