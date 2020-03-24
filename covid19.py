from covid19uncle import ThaiCovid19

thai = ThaiCovid19()

patient = {
  'update' : lambda:thai.get('อัพเดต'),
  'cumulative' : lambda:thai.get('ผู้ป่วยสะสม'),
  'new' : lambda:thai.get('ผู้ป่วยรายใหม่'),
  'severe' : lambda:thai.get('ผู้ป่วยรุนแรง'),
  'dead' : lambda:thai.get('ผู้ป่วยเสียชีวิต'),
  'goHome' : lambda:thai.get('ผู้ป่วยกลับบ้านแล้ว'),
  'references' : lambda:thai.get('อ้างอิง')
}
# print(upDate)