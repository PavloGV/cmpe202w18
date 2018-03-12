#!/bin/bash
# CMPE202 Winter 2018 Project 
# Pavlo Vlastos
#
# How to use:
# 	- 	Initially running 'run.sh' will execute both the throughput and latency benchmarks
#		with all threads all input sizes, etc... This can take a long time.
sudo sh -c 'echo -1 >/proc/sys/kernel/perf_event_paranoid'
sudo sh -c 'echo 0 >/proc/sys/kernel/nmi_watchdog'
echo '================ executing run.sh =================='
declare -a divType=(256 64 16 4 1) 		# **** Corresponds inputSizes order *****
declare -a measName=(IPC BranchMPKI LoneMPKI LLC)
declare -a threadNum=(1 2 4 8)
declare -i instCountNum
instCountNum=100
index=0
inputSizes=(200 1350 5750 24000 93000) # **** Corresponds divType order *****

## THROUGHPUT
echo 'Beginning Throughput benchmark measurements '
for m in "${measName[@]}" # for every measurement type
do
	for t in "${threadNum[@]}" # for every number of threads
	do
		for d in "${divType[@]}" # for every division type, example: x/256, x/64, ...
		do 
			echo '-------------------------------------------------------------------'
			echo 'Thread number: '$t', inputSize: '${inputSizes[index]}', divType: '$d', measure: '$m
			echo 'pwd'
			echo pwd
			sudo python cmpe202w2018/project/filterpy/filterpy/kalman/tests/noisy_sine.py -l ${inputSizes[index]} -t $t
			sudo perf stat -I $instCountNum -e cpu-cycles,instructions,branch-instructions,branch-misses,L1-dcache-load,LLC-loads -x, -o intermediate.csv python cmpe202w2018/project/filterpy/filterpy/kalman/tests/read_signal.py; python cmpe202w2018/project/filterpy/filterpy/kalman/tests/../../../../../pmu-tools/interval-normalize.py intermediate.csv > normOut.csv
			sudo python cmpe202w2018/project/filterpy/filterpy/kalman/tests/plotMyData.py -f normOut.csv -d $d -m $m -t $t
			index=$(( $index + 1 ))	
		done
		index=0
	done
done

### LATENCY 
# - measure response time for GUI (open and closing sine wave graphs)
# - report distribution and average
# - measure time to start/stop gui app
# - 

echo 'Throughput benchmark measurements completed'
echo '---------------------------------'
echo 'Beginning Latnecy benchmark measurements '

# run noisey_sine.py
# run and measure the start/stop time of read_sine.py 100 times
# get_run_time takes in the csv file, file number, and outputs txt files time1.txt, time2.txt, ... time100.txt
# python noisy_sine.py -l 1350 -t 1
python noisy_sine.py -l 200 -t 1
while [ $index -lt $instCountNum ]
do
	sudo perf stat -I 100 -e cycles -x, -o intermediate.csv python cmpe202w2018/project/filterpy/filterpy/kalman/tests/read_signal.py; python cmpe202w2018/project/filterpy/filterpy/kalman/tests/../../../../../pmu-tools/interval-normalize.py intermediate.csv > normOut.csv
	sudo python cmpe202w2018/project/filterpy/filterpy/kalman/tests/get_run_time.py -f normOut.csv -n $index
	echo 'run: '$index
	index=$(( $index + 1 ))
done
sudo python cmpe202w2018/project/filterpy/filterpy/kalman/tests/plotLatency.py
echo 'Latency benchmark measurements completed'

### last things to do
# make single script with docker for setup.sh
# make single script with docker for run.sh
# make slides
# report?

