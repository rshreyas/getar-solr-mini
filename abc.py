def create_lat_lon_field():
	i_f = open('Dataset_z_46_5736178_tweets.csv', 'r')
	o_f = open('Dataset_z_46_5736178_tweets_mod.csv', 'w')
	for line in i_f:
		cols = line.split(',')
		cols = [x.strip() for x in cols]
		col_a = cols[10]
		col_b = cols[11]
		new_line = ''
		for i in cols:
			if not new_line:
				new_line = i
			else:
				new_line = new_line + '	' + i
		if not (col_a or col_b):
			col_a = '0.0'
			col_b = '0.0'
		new_line = new_line + '	' + col_a+','+col_b
		o_f.write(new_line+'\n')

if __name__ == '__main__':
	create_lat_lon_field()
