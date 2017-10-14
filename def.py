def create_lat_lon_field():
	i_f = open('Dataset_z_863_94783_tweets.csv', 'r')
	id = []
	for line in i_f:
		cols = line.split(',')
		cols = [x.strip() for x in cols]
		if cols[4] in id:
			print line
		id.append(cols[4])
	print len(set(id))

if __name__ == '__main__':
	create_lat_lon_field()
