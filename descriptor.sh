#!/bin/bash
#STARTTIME=$((date +%s))


# python rename.py

mkdir descriptors
mkdir regionFiles


iter=1

SRC_DIR=database/light_fruits
REG_DIR=regionFiles
DEST_DIR=descriptors
		
cd ${SRC_DIR}
n=`ls *.pgm* | wc -l`
echo $n
cd ../..
pwd
while [ $iter -le $n ];
do
	echo $iter
	./detect_points.ln -haraff -i ${SRC_DIR}/img${iter}.pgm -o ${REG_DIR}/img${iter}.haraff -thres 1000
	# ./mser.ln -i ${SRC_DIR}/img${iter}.jpg -o ${REG_DIR}/img${iter}.haraff
	./LIOPEx -img ${SRC_DIR}/img${iter}.pgm -region ${REG_DIR}/img${iter}.haraff -des ${DEST_DIR}/img${iter}.txt
	iter=$((iter + 1))
done
cp -i score.py ${DEST_DIR}/score.py
cd ${DEST_DIR}
python score.py

#ENDTIME=$((date +%s))
#echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..."
