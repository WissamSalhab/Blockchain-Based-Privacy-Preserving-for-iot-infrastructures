# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:03:20 2021

@author: Hajer 
"""

from phe import paillier
import numpy as np



public_key, private_key = paillier.generate_paillier_keypair()
secret_number_list = [1, 2, 3]
secret_number_list2 = [1, 2, 6]
dif=np.linalg.norm(np.array(secret_number_list)-np.array(secret_number_list2))

encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]
encrypted_number_list2 = [public_key.encrypt(x) for x in secret_number_list2]

encrypteddif=[]
for i in range(len(encrypted_number_list2)):
    encrypteddif.append(encrypted_number_list[i]-encrypted_number_list2[i])
    
decrdif=[private_key.decrypt(x) for x in encrypteddif]

print(np.linalg.norm(np.array(decrdif)),dif)


