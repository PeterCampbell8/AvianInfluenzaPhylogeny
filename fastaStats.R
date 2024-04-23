#fastaStats
#install.packages('seqinr')
library(stringr)
setwd('C:/Users/p953c068/Documents/InfluenzaPIPP/GenBankSurvey/full_data')
library(seqinr)

#read in the fasta file
fasta <- read.fasta("./pb1/pb1Nucleotides.fasta",seqtype = "DNA") #change to target protein's folder
#create a new vector of the lengths of the sequences
lengths <- sapply(fasta, length)

#middle 80% quantile, cut-off for top 80% quantile, and make a list of the top 80% quantile
quant80 <-quantile(lengths,c(.1,.9))
quantBot20 <- quantile(lengths,.2)
top80 <- subset(lengths, lengths >= quantBot20)

#Create a histogram with some of the statistics
hist_vect <- hist(lengths, breaks = 100)
abline(v = range(lengths), col = "blue")
abline(v = quant80, col = "red")
abline(v = quantBot20, col = "purple")
abline(v = median(lengths), col = "orange")
abline(v = mean(lengths), col = "green")
abline(v = 1780, col = "gold")


#intre <- same(fasta['Name'],top80['Name'])

#Identify gappy breakpoints
ambig <- read.csv("./pb1/pb1AlignedGuide2.clean.csv", header=FALSE)
foo <- function(x) as.numeric(str_sub(x,0,-2))
perCent <- sapply(ambig$V3, foo)
breaks <- seq(-.005, .04, by=.005)
hist(perCent, breaks, plot = FALSE)
perCent.cut <- cut(perCent, breaks, right=FALSE, include.lowest = TRUE)
perCent.freq <- table(perCent.cut)
perCent.cumfreq <- cumsum(perCent.freq)
perCent.cumrelfreq <- perCent.cumfreq / nrow(ambig)

plot(breaks, c(0, perCent.cumrelfreq), xlab="ambiguity", ylab="cumulative percent of sequences")
hist(perCent, breaks = 100)
cumsum(perCent)
plot()

     