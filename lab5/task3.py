encrypted_message = 4233037422
e = 97
n = 4378657993
print((123 ** e) % n)

def compare_encrypted_message(res_encription):
    return 4233037422 == res_encription

def receiving_message(encrypted_message, e, n):
    enc_res = (encrypted_message ** e) % n
    while not compare_encrypted_message(enc_res):
        prev_enc = enc_res
        enc_res = (enc_res ** e) % n
    print(prev_enc)

receiving_message(encrypted_message, e, n)