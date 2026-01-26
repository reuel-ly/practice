def int32_to_ip(int32):
    
    octet_1 = int32 // 2 ** 24
    int32 = int32 - (octet_1 * (2**24))
    
    octet_2 = int32 // 2 ** 16
    int32 = int32 - (octet_2 * (2**16))
    
    octet_3 = int32 // 2 ** 8
    
    octet_4 = int32 - (octet_3 * (2**8))
    
    return f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"