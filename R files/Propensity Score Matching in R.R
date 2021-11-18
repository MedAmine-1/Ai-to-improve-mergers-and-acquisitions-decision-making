# Propensity Score Matching in R
# Copyright 2013 by Ani Katchova

#install.packages("Matching")
library(Matching)
#install.packages("rbounds")
library("rbounds")

mydata<- read.csv("testy.csv")
attach(mydata)

# Defining variables (Tr is treatment, Y is outcome, X are independent variables)
Tr <- cbind(TREAT)
Y <- cbind(enterpriseValue2015)
X <- cbind(Country_BE,Country_CA, Country_DE, Country_FR, Country_United.States,Sector_Communication.Services, Sector_Consumer.Cyclical, Sector_Energy, Sector_Financial.Services,Sector_Healthcare, Sector_Industrials, Sector_Technology,minusCashAndCashEquivalents2013,marketCapitalization2013,addTotalDebt2013,enterpriseValue2013)
var1 <- AGE

# Outcome for difference-in-differences model
Y <- cbind(diff_2013_2015)

# Descriptive statistics
summary (Tr)
summary(Y)
summary(X)
  
# Propensity score model 
glm1 <- glm(Tr ~ X, family=binomial(link = "probit"), data=mydata)
summary(glm1)

# Average treatment on the treated effect
# rr1 <- Match(Y = Y, Tr = Tr, X = glm1$fitted)

rr2 <- Match(Y = Y, Tr = Tr, X = glm1$fitted, estimand = "ATT", M = 1, ties = TRUE, replace = TRUE)
# rr3 <- Match(Y = Y, Tr = Tr, X = glm1$fitted, estimand = "ATE", M = 1, ties = TRUE, replace = TRUE)
summary(rr2)
# Checking the balancing property
MatchBalance(Tr ~ X, match.out = rr1, nboots=0, data=mydata)
qqplot(addTotalDebt2013[rr1$index.control],addTotalDebt2013[rr1$index.treated])
abline(coef = c(0, 1), col = 2)

# Genetic matching
gen1 <- GenMatch(Tr = Tr, X = X, BalanceMatrix = X, pop.size = 1000,print.level=2)
mgen1 <- Match(Y = Y, Tr = Tr, X = X, Weight.matrix = gen1)
MatchBalance(Tr ~ X, data = mydata, match.out = mgen1, nboots = 0)
summary(mgen1)
# Sensitivity tests
psens(mgen1, Gamma=1.7, GammaInc=.05)
hlsens(mgen1, Gamma=1.7, GammaInc=.05, .1)

match1.data <- matches.data(gen1)
View(match1.data)