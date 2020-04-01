from covid19openapi import ThaiCovid19


class ThaiPatient(object):
    """Status for covid-19 patients in Thailand"""

    def __new__(cls):
        thai = ThaiCovid19()
        today = thai.get('today')
        patient = {
            'update': today.get('UpdateDate'),
            'cumulative': today.get('Confirmed'),
            'new': today.get('NewConfirmed'),
            'hospitalized': today.get('Hospitalized'),
            'dead': today.get('Deaths'),
            'goHome': today.get('Recovered'),
            'references': today.get('Source')
        }
        return patient
