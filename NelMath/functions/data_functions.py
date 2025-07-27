__all__=["str_to_bits","bits_to_str", "convert"]
def str_to_bits(data:str):
    bytes_data = data.encode('utf-8') 
    bits = ''.join(format(byte, '08b') for byte in bytes_data)
    return bits

def bits_to_str(bits: str) -> str:
    byte_strings = [bits[i:i+8] for i in range(0, len(bits), 8)]
    bytes_data = bytes(int(byte_str, 2) for byte_str in byte_strings)
    return bytes_data.decode('utf-8', errors='replace')

def convert(data, to_t:type, view:type=None):
    if type(data)==str:        
        try:
            float(data)
            numeric = True
        except ValueError:
            numeric = False
        match(to_t):
            case str():
                if type(view)==str:
                    return bits_to_str(data)
                else:
                    return data
            case list():
                if view==list:
                    return [k for k in list(data)]
                else:
                    return list(data)
            case int():
                if numeric:
                    if view==list():
                        return [int(k) for k in list(data)]
                    else:
                        return int(data)
                else:
                    raise ValueError('String is not numeric to convert')
            case bin:
                if view==list():
                    return [int(k) for k in list(str_to_bits(data))]
                else:
                    return str_to_bits(data)
    if type(data)==list:
        match(to_t):
            case str():                
                if view==list():
                    res = [str(k) for k in data]
                else:
                    res = ''.join(str(k) for k in data)                
                if type(view)==str:
                    return bits_to_str(res)
                else:
                    return res
            case list():
                return data
            case int():
                if view==list():
                    return [int(k) for k in list(data)]
                else:
                    return int(''.join([str(k) for k in data]))
            case bin:
                if view==list():
                    return [int(k) for k in list(str_to_bits(data))]
                else:
                    return str_to_bits(data)
    else:
        return convert(data, to_t, view)

