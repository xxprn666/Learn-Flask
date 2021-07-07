from SetupDatabase import db,User

db.create_all()

sam = User('sammy',2)
fran = User('frankie',4)

print(sam.id)
print(fran.id)

db.session.add_all([sam,fran])
db.session.commit()

print(sam.id)
print(fran.id)
