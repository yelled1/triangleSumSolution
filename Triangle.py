"""By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

        5
      9  6
    4   6  8
  0   7  1   5
I.e. 5 + 9 + 6 + 7 = 27."""

with open('./triangle_o.txt', 'r') as f: lines = filter(lambda x: x != '', f.read().split('\n'))
maxi = [int(lines[0])]
idxl = [0]
idx  = 0
sums = int(lines[0])
for ln in lines[1:]:
    lln = ln.strip().split(' ')
    if int(lln[idx]) > int(lln[idx+1]): idx = idx
    elif int(lln[idx]) == int(lln[idx+1]): 
        print "if Eq encountered then this should b forked"
        idx = idx
    else:                               idx = idx+1
    maxi.append(int(lln[idx])) 
    idxl.append(idx)
    sums = sums + int(lln[idx])
print maxi
print sum(maxi), sums

