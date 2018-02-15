set -ev

git clone https://github.com/wdecoster/nanotest.git

NanoFilt -h

NanoStat --fastq nanotest/reads.fastq.gz --prefix tester
NanoStat --bam nanotest/alignment.bam -o outdir
NanoStat --summary nanotest/sequencing_summary.txt -n testerfile
NanoStat --fasta nanotest/reads.fa.gz
