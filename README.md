# IMPATTO A BREVE E LUNGO TERMINE DI RAPPRESENTAZIONI GRAFICHE DINAMICHE SUL RAGIONAMENTO BAYESIANO

## Introduzione
Nel corso della vita quotidiana, gli esseri umani producono costantemente giudizi di probabilità, estremamente importanti in molte attività, come l’apprendimento. Tuttavia, numerosi studi hanno evidenziato che questi giudizi, anche quando epressi da esperti, raramente rispettano i principi descritti nel modello normativo. Di conseguenza, in molti hanno cercato di indagare i fattori che potrebbero migliorare la capacità delle persone di risolvere problemi di probabilità. Tra questi, l’utilizzo di rappresentazioni grafiche per visualizzare le informazioni dei problemi ha ricevuto un notevole interesse.

## Obiettivo
Questo progetto ha lo scopo di verificare l'impatto di rappresentazioni grafiche dinamiche sulla capacità di stimare il "Positive Predictive Value" (PPV) e il "Negative Predictive Value" (NPV), due importanti informazioni in ambito medico.

## Disegno sperimentale
Il progetto adotta un disegno between-subjects nel quale sono stati manipolati il tipo di task (due livelli: stimare il PPV o stimare il NPV) e il tipo di training (tre livelli: una rappresentazione dinamica con feedback; una rappresentazione testuale con colori e feedback; una rappresentazione testuale senza colori e senza feedback). Si è sviluppato in quattro fasi che si sono svolte in diversi giorni per indagare gli effetti a breve e lungo termine del training. 

## Analisi
E' stato applicato un Generalized Linear Mixed Model (GLMM), seguito dall'analisi dei contrasti con correzione di Bonferroni.

## Risultati
I risultati sollevano dubbi sulla possibilità che la componente dinamica di un training possa essere di grande aiuto. 

# INSTALLAZIONE
Questo progetto richiede sia Python che R, e include dipendenze per entrambi i linguaggi.

## a. Installare R
Se non hai già R installato, puoi scaricalo dal sito ufficiale di R (https://www.r-project.org/).

## b. Installare pacchetti R necessari
Esegui il seguente comando per installare i pacchetti R:

```bash
install.packages(c("lme4", "emmeans"), dependencies = TRUE)
```

## c. Clonare il Repository
Clona il repository con il seguente comando:

```bash
git clone https://github.com/plaghn/Python_CIMeC_paolo-ghin
```

## d. Installare i pacchetti Python necessari
Installa le dipendenze tramite:

```bash
pip install -r requirements.txt
```

