import csv
from geopy import distance

def create_distances():
    hm = {}
    def distances(a,b):
        #return distance.distance(hm[a], hm[b]).km
        return distance.great_circle(hm[a], hm[b]).km # this is 20x faster for only slightly more error

    with open("us-county-boundaries.csv", 'r') as f:
        first = True
        f.readline() # gets rid of header
        for i in f:
            row = i.split(";")
            hm[row[5]] = row[0]
    hm2 = {}
    counties = sorted(hm.keys())
    for i in range(len(counties)):
        for j in range(i+1, len(counties)):
            hm2[f'{counties[i]},{counties[j]}'] = distances(counties[i], counties[j])

    with open("counties_distance2.csv", 'w') as f:
        f.write('county1,county2,distance\n')
        for i in hm2:
            f.write(i + ',' + str(round(hm2[i], 5))+'\n')

        
def parse_govt_data():
    overall_array = []
    def parse_row(row):
        co1 = row[0] + row[1]
        co2 = (row[6] + row[7])[-5:]
        if len(co2) < 5: return
        amount = int(row[-2].replace(',',''))
        overall_array.append((co1, co2, amount))
    with open("table3.csv") as f:
        g = csv.reader(f)
        for n,row in enumerate(g):
            if not n: continue
            parse_row(row)

    return overall_array


def merge():
    j = parse_govt_data()
    hm = {}
    with open("counties_distance.csv") as f:
        for n,i in enumerate(f):
            if not n: continue
            g = i.split(',')
            hm[tuple(g[:2])] = g[2]
    with open("edge_data2.csv", 'w') as f:
        f.write("county1,county2,wicf,distance\n")
        for i in j:
            if i[0] == i[1]: continue
            dist = hm.get(tuple(i[:2])) or hm.get(tuple(i[:2][::-1]))
            f.write(f"{i[0]},{i[1]},{i[2]},{dist}")
    
merge()
            
        
