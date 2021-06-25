beta = 0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee
beta2 = 0x851695d49a83f8ef919bb86153cbcb16630fb68aed0a766a3ec693d68e6afa40
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def one_to_6pubkey_1(upub_hex):
    if len(upub_hex) < 70 : print('Please provide full Uncompressed Pubkey in hex'); exit()
    x = int(upub_hex[2:66],16)
    y = int(upub_hex[66:],16)
    return '04'+hex(x)[2:].zfill(64)+hex(y)[2:].zfill(64)

def one_to_6pubkey_2(upub_hex):
    if len(upub_hex) < 70 : print('Please provide full Uncompressed Pubkey in hex'); exit()
    x = int(upub_hex[2:66],16)
    y = int(upub_hex[66:],16)
    return '04'+hex(x*beta%p)[2:].zfill(64)+hex(y)[2:].zfill(64)

def one_to_6pubkey_3(upub_hex):
    if len(upub_hex) < 70 : print('Please provide full Uncompressed Pubkey in hex'); exit()
    x = int(upub_hex[2:66],16)
    y = int(upub_hex[66:],16)
    return '04'+hex(x*beta2%p)[2:].zfill(64)+hex(y)[2:].zfill(64)

def one_to_6pubkey_4(upub_hex):
    if len(upub_hex) < 70 : print('Please provide full Uncompressed Pubkey in hex'); exit()
    x = int(upub_hex[2:66],16)
    y = int(upub_hex[66:],16)
    return '04'+hex(x)[2:].zfill(64)+hex(p-y)[2:].zfill(64)

def one_to_6pubkey_5(upub_hex):
    if len(upub_hex) < 70 : print('Please provide full Uncompressed Pubkey in hex'); exit()
    x = int(upub_hex[2:66],16)
    y = int(upub_hex[66:],16)
    return '04'+hex(x*beta%p)[2:].zfill(64)+hex(p-y)[2:].zfill(64)

def one_to_6pubkey_6(upub_hex):
    if len(upub_hex) < 70 : print('Please provide full Uncompressed Pubkey in hex'); exit()
    x = int(upub_hex[2:66],16)
    y = int(upub_hex[66:],16)
    return '04'+hex(x*beta2%p)[2:].zfill(64)+hex(p-y)[2:].zfill(64)

with open('test_db.txt','r',encoding='utf-8') as f:
    for line in f:
        with open('p_k_6.txt','a',encoding='utf-8') as f:
            f.writelines(f"Pubkey: {line.strip()}\n")
            f.writelines(f"Pubkey1: {one_to_6pubkey_1(line).strip()}\n")
            f.writelines(f"Pubkey2: {one_to_6pubkey_2(line).strip()}\n")
            f.writelines(f"Pubkey3: {one_to_6pubkey_3(line).strip()}\n")
            f.writelines(f"Pubkey4: {one_to_6pubkey_4(line).strip()}\n")
            f.writelines(f"Pubkey5: {one_to_6pubkey_5(line).strip()}\n")
            f.writelines(f"Pubkey6: {one_to_6pubkey_6(line).strip()}\n")
           