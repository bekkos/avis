from app import db, User

user1 = User(email="bekkosm@gmail.com", passhash="179ad45c6ce2cb97cf1029e212046e81", name="Martin Isaksen Bekkos")
user2 = User(email="joakpede@gmail.com", passhash="af07c0f4bbcb83a885339ffec096f385", name="Joakim Pedersen")
user3 = User(email="sigvebm@gmail.com", passhash="af07c0f4bbcb83a885339ffec096f385", name="Sigve Bremer Mejdal")

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.commit()