import json

def encode_complex(object):
    # check using isinstance method
    if isinstance(object, complex):
        return [object.real, object.imag]
    # raised error if object is not complex
    raise TypeError(repr(object) + " is not JSON serialized")

complex_obj = json.dumps(2j + 3, default=encode_complex)
print(complex_obj)