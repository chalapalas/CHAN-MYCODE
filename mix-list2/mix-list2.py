#!/usr/bin/env python3
#proto = ['ssh', 'http', 'https']
#.print(proto)
#print(proto[1])
#protoa = ['ssh','http','https']
#proto.extend('dns') # this line will add 'd' amd 's; to the end of our list
#print(proto)
#proto.append('dna') # this line will add 'dns' to the end of our list
#protoa.append('dna') # this line willa add 'dna' to the end of our list
#print(proto)
#proto2 = [ 22, 80, 443, 53 ] # a list of commmon ports
#proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print
#print(proto)
#protoa.append(proto2) # pass proto2 as an argument to the append method -- then print
#print (protoa)
#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protoa)
