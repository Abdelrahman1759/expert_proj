# filepath: c:\Users\co.magic\OneDrive - Alexandria National University\Desktop\expert_systems\expert_system.py
import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
from experta import *

# Define the facts
class Patient(Fact):
    """Information about the patient."""
    pass

# Define the expert system
class HeartDiseaseRiskAssessment(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.risk_score = 0

    @Rule(AND(Patient(cholesterol=P(lambda x: x > 240)), Patient(age=P(lambda x: x > 50))))
    def high_risk_cholesterol_age(self):
        self.risk_score += 20
        self.declare(Fact(risk='high'))

    @Rule(AND(Patient(blood_pressure=P(lambda x: x > 140)), Patient(smoking='yes')))
    def high_risk_blood_pressure_smoking(self):
        self.risk_score += 20
        self.declare(Fact(risk='high'))

    @Rule(AND(Patient(exercise='regular'), Patient(bmi=P(lambda x: x < 25))))
    def low_risk_exercise_bmi(self):
        self.risk_score -= 10
        self.declare(Fact(risk='low'))

    @Rule(AND(Patient(age=P(lambda x: x > 60)), Patient(blood_pressure=P(lambda x: x > 150))))
    def high_risk_age_blood_pressure(self):
        self.risk_score += 20
        self.declare(Fact(risk='high'))

    @Rule(AND(Patient(cholesterol=P(lambda x: x < 200)), Patient(exercise='regular')))
    def low_risk_cholesterol_exercise(self):
        self.risk_score -= 10
        self.declare(Fact(risk='low'))

    @Rule(AND(Patient(smoking='no'), Patient(bmi=P(lambda x: x < 30))))
    def low_risk_smoking_bmi(self):
        self.risk_score -= 10
        self.declare(Fact(risk='low'))

    @Rule(AND(Patient(age=P(lambda x: x > 70)), Patient(cholesterol=P(lambda x: x > 220))))
    def high_risk_age_cholesterol(self):
        self.risk_score += 20
        self.declare(Fact(risk='high'))

    @Rule(AND(Patient(blood_pressure=P(lambda x: x < 120)), Patient(exercise='regular')))
    def low_risk_blood_pressure_exercise(self):
        self.risk_score -= 10
        self.declare(Fact(risk='low'))

    @Rule(AND(Patient(smoking='yes'), Patient(age=P(lambda x: x > 50))))
    def high_risk_smoking_age(self):
        self.risk_score += 20
        self.declare(Fact(risk='high'))

    @Rule(AND(Patient(bmi=P(lambda x: x > 30)), Patient(cholesterol=P(lambda x: x > 250))))
    def high_risk_bmi_cholesterol(self):
        self.risk_score += 20
        self.declare(Fact(risk='high'))

    @Rule(Fact(risk='high'))
    def high_risk(self):
        self.result = "The patient is at high risk for heart disease."

    @Rule(Fact(risk='low'))
    def low_risk(self):
        self.result = "The patient is at low risk for heart disease."

    def get_result(self):
        return self.result

    def get_risk_score(self):
        return self.risk_score