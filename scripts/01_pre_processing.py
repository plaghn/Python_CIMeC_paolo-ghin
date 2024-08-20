#############################   Final Assignment   ##############################

# Di seguito, riporto il codice utilizzato per importare e pulire il dataframe originale. Questo ha previsto:
#                              - l'importazione del dataframe originale;
#                              - la selezione di determinate colonne;
#                              - l'aggiunta della colonna Subject_ID
#                              - la rimozione di Nan e outliers;
#                              - la trasformazione del dataframe in formato lungo.



# Importare pacchetti necessari
import pandas as pd

# Importare DataFrame
df = pd.read_excel(r"C:\Users\ghinp\Desktop\Nuova cartella\Dataframe_Originale.xlsx")

# Stampare DataFrame Originale
print("Initial DataFrame:")
print(df)

# Tenere solo le colonne utili per le analisi
selected_columns = ['Condition','Training','Duration_P1','Duration_P2','Duration_P3','Order_P1','Order_Training','Order_P2','FL_367_DO','FL_373_DO','AccQ1_P1','AccQ2_P1','AccQ3_P1','AccQ4_P1','AccQ1_P2','AccQ2_P2','AccQ3_P2','AccQ4_P2','AccQ1_P3','AccQ2_P3','AccQ3_P3','AccQ4_P3','AccQ5_P3','AccQ6_P3','AccQ7_P3','AccQ8_P3']

# Creare un nuovo DataFrame con solo le colonne selezionate
simplified_data_pp = df[selected_columns]

# Creare una copia del DataFrame
simplified_data = simplified_data_pp.copy()

# Aggiungere una colonna Subject_ID basata sull'indice
simplified_data['Subject_ID'] = simplified_data_pp.index + 1  # Aggiunge un ID unico ai soggetti

# Rinominare le colonne FL_367_DO e FL_373_DO
simplified_data.rename(columns={'FL_367_DO': 'Order_P3a', 'FL_373_DO': 'Order_P3b'}, inplace=True)

#Settare Ordine di presentazione come variabile categoriale
simplified_data['Order_P1'] = simplified_data['Order_P1'].astype('category').cat.codes
simplified_data['Order_Training'] = simplified_data['Order_Training'].astype('category').cat.codes
simplified_data['Order_P2'] = simplified_data['Order_P2'].astype('category').cat.codes
simplified_data['Order_P3a'] = simplified_data['Order_P3a'].astype('category').cat.codes
simplified_data['Order_P3b'] = simplified_data['Order_P3b'].astype('category').cat.codes

# Stampare il nuovo DataFrame
print("DataFrame after selecting specific columns:")
print(simplified_data)

# Rimuovere righe con celle NaN
data = simplified_data.dropna()
# Stampare nuovo DataFrame
print("DataFrame after removing rows with NaN value in any column:")
print(data)

# Trovare media e ds nei tempi di realizzazione
mean_times = data[['Duration_P1', 'Duration_P2', 'Duration_P3']].mean()
std_times = data[['Duration_P1', 'Duration_P2', 'Duration_P3']].std()

print("\nMean times:")
print(mean_times)

print("\nStandard Deviation times:")
print(std_times)

# Identificare i soggetti fuori dal range 2 SD dalla media Duration
outliers = ((data[['Duration_P1', 'Duration_P2', 'Duration_P3']] > (mean_times + 2 * std_times)) | 
            (data[['Duration_P1', 'Duration_P2', 'Duration_P3']] < (mean_times - 2 * std_times))).all(axis=1)

# Rimuovere i soggetti outlier
filtered_data = data[~outliers].copy()

# Stampare nuovo DataFrame
print("\nFiltered DataFrame (outliers removed):")
print(filtered_data)

# Trasformare in formato lungo
data_long = pd.melt(
    filtered_data,
    id_vars=['Subject_ID', 'Condition', 'Training'],
    value_vars=['AccQ1_P1', 'AccQ2_P1', 'AccQ3_P1', 'AccQ4_P1',
                'AccQ1_P2', 'AccQ2_P2', 'AccQ3_P2', 'AccQ4_P2',
                'AccQ1_P3', 'AccQ2_P3', 'AccQ3_P3', 'AccQ4_P3',
                'AccQ5_P3', 'AccQ6_P3', 'AccQ7_P3', 'AccQ8_P3'],
    var_name='Phase',
    value_name='Accuracy'
)

#Sistemare formati variabili
data_long['Subject_ID'] = data_long['Subject_ID'].astype('category')
data_long['Condition'] = data_long['Condition'].astype('category')
data_long['Training'] = data_long['Training'].astype('category')
data_long['Phase'] = data_long['Phase'].astype('category')
data_long['Accuracy'] = data_long['Accuracy'].astype(int)

# Verificare il risultato
print(data_long.dtypes)

# Mappare le fasi a etichette (P1: Fase 1, P2: Fase 2, etc.)
phase_mapping = {
    'AccQ1_P1': 'Fase 1', 'AccQ2_P1': 'Fase 1', 'AccQ3_P1': 'Fase 1', 'AccQ4_P1': 'Fase 1',
    'AccQ1_P2': 'Fase 2', 'AccQ2_P2': 'Fase 2', 'AccQ3_P2': 'Fase 2', 'AccQ4_P2': 'Fase 2',
    'AccQ1_P3': 'Fase 3', 'AccQ2_P3': 'Fase 3', 'AccQ3_P3': 'Fase 3', 'AccQ4_P3': 'Fase 3',
    'AccQ5_P3': 'Fase 4', 'AccQ6_P3': 'Fase 4', 'AccQ7_P3': 'Fase 4', 'AccQ8_P3': 'Fase 4'
}

data_long['Phase'] = data_long['Phase'].map(phase_mapping)

# Verificare il risultato
print(data_long)
