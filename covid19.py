from covid19uncle import ThaiCovid19
thai = ThaiCovid19()

upDate = thai.get('อัพเดต')
cumulative = thai.get('ผู้ป่วยสะสม')
new = thai.get('ผู้ป่วยรายใหม่')
severe = thai.get('ผู้ป่วยรุนแรง')
died = thai.get('ผู้ป่วยเสียชีวิต')
goHome = thai.get('ผู้ป่วยกลับบ้านแล้ว')

refer = thai.get('อ้างอิง')

# print(upDate)