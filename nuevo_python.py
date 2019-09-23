ipAddress = input("Please enter an IP address: ")
if ipAddress[-1] != '.':
    ipAddress += '.'
ipAddress += '.'
segment = 1
segment_lenght = 0 
#scharacter = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_lenght))
        segment += 1 
        segment_lenght = 0 
    else:
        segment_lenght += 1 
#unless the final character in the string was a . hen we haven't printed the last segment
#if character != '.':
#    print("segment {} contains {} characters".format(segment, segment_lenght))