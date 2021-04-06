#!/bin/bash
# this scripts needs to be run from the GIZA++ dir which contains data dir with files preprocessed with tokenize.py


./plain2snt.out ../data/en.data ../data/hindi.data
./snt2cooc.out ../data/en.data.vcb ../data/hindi.data.vcb ../data/en.data_hindi.data.snt > ../data/corp.cooc
./GIZA++ -S ../data/en.data.vcb -T ../data/hindi.data.vcb -C ../data/en.data_hindi.data.snt -CoocurrenceFile ../data/corp.cooc -outputpath ../data/

