from app import db

user1 = User(email="bekkosm@gmail.com", "179ad45c6ce2cb97cf1029e212046e81", "Martin Isaksen Bekkos")
user2 = User(email="joakpede@gmail.com", "af07c0f4bbcb83a885339ffec096f385", "Joakim Pedersen")
user3 = User(email="sigvebm@gmail.com", "af07c0f4bbcb83a885339ffec096f385", "Sigve Bremer Mejdal")

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.commit()