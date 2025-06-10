import pandas as pd

# S-a efectuat un studiu despre starea domeniului Data Science, iar datele colectate sunt salvate in
# fisierul "data/surveyDataScience.csv".
#
# 1.a. Sa se stabileasca:

#----------------------------------------------
# numarul de respondenti (de la care s-au colectate informatiile)
df = pd.read_csv("surveyDataSience.csv")
nr_respondenti = df.shape[0]
print("Numarul de respondenti (de la care s-au colectate informatiile)", nr_respondenti)

#---------------------------------------------
# numar si tipul informatiilor (atributelor, proprietatilor) detinute pentru un respondent
num_attributes = df.shape[1]
attribute_types = df.dtypes
print("Numar informatiilor (atributelor, proprietatilor) detinute pentru un respondent: ", num_attributes)
print("Tipul informatiilor (atributelor, proprietatilor) detinute pentru un respondent: ")
print(attribute_types)

#---------------------------------------------
# numarul de respondenti pentru care se detin date complete
num_complete_respondents = df.dropna().shape[0]
print("Numarul de respondenti pentru care se detin date complete: ", num_complete_respondents)

#---------------------------------------------
# durata medie a anilor de studii superioare pentru acesti respondenti (cea efectiva sau cea estimata),
# durata medie a anilor de studii pentru respondentii din Romania si
# durata medie a anilor de studii pentru respondentii din Romania care sunt femei.
# Comparati rezultatele obtinute pentru cele trei grupuri de respondenti.
# Se presupune ca studiile de licenta dureaza 3 ani, cele de master 2 ani si cele de doctorat 3 ani.

def calculate_study_years(education_level):
    mapping = {
        "Bachelor’s degree": 3,
        "Master’s degree": 5,
        "Doctoral degree": 8,
    }
    return mapping.get(education_level, 0)

df["Study Years"] = df["Q4"].apply(calculate_study_years)
avg_study_years = df["Study Years"].mean()
print("Durata medie a anilor de studii superioare pentru acesti respondenti:  ", avg_study_years)

romania_df = df[df["Q3"] == "Romania"]
avg_study_years_romania = romania_df["Study Years"].mean()
print("Durata medie a anilor de studii pentru respondentii din Romania: ", avg_study_years_romania)

romania_women_df = romania_df[romania_df["Q2"] == "Woman"]
avg_study_years_romania_women = romania_women_df["Study Years"].mean()
print("durata medie a anilor de studii pentru respondentii din Romania care sunt femei", avg_study_years_romania_women)


#---------------------------------------------
# numarul de respondenti femei din Romania pentru care se detin date complete

num_complete_romania_women = romania_women_df.dropna().shape[0]
print("numarul de respondenti femei din Romania pentru care se detin date complete: ", num_complete_romania_women)