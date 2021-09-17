def scanner(name, function):
    file = open(name, 'r')      # create file object
    while True:
        line = file.readline()
        if not line: break
        function(line)
    file.close()