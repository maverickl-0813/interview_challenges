"""
A coding problem from N******e coding interview.
The original requirement only asked to implement a simple encrypting mechanism. This code file extends the context.

Encrypt A-Z and a-z into traceable hashes.
The hash length will be 4 and combined with a-z letters and not duplicated.
It's only traceable when the instance is alive.
Each instance will have its own combination of hash.

"""
import random
import string


class StringEncryptor:

    def __init__(self):
        self.letter_hashmap = {x: "" for x in string.ascii_letters}
        self.hashmap_letters = dict()
        self.hash_length = 4
        self._create_hash()

    def _create_hash(self):
        for letter, hashkey in self.letter_hashmap.items():
            if not hashkey:
                hashkey = ''.join(random.choices(string.ascii_lowercase, k=self.hash_length))
                self.letter_hashmap[letter] = hashkey
                # No duplicate "hashkey" check on  for the moment...

        # reverse the hashmap for decryption.
        self.hashmap_letters = {hashkey: letter for letter, hashkey in self.letter_hashmap.items()}

    def get_hashmap(self):
        return self.letter_hashmap

    def encrypt_string(self, input_str):
        encrypted_string = ""
        for c in input_str:
            if c in string.ascii_letters:
                encrypted_string += self.letter_hashmap.get(c)
            else:
                encrypted_string += c
        return encrypted_string

    def decrypt_string(self, input_str):
        decrypted_string = ""
        idx = 0
        while idx < len(input_str):
            if input_str[idx] not in string.ascii_lowercase:
                decrypted_string += input_str[idx]
                idx += 1
            else:
                found = False
                for length in range(1, self.hash_length + 1):
                    partial_str = input_str[idx:idx + length]
                    if partial_str in self.hashmap_letters:
                        decrypted_string += self.hashmap_letters.get(partial_str)
                        idx += length
                        found = True
                        break
                if not found:
                    print(f"cannot recognize the encrypted string! {input_str[idx]}")
                    break
        return decrypted_string


if __name__ == "__main__":
    # str = "Hi! This is Maverick!"
    # str = "abc123def"
    # str = "a"
    # str = "abc"
    # str = "!@#$%^"
    # str = ""
    # str = "sagittis, pretium neque in, vestibulum eros. Etiam sed sodales orci. Quisque pretium risus nibh,
    #        sed hendrerit urna convallis ut. Cras eu tellus sed odio venenatis cursus a ut ipsum. Pellentesque nec
    #        velit erat. Nulla eget diam sit amet ipsum posuere biben"

    encryptor = StringEncryptor()
    print(encryptor.get_hashmap())
    encrypted_str = encryptor.encrypt_string(str)
    print(f"{encrypted_str = }")
    decrypted_str = encryptor.decrypt_string(encrypted_str)
    assert decrypted_str == str
    print(f"{decrypted_str = }")
