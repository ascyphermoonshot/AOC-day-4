import csv
import re
def check_sectors(elfpair):
	def get_sectors(elf):
		firstnum=re.search(r'\d+(?=\-)',elf)
		finnum=re.search(r'(?<=\-)\d+',elf)
		return (int(firstnum.group()),int(finnum.group()))
	elf1,elf2=elfpair
	start1,end1=get_sectors(elf1)
	start2,end2=get_sectors(elf2)
	elf1_sectors={sector for sector in range(start1,end1)}
	elf2_sectors={sector for sector in range(start2,end2)}
	return elf1_sectors.issubset(elf2_sectors)or elf2_sectors.issubset(elf1_sectors)

with open("/storage/emulated/0/Download/input (3).txt",newline='') as f:
    reader=csv.reader(f)
    taskpairs=[tuple(elfpair) for elfpair in reader]
overlaps=[]
for elfpair in taskpairs:
	overlaps.append(check_sectors(elfpair))
print('\n',overlaps.count(True))