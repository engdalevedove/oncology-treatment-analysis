import pandas as pd
import random
from faker import Faker
import datetime

# Initialize Faker and create a seed for reproducibility
fake = Faker('pt_BR')
random.seed(42)

# Number of patients
num_patients = 100

# Helper functions to generate data


def generate_patient_data():
    name = fake.name()
    phone = fake.phone_number()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
    age = (datetime.datetime.now().year - birth_date.year)
    sex = random.choice(['Masculino', 'Feminino'])
    addiction = random.choice(['Nenhum', 'Álcool', 'Tabaco', 'Ambos'])
    weight = round(random.uniform(50, 100), 2)
    height = round(random.uniform(1.50, 2.00), 2)
    cancer_type = random.choice(
        ['Câncer de boca', 'Câncer de garganta', 'Câncer de laringe', 'Câncer de esôfago'])
    symptom_start = fake.date_between(start_date='-2y', end_date='today')
    diagnosis_date = fake.date_between(
        start_date=symptom_start, end_date='today')
    treatment_start = fake.date_between(
        start_date=diagnosis_date, end_date='today')
    treatment_type = random.choice(
        ['Quimioterapia', 'Radioterapia', 'Cirurgia', 'Imunoterapia'])
    combined_treatment = random.choice(['Sim', 'Não'])
    main_caregiver = random.choice(['Familiar', 'Amigo', 'Profissional'])
    surgery_type = random.choice(['Paliativa', 'Curativa'])
    hospitalization_duration = random.randint(1, 30)
    multidisciplinary_care = random.choice(['Sim', 'Não'])
    navigation_start = fake.date_between(
        start_date=treatment_start, end_date='today')
    navigation_end = fake.date_between(
        start_date=navigation_start, end_date='today')
    num_medical_consultations = random.randint(1, 20)
    num_nurse_consultations = random.randint(1, 20)
    post_surgery_er_visit = random.choice(['Sim', 'Não'])
    post_treatment_er_visit = random.choice(['Sim', 'Não'])
    readmission_complications = random.choice(['Sim', 'Não'])
    family_cancer_history = random.choice(['Sim', 'Não'])
    comorbidities = random.choice(
        ['Diabetes', 'Hipertensão', 'Nenhuma', 'Ambas'])
    socioeconomic_status = random.choice(['Baixo', 'Médio', 'Alto'])
    num_therapy_sessions = random.randint(1, 30)
    treatment_adherence = random.choice(['Alta', 'Média', 'Baixa'])
    quality_of_life = random.choice(['Boa', 'Média', 'Ruim'])
    psychological_impact = random.choice(['Leve', 'Moderado', 'Severo'])

    return [name, phone, birth_date, age, sex, addiction, weight, height, cancer_type, symptom_start,
            diagnosis_date, treatment_start, treatment_type, combined_treatment, main_caregiver, surgery_type,
            hospitalization_duration, multidisciplinary_care, navigation_start, navigation_end, num_medical_consultations,
            num_nurse_consultations, post_surgery_er_visit, post_treatment_er_visit, readmission_complications,
            family_cancer_history, comorbidities, socioeconomic_status, num_therapy_sessions, treatment_adherence,
            quality_of_life, psychological_impact]


# Generate data for all patients
data = [generate_patient_data() for _ in range(num_patients)]

# Create a DataFrame
columns = ['Nome', 'Telefone', 'Data de Nascimento', 'Idade', 'Sexo', 'Vício', 'Peso', 'Altura', 'Tipo de Câncer',
           'Início de Sintomas', 'Data de Diagnóstico', 'Início de Tratamento', 'Tipo de Tratamento',
           'Tratamento Combinado', 'Cuidador Principal', 'Cirurgia Paliativa ou Curativa', 'Tempo de Internação',
           'Atendimento Multidisciplinar', 'Início de Navegação', 'Fim de Navegação', 'Quantidade de Consultas Médicas',
           'Quantidade de Consultas com Enfermeiro Navegador', 'Atendimento no PS Pós-Cirúrgico', 'Atendimento no PS Pós-Início de Tratamento',
           'Reinternação com Complicação Pós-Cirúrgica', 'Histórico Familiar de Câncer', 'Comorbidades', 'Status Socioeconômico',
           'Número de Sessões de Quimioterapia/Radioterapia', 'Adesão ao Tratamento', 'Qualidade de Vida Pós-Tratamento', 'Impacto Psicológico']

df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
output_file = 'patient_data.csv'
df.to_csv(output_file, index=False)

print(f"Arquivo CSV salvo como {output_file}")
