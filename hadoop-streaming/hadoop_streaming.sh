export HADOOP_STREAMING_JAR=/usr/lib/hadoop-mapreduce/hadoop-streaming.jar 
hadoop jar $HADOOP_STREAMING_JAR -input "input-file.txt" -output "mr-streaming-$(date '+%s')" -mapper "$(pwd)/mapper" -reducer "$(pwd)/reducer"

