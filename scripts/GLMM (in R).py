################################   Final Assignment ######################################

#Di seguito, riporto il codice utilizzato per eseguire un GLMM. 


# Istogramma e grafico della densità per verifica normalità
plt.figure(figsize=(12, 6))
sns.histplot(data_long['Accuracy'], kde=True)
plt.title('Istogramma Accuracy')
plt.xlabel('Accuracy')
plt.ylabel('Frequency')
plt.show()

# Q-Q plot per la distribuzione normale
plt.figure(figsize=(6, 6))
stats.probplot(data_long['Accuracy'], dist="norm", plot=plt)
plt.title('Q-Q Plot della Accuracy')
plt.show()

#Eseguire il Test di Normalità
# Test di Shapiro-Wilk
stat, p = stats.shapiro(data_long['Accuracy'])
print(f'Shapiro-Wilk Test: Statistic={stat:.3f}, p-value={p:.3f}')
    
# Test di Kolmogorov-Smirnov
stat, p = stats.kstest(data_long['Accuracy'], 'norm', args=(data_long['Accuracy'].mean(), data_long['Accuracy'].std()))
print(f'Kolmogorov-Smirnov Test: Statistic={stat:.3f}, p-value={p:.3f}')

# Attivare la conversione automatica tra pandas e R
pandas2ri.activate()

# Caricare i pacchetti necessari in R
lme4 = importr('lme4')
stats = importr('stats')

# Convertire le colonne categoriali in stringhe (altrimenti errore)
data_long['Phase'] = data_long['Phase'].astype(str)
data_long['Condition'] = data_long['Condition'].astype(str)
data_long['Training'] = data_long['Training'].astype(str)

# Convertire il DataFrame pandas in un DataFrame R
data_long_r = pandas2ri.py2rpy(data_long)

# Definire il DataFrame in R
ro.globalenv['data_long'] = data_long_r

# Cambiare i formati delle variabili
ro.r('''data_long$Subject_ID <- as.factor(data_long$Subject_ID)
        data_long$Phase <- as.factor(data_long$Phase)
        data_long$Condition <- as.factor(data_long$Condition)
        data_long$Training <- as.factor(data_long$Training)
''')

#Verificare l'avvenuta conversione
ro.r('''sapply(data_long, class)
''')

# Eseguire il codice R per il modello GLMM
ro.r('''
library(lme4)

# Modificare la variabile 'Accuracy' per essere binaria
data_long$Accuracy <- as.factor(data_long$Accuracy)

# Specificare il modello GLMM
model <- glmer(Accuracy ~ Condition * Training * Phase + (1 | Subject_ID), 
               data = data_long, 
               family = binomial,
               control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
               
# Ottenere il sommario del modello
model_summary <- summary(model)
''')

# Ottenere l'oggetto R model_summary in Python
model_summary = ro.r('model_summary')

# Stampare il sommario
print(model_summary)

#Eseguire Contrasti con correzione di Bonferroni
ro.r('''

library(emmeans)

# Calcolare le "estimated marginal means"
emm <- emmeans(model, ~ Condition * Training * Phase)

# Visualizzare le emmeans
emm

# Fare Contrasti con conrrezione Bonferroni
pairwise_comparisons <- contrast(emm, method = "pairwise")
results <- summary(pairwise_comparisons, adjust = "bonferroni")

# Filtrare i risultati con p-value < 0.05
significant_results <- results[results$p.value < 0.05, ]

# Visualizzare i risultati significativi
print(significant_results)

''')
