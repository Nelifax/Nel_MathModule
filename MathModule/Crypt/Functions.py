__all__ = ['encode', 'decode']

def encode(stroke_to_encode:any)->int:
    '''
    ������� ������ � �����
    '''
    byteStroke = bytes(stroke_to_encode, 'utf-8')
    hexStroke = byteStroke.hex()
    return str(int(hexStroke, 16))

def decode(number_to_decode:int)->str:
    '''
    ������� ����� � �����
    '''
    hexString = hex(number_to_decode)
    byteStroke = bytes.fromhex(hexString[2:])
    decodedStroke = byteStroke.decode('utf-8')
    return decodedStroke