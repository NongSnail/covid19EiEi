from covid19uncle import ThaiCovid19

class ThaiPatient(object):
  """Status for covid-19 patients in Thailand"""
  def __new__(cls):
    thai = ThaiCovid19()
    patient = {
      'update' : thai.get('อัพเดต'),
      'cumulative' : thai.get('ผู้ป่วยสะสม'),
      'new' : thai.get('ผู้ป่วยรายใหม่'),
      'severe' : thai.get('ผู้ป่วยรุนแรง'),
      'dead' : thai.get('ผู้ป่วยเสียชีวิต'),
      'goHome' : thai.get('ผู้ป่วยกลับบ้านแล้ว'),
      'references' : thai.get('อ้างอิง')
    }
    return patient