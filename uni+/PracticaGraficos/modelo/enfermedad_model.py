import pandas as pd
import numpy as np

class EnfermedadModel:

    def __init__(self):
                
    #DATASET GRANDE
        self.df = pd.read_csv(
            "PracticaGraficos/diabetes.csv"
        )

#=========================================================
#TOTAL PACIENTES
#=========================================================  
    def total_pacientes(self):
        return len(self.df)
    
#=========================================================
#PROMEDIO GLUCOSA
#=========================================================  
    def promedio_glucosa(self):
        return np.mean(
            self.df["Glucose"]
        )
    
#=========================================================
#PACIENTES CON GLUCOSA ELEVADA
#=========================================================
    def pacientes_glucosa_elevada(self):
        return len(
            self.df[   
                self.df["Glucose"] > 150
            ]
        )

#=========================================================
#PACIENTES CON BMI ELEVADO
#=========================================================
    def pacientes_bmi_elevado(self):
        return len(
            self.df[   
                self.df["BMI"] > 35
            ]
        )

#=========================================================
#PROMEDIO BMI
#=========================================================
    def promedio_bmi(self):
        return np.mean(
            self.df["BMI"]
        )
    

#=========================================================
#PACIENTES CON DIABETES
#=========================================================
    def pacientes_diabetes(self):
        return len(
            self.df[   
                self.df["Outcome"] == 1
            ]
        )
    
#=========================================================
#PACIENTES SIN DIABETES
#=========================================================
    def pacientes_sanos(self):
        return len(
            self.df[   
                self.df["Outcome"] == 0
            ]
        )
    
#=========================================================
#PACIENTES DE RIESGO
#=========================================================
    def pacientes_de_riesgo(self):
        return self.df[   
                (self.df["Glucose"] > 150) & 
                (self.df["BMI"] > 35)
            ].head(20)
    
#=========================================================
#PACIENTES MAYORES 
#=========================================================
    def pacientes_mayores(self):
        return self.df[   
                self.df["Age"] > 50
            ].head(20)
        