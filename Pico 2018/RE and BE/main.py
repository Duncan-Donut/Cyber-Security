goal = "You have now entered the Duck Web and you re in for a honkin good time. Can you figure out my trick" #99

offset = [0x29,0x6,0x16,0x4f,0x2b,0x35,0x30,0x1e,0x51,0x1b,0x5b,0x14,0x4b,0x8,0x5d,0x2b,0x50,0x14,0x5d,0x0,0x19,0x17,0x59,0x52,0x5d,0x0,0x4e,0x6f,0x20,0x6c,0x69,0x6e,0x65,0x20,0x72,0x65,0x61,0x64,0x2e,0x2e,0x2e,0x0,0x0,0x0,0x6d,0x61,0x6c,0x6c,0x6f,0x63,0x28,0x29,0x20,0x72,0x65,0x74,0x75,0x72,0x6e,0x65,0x64,0x20,0x4e,0x55,0x4c,0x4c,0x2e,0x20,0x4f,0x75,0x74,0x20,0x6f,0x66]

answer = ""

print(len(goal))
print(len(offset))

for x in range(len(offset)):
	answer += chr(offset[x] ^ ord(goal[x]))


print(answer)



