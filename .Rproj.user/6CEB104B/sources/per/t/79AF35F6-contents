path <- "/Users/noah/DSKI/S1/Repos/ErklarbarkeitAlgo/ErklaerbarkeitAlgos/data/"

data <- read.table(file = paste(path, "Multivariate_Log_Reg.txt", sep=""), header = TRUE, sep= "\t",
                   stringsAsFactors = TRUE, dec = ".", na.strings = "NaN")


str(data)

View(data)

# Estimate logistic regression
LLR_Model <- glm(Target ~ x90_1 + x90_2 + x60_1, data = data,
                 family = binomial(link = "logit"))
summary(LLR_Model)            

# Predict logistic regression for training data
LLR_EST <- predict(LLR_Model, data[,2:4], "response")
summary(LLR_EST)

#Check discriminatory power (Wirft noch error wegen fehlender Bib)
auc(roc(Target, LLR_EST))

#Partial Dependence Plots
data_copy <- data
x <- seq(from = -3, to = 3, by = 0.05)

#Save a Vector where to start... Wird für performance vorab spezifiziert
Result_PDP <- rep(NA, length(x))

for(k in 1:length(x)){
  print(k)# Just say where we are
  
  data_copy$x60_1 <- rep(x[k], length(data_copy)) #Replace the variable
  
  PDs <- predict(LLR_Model, data_copy[,-1], "response")
  Result_PDP[k] <- mean(PDs)
}

plot(x, Result_PDP)
