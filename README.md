# getar-solr-mini

hadoop fs -put Dataset_z_863_94783_tweets.csv

hbase shell

create 'getar-cs5604f17-solr-mini', 'tweet17' 

hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=, -Dimporttsv.columns="tweet17:archivesource,tweet17:text,tweet17:to_user_id,tweet17:from_user,HBASE_ROW_KEY,tweet17:from_user_id,tweet17:iso_language_code,tweet17:source,tweet17:profile_image_url,tweet17:geo_type,tweet17:geo_coordinates_0,tweet17:geo_coordinates_1,tweet17:time,tweet17:created_at"  getar-cs5604f17-solr-mini Dataset_z_863_94783_tweets.csv

rm -rf getar-cs5604f17-solr-mini-collection/

solrctl instancedir --delete getar-cs5604f17-solr-mini-collection

solrctl instancedir --generate $HOME/getar-cs5604f17-solr-mini-collection

UPLOAD schema file

solrctl instancedir --create getar-cs5604f17-solr-mini-collection $HOME/getar-cs5604f17-solr-mini-collection

solrctl collection --create getar-cs5604f17-solr-mini-collection

hadoop fs -mkdir /user/cloudera/getar_cs5604f17_solr_mini

COPY morphline.conf to /etc/hbase-solr/conf

ADD log4j.logger.org.kitesdk.morphline=TRACE to log4j.properties

LIVE INDEXING:
hadoop --config /etc/hadoop/conf jar /usr/lib/hbase-solr/tools/hbase-indexer-mr-*-job.jar --conf /etc/hbase/conf/hbase-site.xml -D 'mapred.child.java.opts=-Xmx500m' --hbase-indexer-file ./morphline-hbase-mapper.xml --zk-host 127.0.0.1/solr --collection getar-cs5604f17-solr-mini-collection --go-live --log4j ./log4j.properties

BATCH INDEXING:

sudo hadoop --config /etc/hadoop/conf jar /usr/lib/hbase-solr/tools/hbase-indexer-mr-*-job.jar --conf /etc/hbase/conf/hbase-site.xml -D 'mapred.child.java.opts=-Xmx3000m' --hbase-indexer-file ./morphline-hbase-mapper.xml --zk-host 127.0.0.1/solr --log4j ./log4j.properties --collection getar-cs5604f17-solr-mini-collection --verbose --output-dir hdfs://quickstart.cloudera/user/cloudera/getar_cs5604f17_solr_mini --overwrite-output-dir --shards 1

hadoop fs -get getar_cs5604f17_solr_mini/results/part-00000/data/index index

sudo -u hdfs hadoop fs -rm -r -skipTrash /solr/getar-cs5604f17-solr-mini-collection/core_node1/data/index

sudo -u hdfs hadoop fs -rm -r -skipTrash /solr/getar-cs5604f17-solr-mini-collection/core_node1/data/tlog

sudo -u solr hadoop fs -put index /solr/getar-cs5604f17-solr-mini-collection/core_node1/data/index

sudo service solr-server restart
