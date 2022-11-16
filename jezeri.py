from sys import argv
from subprocess import run as sh
print(f"JEZERI v1 (c) Leander Francis Westren Johns 2022")
print(f"------------------------------------------------")
def main():
	print(f"Opening <{argv[1]}>...")
	try:f=open(argv[1])
	except:
		print(f"FATAL: Cannot find file <{argv[1]}>.")
		quit()
	c=0
	p="out"
	o=["#!/usr/bin/env python3"]
	d=0
	dent=""
	l=1
	print(f"Parsing <{f.name}>...")
	for line in f:
		dent=""
		line=line.replace("\n","").replace("    ","\t").replace("\t","")
		if line.startswith("{:"):
			c=1
			if line.endswith(":}"):
				c=0
		elif line.endswith(":}"):
			c=0
		elif line.startswith("program "):
			p=line.replace("program ","",1)
		elif line.startswith("start "):
			d+=1
			o.append(f'def {line.replace("start ","",1)}:')
		elif line.startswith("print "):
			for i in range(d):dent+="\t"
			o.append(f'{dent}print(f{line.replace("print ","",1)})')
		elif line.startswith("declare "):
			for i in range(d):dent+="\t"
			o.append(f'{dent}{line.replace("declare ","",1)}')
		elif line.startswith("call "):
			for i in range(d):dent+="\t"
			o.append(f'{dent}{line.replace("call ","",1)}')
		elif line.startswith("if "):
			for i in range(d):dent+="\t"
			o.append(f'{dent}{line}')
		elif line.startswith("if otherwise "):
			for i in range(d):dent+="\t"
			o.append(f'{dent}elif {line.replace("if otherwise ","",1)}:')
		elif line=="otherwise":
			for i in range(d):dent+="\t"
			o.append(f'{dent}else:')
		elif line.startswith("for "):
			for i in range(d):dent+="\t"
			o.append(f'{line}')
		elif line=="continue":
			for i in range(d):dent+="\t"
			o.append(f'pass')
		elif line=="halt":
			for i in range(d):dent+="\t"
			o.append(f'quit()')
		elif line.startswith("use"):
			o.append(f'{line.replace("use ","import ")}')
		elif line=="finish":
			d-=1
		else:
			print(f"FATAL: Line {str(l)} in <{f.name}>\n  {line}\nSyntax: Unidentified token ({line.split()[0]}).")
			quit()
		l+=1
	o.append("main()")
	of=open(f"{p}","w")
	print(f"Writing to <{of.name}>...")
	for item in o:
		of.write(f"{item}\n")
	print(f"Running chmod on <{of.name}>...")
	sh(f"chmod +x {of.name}",shell=True)
	print(f"Compiled <{f.name}> succesfully!\nRun ./{of.name} to execute your program.")
	f.close()
	of.close()
if len(argv[1])==0:quit()
else:main()
