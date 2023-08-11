def coding_str(string,size):
    return string.encode('utf-8')[:size].ljust(size, b'\0')