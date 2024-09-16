#############################   Final Assignment   ##############################

# Di seguito, riporto il codice per la visualizzazione dei dati:
#                 - la variabile dipendente è l'accuratezza (media);
#                 - le variabili indipendenti sono la condizione (a due livelli) e il tipo di training (a 3 livelli)

# LP: in the same way, make sure that each script is self-contained, and does not make assumptions about the existence of variables in the global scope,
# and does not assume we have all the libraries already loaded!
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcolare l'accuratezza media per Fase, Condizione e Training
# LP follows from the previous script
data_long = pd.from_csv(r"/Users/vigji/Downloads/Dataframe_Pre_Processed.csv")

mean_accuracy = data_long.groupby(['Phase', 'Condition', 'Training'])['Accuracy'].mean().reset_index()

# Impostare la dimensione della figura
plt.figure(figsize=(12, 6))

# Creare un grafico a linee
sns.lineplot(data=mean_accuracy,
             x='Phase',
             y='Accuracy',
             hue='Condition', #Impostare Colore in base a 'Condition'
             style='Training', #Impostare Stile in base a 'Training'
             markers=True, dashes=False)

# Aggiungere titoli e etichette
plt.title('Accuratezza Media per Fase, Condizione e Training')
plt.xlabel('Phase')
plt.ylabel('Mean Accuracy')
plt.legend(title='Condition and Training')
plt.grid(True)
plt.tight_layout()

# Mostrare il grafico
plt.show()
