setwd("C:\\Users\\mekline\\Documents\\My Dropbox\\_Projects\\Clan2R")
source("CLANtoR.R")
library(gsubfn)
library(stringr)

paths <- c("Brown/Brown/Adam", "Brown/Brown/Sarah", "Brown/Brown/Eve")
filenames <- c()
for (p in paths){
	f <- list.files(path=p, pattern="*.cha")
	f <- mapply(paste, p, f, sep="/")
	filenames <- append(filenames, f)
}

d <- sapply(filenames, read.CLAN.file)
mydata <- rbind.fill(d)
orig.length <-nrow(mydata)
origdata <- mydata

###################################################

mydata$mor <- as.character(mydata$mor)

mydata_orig <- mydata

#Do some more cleaning up of mor and Gloss line!   

mysub <- function(pat, rep, str){
	sub(pat, rep, str, fixed=TRUE)
}

mydata$CleanMor <- mapply(mysub,"\t", " ", mydata$mor)
mydata$CleanMor <- mapply(mysub,"\n", " ", mydata$CleanMor)
mydata$CleanMor <- mapply(mysub,".", "", mydata$CleanMor)
mydata$CleanMor <- mapply(mysub,"?", "", mydata$CleanMor)
mydata$CleanMor <- mapply(mysub,",", "", mydata$CleanMor)
mydata$CleanMor <- mapply(mysub,"  ", " ", mydata$CleanMor)
mydata$CleanMor <- mapply(str_trim, mydata$CleanMor)


mydata$CleanGloss <- mapply(mysub, "\" ", "", mydata$Gloss)
mydata$CleanGloss <- mapply(mysub, "+", "", mydata$CleanGloss)
mydata$CleanGloss <- mapply(mysub,".", "", mydata$CleanGloss)
mydata$CleanGloss <- mapply(mysub,"?", "", mydata$CleanGloss)
mydata$CleanGloss <- mapply(mysub,",", "", mydata$CleanGloss)
mydata$CleanGloss <- mapply(mysub,"  ", " ", mydata$CleanGloss)
mydata$CleanGloss <- mapply(str_trim, mydata$CleanGloss)


#Check whether Gloss and Mor lengths match!
morsplits <- mapply(strsplit, as.character(mydata$CleanMor), " ")
glosplits <- mapply(strsplit, as.character(mydata$CleanGloss), " ")
mydata$Length.Mor <- unlist(lapply(morsplits, length))
mydata$Length.Gloss <- unlist(lapply(glosplits, length))
mydata$Length.Match <- mydata$Length.Mor == mydata$Length.Gloss

write.table(mydata, file="Brown_as_df.txt", sep="\t", col.names = NA) #this gives you an excel-style file with as many columns as column names)

somedata <- read.table(file="Brown_as_df.txt", header=TRUE) #Reads that text file back into R for access!

