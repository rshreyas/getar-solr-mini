import pandas as pd

def create_lat_lon_field():
	i_f = open('Dataset_z_863_94783_tweets.csv', 'r')
	#o_f = open('Dataset_z_46_5736178_tweets_mod.csv', 'w')
	temp = []
	df = pd.DataFrame([])
	
	for line in i_f:
		cols = line.split(',')
		cols = [x.strip() for x in cols]
		col_a = cols[10]
		col_b = cols[11]
		if not (col_a or col_b):
			col_a = '0.0'
			col_b = '0.0'
		cols.append(col_a+','+col_b)
		temp.append(cols)
	df = df.append(temp)
	df.to_csv(path_or_buf = 'Dataset_z_863_94783_tweets_mod.csv', sep = '\t', index = False, header = False)

if __name__ == '__main__':
	create_lat_lon_field()
